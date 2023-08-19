from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

servico = Service(executable_path="./drivers/geckodriver")

opcoes = Options()
opcoes.add_argument("-headless")


navegador = webdriver.Firefox(service=servico, options=opcoes)
navegador.get("https://github.com/EnzEdu")
print("Titulo da aba: %s" % navegador.title)
navegador.quit()