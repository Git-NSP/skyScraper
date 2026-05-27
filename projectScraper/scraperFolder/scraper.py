# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
# import os
# import time

# driver = webdriver.Chrome()

# URL = "https://unsplash.com/s/photos/living-room"

# driver.get(URL)


# time.sleep(5)

# images = driver.find_elements(By.TAG_NAME, "img")

# print("Number of images:", len(images))

# os.makedirs("../raw_images/living_room", exist_ok=True)

# count = 0

# for img in images:

#     src = img.get_attribute("src")

#     if not src:
#         continue

#     try:
#         img_data = requests.get(src).content

#         with open(f"../raw_images/living_room/image_{count}.jpg", "wb") as f:
#             f.write(img_data)

#         print(f"Downloaded image {count}")

#         count += 1

#     except Exception as e:
#         print(e)

# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# =========================
# CONFIG
# =========================
SAVE_FOLDER = "../raw_images/bedroom"

URL = "https://unsplash.com/s/photos/bedroom"

# URL = "https://unsplash.com/s/photos/living-room"

# SAVE_FOLDER = "../raw_images/living_room"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Referer": "https://unsplash.com"
}

os.makedirs(SAVE_FOLDER, exist_ok=True)

# =========================
# START BROWSER
# =========================

driver = webdriver.Chrome()

driver.get(URL)

# wait for JS rendering
time.sleep(5)

# =========================
# SCROLL PAGE
# =========================

for i in range(3):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(3)

# =========================
# EXTRACT IMAGES
# =========================

images = driver.find_elements(By.TAG_NAME, "img")

print("Images found:", len(images))

count = 0

# =========================
# DOWNLOAD IMAGES
# =========================

for img in images:

    src = img.get_attribute("src")

    if not src:
        continue

    # skip tiny/base64 images
    if "images.unsplash.com" not in src:
        continue

    try:

        response = requests.get(
            src,
            headers=HEADERS
        )

        if response.status_code == 200:

            file_path = (
                f"{SAVE_FOLDER}/image_{count}.jpg"
            )

            with open(file_path, "wb") as f:

                f.write(response.content)

            print(f"Downloaded image {count}")

            count += 1

        else:
            print(
                "Failed:",
                response.status_code
            )

    except Exception as e:
        print(e)

driver.quit()

print("Scraping complete.")

