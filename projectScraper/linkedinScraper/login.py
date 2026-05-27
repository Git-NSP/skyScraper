from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login")

print("Please login manually.")

# wait for manual login
time.sleep(60)

print("Login complete.")

# keep browser alive
input("Press Enter to close browser...")

driver.quit()

