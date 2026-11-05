# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All tasks run via `mise run <task>`. The toolchain (Python 3.15, uv) is pinned in `mise.toml`.

| Task | Command |
|---|---|
| Install dependencies | `mise run install` |
| Format | `mise run fmt` |
| Lint | `mise run lint` |
| Type check | `mise run typecheck` |
| Vulnerability audit | `mise run vuln` |
| Run tests | `mise run test` |
| Upgrade dependencies | `mise run deps` |

## Architecture

This is a CLI application — there is no web server. Entry point is `main.py`, which accepts a target image and one or more folders of tile images and generates a photomosaic.

Key functions in `main.py`:

- `get_dominant_color(image)` — resizes an image to 1×1 and returns the resulting pixel (dominant color)
- `process_tile_images(tile_folders, tile_size)` — loads all tile images, resizes them, and extracts dominant colors
- `create_mosaic(target_image_path, tile_folders, tile_size)` — builds the mosaic using a KDTree for nearest-color matching
- `generate_mosaic(...)` — Typer CLI entry point

Run with:

```bash
uv run python main.py --target-image path/to/image.jpg --tile-folders path/to/tiles
```

Tests live in `tests/`. They test `get_dominant_color` with synthetic `PIL.Image.new` images — no external files needed.
