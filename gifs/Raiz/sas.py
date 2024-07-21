from selenium import webdriver
import time

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://x.com/home")

# Adds the cookie into current browser context
driver.add_cookie({"name": "twid", "value": "u%3D1603991971982442498",'path':'/','domain':'.x.com'})
time.sleep(35)

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("twid"))
  