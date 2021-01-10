from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Routing if using Firefox driver - comment out if doesn't apply
# driver = webdriver.Firefox()

# Routing if using Chrome driver - comment out if doesn't apply
options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1200x600')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)


categories = [
    "carabiners", 
    "quickdraws", 
    "belay+devices", 
    "chalk", 
    "mens+trail+shoes", 
    "womens+trail+shoes",
    "sleeping+bags",
    "sleeping+pads"
]

for category in categories:
    
    driver.get(f'https://www.backcountry.com/Store/catalog/search.jsp?s=u&q=${category}')

    def get_products():
        products = driver.find_elements_by_class_name('product')
        for product in products:
            brand = product.find_element_by_class_name('ui-pl-name-brand').text
            model = product.find_element_by_class_name('ui-pl-name-title').text
            try:
                price = product.find_element_by_class_name('ui-pl-pricing-low-price').text
            except:
                price = product.find_element_by_class_name('ui-pl-pricing-high-price').text

            clean_price = re.search("[0-9]+\.[0-9][0-9]", price).group(0)
            print({ "category": category, "page": page, "brand": brand, "model": model, "price": clean_price})



    # BEGIN EXECUTION:

    page = 1

    get_products()

    loop = True
    while loop:
        try:
            next_page = driver.find_element_by_link_text('Next Page')
            next_page.click()

            time.sleep(3)
            page += 1

            get_products()
        except:
            loop = False