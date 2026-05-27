from PIL import Image
import os
import json

# =========================
# CONFIG
# =========================

# IMAGE_FOLDER = "../raw_images/living_room"
IMAGE_FOLDER = "../raw_images/bedroom"

OUTPUT_FILE = "bedroom_metadata.json"

SOURCE = "unsplash"

CATEGORY = "living_room"

metadata = []

# =========================
# PROCESS IMAGES
# =========================

for file_name in os.listdir(IMAGE_FOLDER):

    file_path = os.path.join(
        IMAGE_FOLDER,
        file_name
    )

    try:

        img = Image.open(file_path)

        width, height = img.size

        image_info = {

            "file_name": file_name,

            "width": width,

            "height": height,

            "source": SOURCE,

            "category": CATEGORY
        }

        metadata.append(image_info)

    except Exception as e:

        print(
            f"Failed metadata for: "
            f"{file_name}"
        )

        print(e)

# =========================
# SAVE JSON
# =========================

with open(OUTPUT_FILE, "w") as f:

    json.dump(
        metadata,
        f,
        indent=4
    )

print("Metadata generated.")

