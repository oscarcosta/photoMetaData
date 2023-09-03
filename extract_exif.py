import sys
import pyexiv2

from PIL import Image
from PIL.ExifTags import TAGS

print('PIL output')
image_path = sys.argv[1]  # input file name
image = Image.open(image_path)
exif_data = image.getexif()
for tag, value in exif_data.items():
    tag_name = TAGS.get(tag, tag)
    print(f'{tag_name}: {value}')

print('pyexiv2 output')
with open(image_path, 'rb') as f:
    with pyexiv2.ImageData(f.read()) as img:
        exif_data = img.read_exif()
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            print(f'{tag_name}: {value}')
