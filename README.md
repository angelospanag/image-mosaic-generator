# Image Mosaic Generator

Create mosaics of images using a collection of smaller images.

<!-- TOC -->
* [Image Mosaic Generator](#image-mosaic-generator)
  * [🚀 Features](#-features)
  * [Prerequisites](#prerequisites)
    * [1. Install Python 3 and uv](#1-install-python-3-and-uv)
    * [2. Create a virtual environment with all necessary dependencies](#2-create-a-virtual-environment-with-all-necessary-dependencies)
    * [3. Activate the virtual environment](#3-activate-the-virtual-environment)
  * [Usage](#usage)
  * [Linting (using ruff)](#linting-using-ruff)
  * [Formatting (using ruff)](#formatting-using-ruff)
<!-- TOC -->

## 🚀 Features

✅ Converts a target image into a mosaic using folders of other images as source

✅ Uses dominant colors of tiles for better accuracy

✅ Supports multiple folders for tile images

✅ Allows custom tile sizes for high-resolution results

✅ Simple command-line interface (CLI) with [Typer](https://typer.tiangolo.com/)

## Prerequisites

- [Python 3.13.\*](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/)

### 1. Install Python 3 and uv

**MacOS (using `brew`)**

```bash
brew install python3 uv
```

**Ubuntu/Debian**

```bash
sudo apt install python3 python3-venv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create a virtual environment with all necessary dependencies

From the root of the project execute:

```bash
uv sync
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

## Usage

```                                                                                                                                                                             
 Usage: main.py [OPTIONS]                                                                                                                                                                                 
                                                                                                                                                                                                          
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --target-image              TEXT     Path to the target image. [default: None] [required]                                                                                                           │
│ *  --tile-folders              TEXT     List of folders containing tile images. [default: None] [required]                                                                                             │
│    --tile-size                 INTEGER  Size of the tiles in pixels (default is 200). [default: 200]                                                                                                   │
│    --install-completion                 Install completion for the current shell.                                                                                                                      │
│    --show-completion                    Show completion for the current shell, to copy it or customize the installation.                                                                               │
│    --help                               Show this message and exit.                                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Linting (using [ruff](https://docs.astral.sh/ruff/))

```bash
ruff check main.py
```

## Formatting (using [ruff](https://docs.astral.sh/ruff/))

```bash
ruff format main.py
```
