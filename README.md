# Image Mosaic Generator

Create mosaics of images using a collection of smaller images.

## Features

- Converts a target image into a mosaic using folders of other images as source
- Uses dominant colors of tiles for better accuracy
- Supports multiple tile image folders
- Configurable tile size for high-resolution results
- Simple CLI via [Typer](https://typer.tiangolo.com/)

## Getting Started

[mise](https://mise.jdx.dev/) manages the pinned toolchain (Python 3.15, uv).

```bash
# macOS / Linux
curl https://mise.run | sh

# Windows
winget install jdx.mise
```

Activate mise in your shell (`~/.zshrc`):

```zsh
eval "$(mise activate zsh)"
```

Then, in the repo:

```bash
mise trust         # one-time
mise install       # downloads Python and uv
mise run install   # installs dependencies into .venv
```

## Usage

```bash
uv run python main.py --target-image path/to/image.jpg --tile-folders path/to/tiles
```

Multiple tile folders:

```bash
uv run python main.py --target-image photo.jpg \
  --tile-folders folder1 --tile-folders folder2 \
  --tile-size 100
```

The output image is saved to `output/` in the current directory.

## Development

| Command              | Description                                 |
|----------------------|---------------------------------------------|
| `mise run install`   | Install dependencies into `.venv`           |
| `mise run test`      | Run tests                                   |
| `mise run fmt`       | Format code via `ruff format`               |
| `mise run lint`      | Lint code via `ruff check`                  |
| `mise run typecheck` | Type check via `ty check`                   |
| `mise run vuln`      | Scan dependencies for known vulnerabilities |
| `mise run deps`      | Update and sync dependencies                |
