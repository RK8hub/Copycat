from copycat import clipboard, cli


def test_missing_file_prints_error_without_crashing(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["copycat", str(tmp_path / "no-existe.txt")])

    cli.main()

    assert "no existe" in capsys.readouterr().out


def test_quiet_skips_content_and_prints_status(tmp_path, monkeypatch, capsys):
    archivo = tmp_path / "ejemplo.py"
    archivo.write_text("print('hola')\n", encoding="utf-8")
    monkeypatch.setattr(clipboard, "copy", lambda _: None)
    monkeypatch.setattr("sys.argv", ["copycat", "-q", str(archivo)])

    cli.main()

    salida = capsys.readouterr().out
    assert "Contenido copiado con éxito" in salida
    assert "print" not in salida
