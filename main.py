import os
import sys
import pandas as pd
import pyexiv2

from PIL import Image
from PIL.ExifTags import TAGS


def extract_image_exif_data(image_path):
    with open(image_path, 'rb') as f:
        with pyexiv2.ImageData(f.read()) as img:
            exif_data = img.read_exif()
            # exif_data_dict = {}
            # for tag, value in exif_data.items():
            #     tag_name = TAGS.get(tag, tag)
            #     exif_data_dict[tag_name] = value
            image_info_dict = {
                'FileName': f.name,
                'Date': exif_data.get('Exif.Image.DateTime', None),
                'ExposureTime': exif_data.get('Exif.Photo.ExposureTime', None),
                # 'RecommendedExposureIndex': exif_data.get('Exif.Photo.RecommendedExposureIndex', None),
                'FNumber': exif_data.get('Exif.Photo.FNumber', None),
                # 'FNumber-Nikon': exif_data.get('Exif.NikonLd4.FNumber', None),
                'ISOSpeedRatings': exif_data.get('Exif.Photo.ISOSpeedRatings', None),
                # 'ISO': exif_data.get('Exif.NikonIi.ISO', None),
                # 'ISO2': exif_data.get('Exif.NikonIi.ISO2', None),
                'FocalLength': exif_data.get('Exif.Photo.FocalLength', None),
                # 'FocalLength-Nikon': exif_data.get('Exif.NikonLd4.FocalLength', None),
                'FocalLengthIn35mmFilm': exif_data.get('Exif.Photo.FocalLengthIn35mmFilm', None)
            }
            return image_info_dict


# cmd: main.py <images_directory> <output_file>
if __name__ == '__main__':
    image_directory = sys.argv[1]
    output_csv_file = sys.argv[2]
    exif_data_list = []
    # load exif data from files in image directory
    for filename in os.listdir(image_directory):
        if filename.endswith('.NEF'):
            try:
                image_path = os.path.join(image_directory, filename)
                exif_data_list.append(extract_image_exif_data(image_path))
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    # save exif data to output file
    df = pd.DataFrame(exif_data_list)
    df.to_csv(output_csv_file, index=False)
