from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

servico = Service(executable_path="./drivers/geckodriver")

navegador = webdriver.Firefox(service=servico)
navegador.get("https://github.com/EnzEdu")
print("Titulo da aba: %s" % navegador.title)
navegador.quit()