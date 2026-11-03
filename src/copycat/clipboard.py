from pathlib import Path
from pyperclip import copy

def copiarContenido (ruta: Path):
    if not ruta.is_file():
        return ("el archivo a copiar no existe")

    with ruta.open("r", encoding="utf-8") as fichero:
        contenido = fichero.read()


    copy(contenido)
    return ("Contenido copiado con éxito")
