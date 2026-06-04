from PIL import Image

from main import get_dominant_color


def test_get_dominant_color_red():
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    result = get_dominant_color(img)
    assert result == (255, 0, 0)


def test_get_dominant_color_white():
    img = Image.new("RGB", (50, 50), color=(255, 255, 255))
    result = get_dominant_color(img)
    assert result == (255, 255, 255)


def test_get_dominant_color_black():
    img = Image.new("RGB", (10, 10), color=(0, 0, 0))
    result = get_dominant_color(img)
    assert result == (0, 0, 0)
