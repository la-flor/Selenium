from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import time

# for WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

####################################################################################
############################## Non-Proxied Scraping ################################
####################################################################################

webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True

# Routing if using Chrome driver
options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1200x600')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

# for testing ip identification of proxy
# driver.get('http://ipv4.icanhazip.com')

categories = [
    "sleeping+bags",
    "sleeping+pads",
    "carabiners", 
    "quickdraws", 
    "belay+devices", 
    "chalk", 
    "mens+trail+shoes", 
    "womens+trail+shoes"
]

wait = WebDriverWait(driver, 10)

for category in categories:
    
  driver.get(f'https://www.backcountry.com/Store/catalog/search.jsp?s=u&q={category}')

  def get_products():
      products = driver.find_elements_by_class_name('product')
      for product in products:
          brand = product.find_element_by_class_name('ui-pl-name-brand').text
          model = product.find_element_by_class_name('ui-pl-name-title').text
          model_url = product.find_element_by_class_name('ui-pl-link').get_attribute('href')
          image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ui-pl-img img'))).get_attribute('src')
          try:
              price = product.find_element_by_class_name('ui-pl-pricing-low-price').text
          except:
              price = product.find_element_by_class_name('ui-pl-pricing-high-price').text

          clean_price = re.search("[0-9]+\.[0-9][0-9]", price).group(0)
          print({ "category": category, "page": page, "brand": brand, "model": model, "model_url": model_url, "image": image, "price": clean_price})

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