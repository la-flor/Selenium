from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://www.backcountry.com/Store/catalog/search.jsp?s=u&q=carabiner')

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
        print({ "page": page, "brand": brand, "model": model, "price": clean_price})



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


driver.close()