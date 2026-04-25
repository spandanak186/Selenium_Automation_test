from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_login():
    driver.get("https://example.com")
    time.sleep(2)

    # Dummy example (replace with real site if needed)
    print("Opened website successfully")

    driver.quit()

if __name__ == "__main__":
    test_login()
