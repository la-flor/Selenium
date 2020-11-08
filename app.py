from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.backcountry.com/Store/catalog/search.jsp?s=u&q=chalk')

products = browser.find_elements_by_class_name('product')
for product in products:
    product.find_element_by_class_name('ui-pl-name-brand').text
    brand = product.find_element_by_class_name('ui-pl-name-brand').text
    model = product.find_element_by_class_name('ui-pl-name-title').text
    try:
        price = product.find_element_by_class_name('ui-pl-pricing-low-price').text
    except:
        price = product.find_element_by_class_name('ui-pl-pricing-high-price').text

    clean_price = re.search("[0-9]+\.[0-9][0-9]", price).group(0)
    print({ "brand": brand, "model": model, "price": clean_price})

browser.close()