def patch(path, pairs):
    s = open(path, encoding="utf8").read()
    for old, new in pairs:
        n = s.count(old)
        assert n == 1, (path, n, old[:90])
        s = s.replace(old, new)
    open(path, "w", encoding="utf8", newline="\n").write(s)
