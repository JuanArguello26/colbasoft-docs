# MVP COLBASOFT en OutSystems — empezar aquí (equipo con Windows)

**Objetivo:** el lunes 23 de noviembre de 2026 mostrar COLBASOFT funcionando en OutSystems (sin diapositivas) con:
1. Base de datos y front-end.
2. Botones de eliminar en los formularios que lo necesitan.
3. Consultas adicionales.

**Por qué en Windows:** Service Studio / ODC Studio (donde se construye en OutSystems) solo existen para Windows y macOS; el equipo principal usa Pop!_OS (Linux).

| Archivo | Para qué |
|---|---|
| `README.md` | Este archivo: preparar el equipo (pasos 1 a 4) |
| `GUIA_MVP.md` | Construir el MVP en OutSystems, parte por parte (paso 5) |
| `COLBASOFT_OutSystems.xlsx` | Se importa en OutSystems y crea las 16 tablas con datos ficticios |
| `generar_excel.js` | Regenera el Excel desde `colbasoft-app/data/datos_ficticios.xlsx` (no hace falta en Windows) |

---

## 1. Traer el repositorio

**Primera vez (el equipo no tiene el repositorio):**
1. Instalar **Git for Windows**: https://git-scm.com/download/win (todo con las opciones por defecto; incluye *Git Credential Manager*).
2. Abrir **PowerShell** y ejecutar:
   ```powershell
   cd $HOME\Documents
   git clone https://github.com/JuanArguello26/colbasoft-docs.git
   ```
   Si el repositorio es privado se abre el navegador para iniciar sesión en GitHub: autorizar y listo (queda guardado).
3. La carpeta de trabajo queda en `Documents\colbasoft-docs\08_OUTSYSTEMS_MVP`.

**Las veces siguientes (ya clonado):**
```powershell
cd $HOME\Documents\colbasoft-docs
git pull
```

*(Sin Git: en github.com, repositorio `colbasoft-docs` → botón **Code** → **Download ZIP** → descomprimir.)*

## 2. Cuenta de OutSystems
1. Entrar a https://www.outsystems.com y crear la cuenta gratuita (**Start free** / *Sign up*).
2. Según lo que ofrezca la cuenta:
   - **ODC** (OutSystems Developer Cloud, la opción gratuita actual): se crea una organización y se entra al **ODC Portal**.
   - **OutSystems 11** (*Personal Environment*): se crea el entorno personal.

La guía sirve para ambas; donde cambia algo, lo indica.

## 3. Instalar el editor
- **ODC:** en el ODC Portal, opción de descarga de **ODC Studio** → instalar → abrir → iniciar sesión con la cuenta (elegir la organización).
- **OutSystems 11:** descargar **Service Studio** desde la página de la cuenta / Personal Environment → instalar → abrir → conectarse al entorno personal con usuario y clave.

Requisitos razonables: 8 GB de RAM o más y conexión estable (cada publicación se compila en la nube).

## 4. Comprobar que todo funciona
1. En el editor: **Create** → **App** → **Reactive Web App** (en ODC: *Web app*) → nombre `COLBASOFT`.
2. Publicar vacía (**1-Click Publish** / *Publish*). Debe terminar sin errores y abrir la app en el navegador.

## 5. Construir el MVP
Abrir **`GUIA_MVP.md`** (en GitHub se ve con formato) y seguirla en orden:
- Parte 1: importar `COLBASOFT_OutSystems.xlsx` **una sola vez en la app nueva y vacía** → convertir los `…Id` en relaciones → diagrama de entidades → pantallas generadas.
- Parte 2: acciones y botones de eliminar.
- Parte 3: consultas (existencia, «¿dónde está?», gráfico por categoría, kardex con saldo).

Al final de `GUIA_MVP.md` está el orden de la demostración del lunes.

## Si se usa Claude Code en el equipo Windows
Abrir Claude Code en la carpeta `colbasoft-docs` y decir: *«Vamos a construir el MVP en OutSystems; lee 08_OUTSYSTEMS_MVP/README.md y GUIA_MVP.md»*. Claude no puede manejar Service Studio por sí solo (salvo que la sesión tenga control del computador habilitado), así que el flujo es: tú haces clics, Claude te dice qué hacer y resuelve errores, expresiones y SQL a partir de lo que le pegues o le muestres en capturas.
