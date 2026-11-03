from copycat import clipboard


def test_copies_file_contents(tmp_path, monkeypatch):
    archivo = tmp_path / "ejemplo.txt"
    archivo.write_text("hola\n", encoding="utf-8")
    copiado = []
    monkeypatch.setattr(clipboard, "copy", copiado.append)

    estado = clipboard.copiarContenido(archivo)

    assert copiado == ["hola\n"]
    assert estado == "Contenido copiado con éxito"


def test_missing_file_reports_error(tmp_path, monkeypatch):
    copiado = []
    monkeypatch.setattr(clipboard, "copy", copiado.append)

    estado = clipboard.copiarContenido(tmp_path / "no-existe.txt")

    assert copiado == []
    assert estado == "el archivo a copiar no existe"
