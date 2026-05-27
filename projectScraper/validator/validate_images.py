from PIL import Image
import os

# Folder containing category folders
BASE_FOLDER = "../raw_images"

MIN_WIDTH = 256
MIN_HEIGHT = 256

for category in os.listdir(BASE_FOLDER):

    category_path = os.path.join(BASE_FOLDER, category)

    # Skip non-folders
    if not os.path.isdir(category_path):
        continue

    for file in os.listdir(category_path):

        file_path = os.path.join(category_path, file)

        try:
            # Open image safely
            with Image.open(file_path) as img:

                width, height = img.size

                print(f"Checking {file} ({width}x{height})")

                # Remove very small images
                if width < MIN_WIDTH or height < MIN_HEIGHT:

                    print(f"Removing small image: {file}")

                    # Image closes automatically after this block
                    pass

                else:
                    continue

            # Delete AFTER image is closed
            os.remove(file_path)

        except Exception as e:

            print(f"Corrupted image: {file}")

            try:
                os.remove(file_path)
                print(f"Deleted corrupted image: {file}")

            except Exception as delete_error:
                print(f"Could not delete {file}: {delete_error}")