import os
from PIL import Image, UnidentifiedImageError
from pathlib import Path

path = Path("input/full").rglob("**/*.*")
for img_p in path:
    try:
        img = Image.open(img_p)
    except UnidentifiedImageError:
        print("Removing " + str(img_p))
        os.remove(img_p)
