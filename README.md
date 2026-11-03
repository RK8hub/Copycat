# Copycat

A small CLI that copies the contents of a file to the clipboard and shows it in the terminal with syntax highlighting.

## Requirements

- Python 3.10 or newer.
- Linux only: a clipboard backend, either `xclip` or `xsel` (on Wayland, `wl-clipboard`).
- macOS and Windows work out of the box.

## Installation

Run these commands from the cloned repository. You can install Copycat with pipx (recommended for CLI tools) or with pip inside a virtual environment.

### Linux

Install a clipboard backend first:

```bash
# Debian/Ubuntu, X11
sudo apt install xclip

# Debian/Ubuntu, Wayland
sudo apt install wl-clipboard

# Arch Linux, X11
sudo pacman -S xclip

# Arch Linux, Wayland
sudo pacman -S wl-clipboard
```

Then install Copycat with a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Or with pipx:

```bash
pipx install .
```

### Windows

The Windows clipboard works out of the box, no extra dependencies are needed. In PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

If PowerShell blocks the activation script, allow it for the current session:

```powershell
Set-ExecutionPolicy -Scope Process RemoteSigned
```

Or with pipx:

```powershell
pipx install .
```

### macOS

The macOS clipboard works out of the box. Install with a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Or with pipx:

```bash
pipx install .
```

## Usage

```bash
copycat <file>
```

Options:

| Option | Description |
| --- | --- |
| `-q`, `--quiet` | Copy the file without printing its contents. |
| `-h`, `--help` | Show help. |

Examples:

```bash
copycat src/copycat/cli.py
copycat -q notes.txt
```

If the file does not exist, the command prints an error message instead of the contents.

## Development

```bash
pip install -e ".[dev]"
python -m pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT. See [LICENSE](LICENSE).

---

# Copycat (Español)

Una utilidad CLI pequeña que copia el contenido de un archivo al portapapeles y lo muestra en la terminal con resaltado de sintaxis.

## Requisitos

- Python 3.10 o superior.
- Solo en Linux: una herramienta de portapapeles, `xclip` o `xsel` (en Wayland, `wl-clipboard`).
- macOS y Windows funcionan sin configuración extra.

## Instalación

Ejecuta estos comandos desde el repositorio clonado. Puedes instalar Copycat con pipx (recomendado para herramientas CLI) o con pip dentro de un entorno virtual.

### Linux

Primero instala una herramienta de portapapeles:

```bash
# Debian/Ubuntu, X11
sudo apt install xclip

# Debian/Ubuntu, Wayland
sudo apt install wl-clipboard

# Arch Linux, X11
sudo pacman -S xclip

# Arch Linux, Wayland
sudo pacman -S wl-clipboard
```

Después instala Copycat con un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

O con pipx:

```bash
pipx install .
```

### Windows

El portapapeles de Windows funciona sin configuración extra. En PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

Si PowerShell bloquea el script de activación, habilítalo para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process RemoteSigned
```

O con pipx:

```powershell
pipx install .
```

### macOS

El portapapeles de macOS funciona sin configuración extra. Instala con un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

O con pipx:

```bash
pipx install .
```

## Uso

```bash
copycat <archivo>
```

Opciones:

| Opción | Descripción |
| --- | --- |
| `-q`, `--quiet` | Copia el archivo sin mostrar su contenido. |
| `-h`, `--help` | Muestra la ayuda. |

Ejemplos:

```bash
copycat src/copycat/cli.py
copycat -q notas.txt
```

Si el archivo no existe, el comando muestra un mensaje de error en lugar del contenido.

## Desarrollo

```bash
pip install -e ".[dev]"
python -m pytest
```

Revisa [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

## Licencia

MIT. Ver [LICENSE](LICENSE).
