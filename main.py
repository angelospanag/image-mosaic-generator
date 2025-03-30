import os
from pathlib import Path
from typing import Any

import numpy as np
import typer
from PIL import Image
from PIL.ImageFile import ImageFile
from numpy import ndarray, dtype
from sklearn.neighbors import KDTree

app = typer.Typer()


def get_dominant_color(image: Image.Image) -> float | tuple[int, ...] | None:
    """Get the dominant color of an image.

    :param image: The image to get the dominant color from
    :return: The dominant color as a pixel
    """
    image = image.resize((1, 1))
    return image.getpixel((0, 0))


def process_tile_images(
    tile_folders, tile_size
) -> tuple[ndarray[tuple[int, ...], dtype[Any]], list[ImageFile]]:
    """Process the tile images of the folders.

    :param tile_folders: The image folders to be used as input to create the mosaic
    :param tile_size: The tile size
    :return:
    """
    tile_data = []
    tile_images = []
    if isinstance(tile_folders, str):
        tile_folders = [tile_folders]  # Convert single folder to list

    for folder in tile_folders:
        for filename in os.listdir(folder):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path).convert("RGB")
                img = img.resize(tile_size)  # Resize tiles to uniform size
                tile_images.append(img)
                tile_data.append(get_dominant_color(img))
            except Exception as e:
                print(f"Skipping {filename}: {e}")

    return np.array(tile_data), tile_images


def create_mosaic(target_image_path, tile_folders, tile_size=(200, 200)) -> None:
    """Creates a mosaic of an image using image folders and saves it.

    :param target_image_path: The path of the target image
    :param tile_folders: The image folders to use sources to generate the mosaic
    :param tile_size: The size of each tile in the generated mosaic image
    :return:
    """
    target_image = Image.open(target_image_path).convert("RGB")
    target_w, target_h = target_image.size
    grid_w, grid_h = target_w // tile_size[0], target_h // tile_size[1]

    # Increase resolution by resizing target image
    # TODO 10x scaling for high res, make that parametrised?
    high_res_w, high_res_h = (
        grid_w * tile_size[0] * 10,
        grid_h * tile_size[1] * 10,
    )
    target_image = target_image.resize((high_res_w, high_res_h))
    grid_w, grid_h = high_res_w // tile_size[0], high_res_h // tile_size[1]

    target_image = target_image.resize((grid_w, grid_h))
    target_pixels = np.array(target_image)

    tile_colors, tile_images = process_tile_images(tile_folders, tile_size)

    tree = KDTree(tile_colors)

    mosaic = Image.new("RGB", (grid_w * tile_size[0], grid_h * tile_size[1]))

    for y in range(grid_h):
        for x in range(grid_w):
            avg_color = target_pixels[y, x]
            dist, idx = tree.query([avg_color], k=1)
            selected_tile = tile_images[idx[0][0]]
            mosaic.paste(selected_tile, (x * tile_size[0], y * tile_size[1]))

    name, ext = os.path.splitext(target_image_path)
    mosaic.save(Path(Path.cwd() / "output" / f"{name}_mosaic{ext}"))


@app.command()
def generate_mosaic(
    target_image: str = typer.Option(..., help="Path to the target image."),
    tile_folders: list[str] = typer.Option(
        ..., help="List of folders containing tile images."
    ),
    tile_size: int = typer.Option(
        200, help="Size of the tiles in pixels (default is 200)."
    ),
):
    create_mosaic(target_image, tile_folders, tile_size=(tile_size, tile_size))


if __name__ == "__main__":
    app()
