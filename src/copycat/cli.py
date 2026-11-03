from rich.console import Console
from rich.syntax import Syntax

from copycat.clipboard import copiarContenido
from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Copia el contenido de un fichero y lo muestra por la terminal"
    )
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="copia sin mostrar el contenido")
    parser.add_argument("ruta", type=Path, help="ruta del archivo")

    args = parser.parse_args()
    estado = copiarContenido(args.ruta)

    console = Console()

    if not args.quiet and args.ruta.is_file():
        syntax = Syntax.from_path(args.ruta, line_numbers=True, theme="ansi_dark")
        console.print(syntax)

    print(estado)


if __name__ == "__main__":
    main()
