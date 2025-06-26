import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpeg(folder_path):
    if not os.path.isdir(folder_path):
        print(f"No such file or directry: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)
            jpeg_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".jpeg")

            try:
                heif_file = pillow_heif.open_heif(heic_path)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                )
                image.save(jpeg_path, "JPEG")
                print(f"success: {filename} → {os.path.basename(jpeg_path)}")
            except Exception as e:
                print(f"error: {filename} - {e}")

if __name__ == "__main__":
    folder = input("input pass: ").strip()
    convert_heic_to_jpeg(folder)