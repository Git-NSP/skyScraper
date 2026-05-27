from selenium import webdriver
from selenium.webdriver.common.by import By
import time

POST_URL = "https://www.linkedin.com/posts/gregorybufithis_today-an-entire-industry-stopped-making-ugcPost-7461015238805663744-Z4cM/?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAABeyIuEBe6BO_Pcop6kr6C_GMg2Uo-SWg74&utm_campaign=copy_link"

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login")

print("Login manually.")

time.sleep(40)

driver.get(POST_URL)

time.sleep(5)

# extract visible text
elements = driver.find_elements(By.TAG_NAME, "span")

for el in elements:

    text = el.text.strip()

    if text:

        print(text)

driver.quit()

