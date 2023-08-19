from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

#escolher a URL que o driver vai acessar
driver.get("https://www.google.com/")

#encontrar a estrutura do campo de busca
search_box = driver.find_element("name", "q")

#inserir o texto da pesquisa no campo de busca
search_box.send_keys("Tutorial Selenium")
time.sleep(0.2)

#realizar a busca
search_box.send_keys(Keys.ENTER)

search_box.submit()