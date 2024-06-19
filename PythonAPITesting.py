from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = input("Please enter browser where you want to test:")
print(browserName)

if browserName.lower() == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName.lower() == "firefox":
    driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
else:
    print("As of now we are supporting only two browser" + browserName)

# driver.i
# driver.get("https://app.hubspchot.com/login")

