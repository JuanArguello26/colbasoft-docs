// Genera el Excel para "Import Entities from Excel" de OutSystems a partir de datos_ficticios.xlsx.
// Uso (desde colbasoft-app, que tiene exceljs):
//   NODE_PATH=$PWD/node_modules node ../colbasoft-docs/08_OUTSYSTEMS_MVP/generar_excel.js data/datos_ficticios.xlsx ../colbasoft-docs/08_OUTSYSTEMS_MVP/COLBASOFT_OutSystems.xlsx
// Cada hoja = una entidad, en orden de dependencias. Los *Id son el número de fila (1..n) de la hoja referida.
const E = require('exceljs');
const [, , origen, destino] = process.argv;

// Generador pseudoaleatorio fijo para que el archivo sea reproducible
let semilla = 20261123;
const azar = () => ((semilla = (semilla * 1103515245 + 12345) % 2147483648) / 2147483648);
const elegir = (a) => a[Math.floor(azar() * a.length)];
const fecha = (dia, hora) => new Date(Date.UTC(2026, 9, 1 + dia, hora, 0, 0)); // desde 1-oct-2026

(async () => {
  const src = new E.Workbook();
  await src.xlsx.readFile(origen);
  const filas = (n) => {
    const ws = src.getWorksheet(n); const out = []; let cab;
    ws.eachRow((r, i) => { const v = r.values.slice(1); if (i === 1) cab = v; else out.push(Object.fromEntries(cab.map((c, j) => [c, v[j] ?? '']))); });
    return out;
  };

  const T = {}; // nombre de hoja -> {cols, rows}
  const tabla = (nombre, cols) => (T[nombre] = { cols, rows: [] });
  const add = (nombre, obj) => { T[nombre].rows.push(obj); return T[nombre].rows.length; }; // devuelve Id

  // Catálogos simples (en vez de Static Entities, para importarlos también)
  tabla('UnidadMedida', ['Nombre']);
  const unidad = {}; for (const [k, n] of [['UNIDADES', 'Unidades'], ['METROS', 'Metros'], ['ROLLOS', 'Rollos'], ['KILOGRAMOS', 'Kilogramos']]) unidad[k] = add('UnidadMedida', { Nombre: n });
  tabla('TipoZona', ['Nombre']);
  const tzona = {}; for (const [k, n] of [['RECEPCION', 'Recepción'], ['ALMACENAMIENTO', 'Almacenamiento'], ['PREPARACION_SALIDA', 'Preparación de salida'], ['CUARENTENA', 'Cuarentena']]) tzona[k] = add('TipoZona', { Nombre: n });
  tabla('TipoMovimiento', ['Nombre', 'Signo']);
  const tmov = { ENTRADA: add('TipoMovimiento', { Nombre: 'Entrada', Signo: 1 }), INTERNO: add('TipoMovimiento', { Nombre: 'Movimiento interno', Signo: 0 }), SALIDA: add('TipoMovimiento', { Nombre: 'Salida', Signo: -1 }) };
  tabla('EstadoSalida', ['Nombre']);
  const est = {}; for (const n of ['Solicitada', 'Autorizada', 'Confirmada', 'Cancelada']) est[n] = add('EstadoSalida', { Nombre: n });

  tabla('Categoria', ['Nombre', 'Activa']);
  const cat = {}; for (const c of filas('categorias')) cat[c.nombre] = add('Categoria', { Nombre: c.nombre, Activa: true });

  const refs = filas('referencias');
  tabla('Talla', ['Nombre']); tabla('Color', ['Nombre']);
  const talla = {}, color = {};
  for (const r of refs) {
    for (const t of String(r.tallas).split(',')) if (!talla[t]) talla[t] = add('Talla', { Nombre: t });
    for (const c of String(r.colores).split(',')) if (!color[c]) color[c] = add('Color', { Nombre: c });
  }

  tabla('Referencia', ['Codigo', 'Descripcion', 'CategoriaId', 'UnidadMedidaId', 'Activa']);
  tabla('Sku', ['ReferenciaId', 'TallaId', 'ColorId', 'CodigoSku']);
  const skus = []; // {id, ref}
  for (const r of refs) {
    const rid = add('Referencia', { Codigo: r.codigo, Descripcion: r.descripcion, CategoriaId: cat[r.categoria], UnidadMedidaId: unidad[r.unidad_medida], Activa: true });
    for (const t of String(r.tallas).split(',')) for (const c of String(r.colores).split(','))
      skus.push({ id: add('Sku', { ReferenciaId: rid, TallaId: talla[t], ColorId: color[c], CodigoSku: `${r.codigo}-${t}-${c.slice(0, 3).toUpperCase()}` }), ref: r });
  }

  tabla('Bodega', ['Codigo', 'Nombre']);
  const bod = {}; for (const b of filas('bodegas')) bod[b.codigo] = add('Bodega', { Codigo: b.codigo, Nombre: b.nombre });

  // Zonas con categoría primero, para que OutSystems infiera CategoriaId como número
  const zonasSrc = filas('zonas').sort((a, b) => (b.categoria ? 1 : 0) - (a.categoria ? 1 : 0));
  tabla('Zona', ['BodegaId', 'Codigo', 'Nombre', 'TipoZonaId', 'CategoriaId']);
  const zona = {}, zonaCat = {};
  for (const z of zonasSrc) { zona[z.codigo] = add('Zona', { BodegaId: bod[z.bodega], Codigo: z.codigo, Nombre: z.nombre, TipoZonaId: tzona[z.tipo], CategoriaId: z.categoria ? cat[z.categoria] : 0 }); if (z.categoria) zonaCat[z.categoria] = z.codigo; }

  tabla('Ubicacion', ['ZonaId', 'Codigo', 'Capacidad', 'Activa']);
  const ubic = {}, ubicPorZona = {};
  for (const u of filas('ubicaciones')) {
    const id = add('Ubicacion', { ZonaId: zona[u.zona], Codigo: u.codigo, Capacidad: u.zona.startsWith('ALM') ? 500.5 : 200.5, Activa: true });
    ubic[u.codigo] = id; (ubicPorZona[u.zona] ??= []).push(id);
  }

  // Lotes + kardex (Movimiento). Cantidad positiva suma existencia en la ubicación, negativa resta.
  tabla('Lote', ['SkuId', 'Codigo', 'Origen', 'FechaIngreso']);
  tabla('Movimiento', ['LoteId', 'UbicacionId', 'TipoMovimientoId', 'Cantidad', 'Fecha', 'Responsable', 'Observacion']);
  tabla('Salida', ['Numero', 'BodegaId', 'Motivo', 'EstadoSalidaId', 'Fecha', 'Responsable']);
  tabla('LineaSalida', ['SalidaId', 'LoteId', 'Cantidad']);
  const personas = ['Persona Demo Jefe de Bodega', 'Persona Demo Coordinadora', 'Persona Demo Auxiliar 1', 'Persona Demo Auxiliar 2'];
  const proveedores = ['Proveedor Ficticio Textiles S.A.S.', 'Taller Ficticio Confecciones', 'Distribuidora Ficticia de Insumos'];
  const motivosSalida = ['Despacho a cliente', 'Envío a taller de confección', 'Traslado a punto de venta', 'Muestra comercial'];
  const saldo = []; // {lote, ubic, cant, dia}
  const usados = new Set();
  for (let i = 0; i < 45; i++) {
    let s; do { s = elegir(skus); } while (usados.has(s.id)); usados.add(s.id);
    const dia = Math.floor(azar() * 40);
    const telas = s.ref.categoria === 'Telas';
    const cant = telas ? Math.round((20 + azar() * 80) * 10) / 10 + 0.5 : 10 * (1 + Math.floor(azar() * 12));
    const lote = add('Lote', { SkuId: s.id, Codigo: `L-2026-${String(i + 1).padStart(3, '0')}`, Origen: elegir(proveedores), FechaIngreso: fecha(dia, 0) });
    const rec = elegir(ubicPorZona.REC);
    add('Movimiento', { LoteId: lote, UbicacionId: rec, TipoMovimientoId: tmov.ENTRADA, Cantidad: cant, Fecha: fecha(dia, 8), Responsable: elegir(personas), Observacion: 'Recepción de mercancía' });
    if (i % 6 === 5) { saldo.push({ lote, ubic: rec, cant, dia }); continue; } // queda en recepción
    const destino = elegir(ubicPorZona[zonaCat[s.ref.categoria]]);
    add('Movimiento', { LoteId: lote, UbicacionId: rec, TipoMovimientoId: tmov.INTERNO, Cantidad: -cant, Fecha: fecha(dia, 11), Responsable: elegir(personas), Observacion: 'Sale de recepción' });
    add('Movimiento', { LoteId: lote, UbicacionId: destino, TipoMovimientoId: tmov.INTERNO, Cantidad: cant, Fecha: fecha(dia, 11), Responsable: elegir(personas), Observacion: 'Ubicado en almacenamiento' });
    saldo.push({ lote, ubic: destino, cant, dia });
  }
  // Salidas: agrupa 2-3 lotes con existencia en almacenamiento
  const disponibles = saldo.filter((x) => !ubicPorZona.REC.includes(x.ubic));
  let n = 1001, k = 0;
  for (let sIdx = 0; sIdx < 12; sIdx++) {
    const estado = ['Confirmada', 'Confirmada', 'Confirmada', 'Solicitada', 'Autorizada', 'Cancelada'][sIdx % 6];
    const dia = 30 + Math.floor(azar() * 16);
    const sal = add('Salida', { Numero: n++, BodegaId: bod.B1, Motivo: elegir(motivosSalida), EstadoSalidaId: est[estado], Fecha: fecha(dia, 14), Responsable: elegir(personas) });
    const lineas = 2 + (sIdx % 2);
    for (let j = 0; j < lineas && k < disponibles.length; j++, k++) {
      const x = disponibles[k];
      const q = x.cant >= 20 ? Math.round(x.cant * (0.2 + azar() * 0.5)) : x.cant;
      add('LineaSalida', { SalidaId: sal, LoteId: x.lote, Cantidad: q });
      if (estado === 'Confirmada') { add('Movimiento', { LoteId: x.lote, UbicacionId: x.ubic, TipoMovimientoId: tmov.SALIDA, Cantidad: -q, Fecha: fecha(Math.max(dia, x.dia + 1), 15), Responsable: elegir(personas), Observacion: `Salida N.º ${n - 1}` }); x.cant -= q; }
    }
  }
  // Ordena el kardex por fecha (el Id quedará cronológico)
  T.Movimiento.rows.sort((a, b) => a.Fecha - b.Fecha);

  const out = new E.Workbook();
  for (const [nombre, { cols, rows }] of Object.entries(T)) {
    const ws = out.addWorksheet(nombre);
    ws.addRow(cols);
    for (const r of rows) ws.addRow(cols.map((c) => r[c]));
    ws.getRow(1).font = { bold: true };
    ws.columns.forEach((c) => (c.width = 18));
  }
  await out.xlsx.writeFile(destino);
  for (const [nombre, { rows }] of Object.entries(T)) console.log(nombre.padEnd(15), rows.length);
  const neg = saldo.filter((x) => x.cant < 0); console.log('saldos negativos:', neg.length);
})();
