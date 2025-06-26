#!/usr/bin/env python3

import os
import sys
import argparse
from PIL import Image
import pillow_heif

def load_image(path):
    if path.lower().endswith(".heic"):
        heif_file = pillow_heif.open_heif(path)
        return Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
        )
    else:
        return Image.open(path)

def process_images(folder_path, convert=False, rotate_angle=None):
    if not os.path.isdir(folder_path):
        print(f"[ERROR] Not a valid directory: {folder_path}")
        return

    if convert:
        output_folder = os.path.join(folder_path, "JPEG")
        os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".heic", ".jpeg", ".jpg", ".png")):
            input_path = os.path.join(folder_path, filename)

            try:
                image = load_image(input_path)

                # Rotation
                if rotate_angle is not None:
                    image = image.rotate(rotate_angle, expand=True)
                    print(f"[INFO] Rotated: {filename} ({rotate_angle} degrees)")

                # Conversion
                if convert and filename.lower().endswith(".heic"):
                    output_name = os.path.splitext(filename)[0] + ".jpeg"
                    output_path = os.path.join(output_folder, output_name)
                    image.save(output_path, "JPEG")
                    print(f"[INFO] Converted: {filename} → JPEG/{output_name}")
                elif rotate_angle is not None and not convert:
                    image.save(input_path)
                    print(f"[INFO] Overwritten with rotation: {filename}")

            except Exception as e:
                print(f"[ERROR] Failed to process {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Batch process HEIC and image files (convert, rotate).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("folder", help="Target folder path containing images.")
    parser.add_argument("--convert", action="store_true", help="Convert HEIC to JPEG.")
    parser.add_argument("--rotate", type=int, help="Rotate images by given degrees (e.g., 90, -90, 180).")
    args = parser.parse_args()

    process_images(args.folder, convert=args.convert, rotate_angle=args.rotate)

if __name__ == "__main__":
    main()