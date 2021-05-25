from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import time

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

for category in categories:
    
  driver.get(f'https://www.rei.com/search?q={category}')


  def get_products():
      search_results = driver.find_elements_by_class_name("pPe0GNuagvmEFURs1Q_vm")
      for product in search_results:
          brand = product.find_element_by_class_name('_1fwp3k8dh1lbhAAenp87CH').text
          model = product.find_element_by_class_name('r9nAQ5Ik_3veCKyyZkP0b').text
          image = product.find_element_by_class_name('_23ES_joIv97BfU9tvFOCdR').get_attribute('src')

          try:
              price = product.find_element_by_class_name('_2xZVXKL4Bd0pJyQCumYi9P').text
          except:
              price = product.find_element_by_class_name('_1zwqhlCzOK-xETXwFg_-iZ').find_element_by_tag_name('span').text

          clean_price = re.search("[0-9]+\.[0-9][0-9]", price).group(0)
          print({ "category": category, "page": page, "brand": brand, "model": model, "price": clean_price, "image": image})

  # BEGIN EXECUTION:

  page = 1

  get_products()  

  loop = True
  while loop:
      try:
          page += 1
          driver.get(f'https://www.rei.com/search?q={category}&page={page}')

          get_products()
      except:
          loop = False