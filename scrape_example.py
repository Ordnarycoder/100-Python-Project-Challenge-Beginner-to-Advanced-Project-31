from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

path = "C:/Users/msı/Desktop/chromedriver-win64/chromedriver.exe"

chrome_options = Options()
chrome_service = Service(executable_path=path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

website = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

driver.get(website)

all_matches_button = driver.find_elements(By.CSS_SELECTOR, "a.title")
links = [match.get_attribute("href") for match in all_matches_button]

products = []

for link in links:
    driver.get(link)  
    
    img = driver.find_element(By.CSS_SELECTOR, "img.img-fluid.img-responsive")
    img_link = img.get_attribute("src")
    title = driver.find_element(By.CSS_SELECTOR, "h4.title.card-title").text
    price = driver.find_element(By.CSS_SELECTOR, "h4.price.float-end.pull-right").text
    battery_time = driver.find_element(By.CSS_SELECTOR, "p.description.card-text").text
    review_count = driver.find_element(By.CSS_SELECTOR, "p.review-count").text
    star_count = len(driver.find_elements(By.CSS_SELECTOR, "span.ws-icon.ws-icon-star"))

    product = {
        "img-link": img_link,
        "title": title,
        "price": price,
        "battery-time": battery_time,
        "review-count": review_count,
        "star-count": star_count
    }

    products.append(product)
    time.sleep(1) 

df = pd.DataFrame(products)
df.to_excel("products.xlsx", index=False)

driver.quit()

print("Data scraped successfully!")
