import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Definir o critério de busca
busca = "empreendedorismo"

# Inicializar o navegador e abrir o Instagram
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

# Esperar a página carregar
time.sleep(3)

# Inserir informações de login
usuario = driver.find_element_by_name("username")
usuario.send_keys("seu_nome_de_usuário")
senha = driver.find_element_by_name("password")
senha.send_keys("sua_senha")
senha.send_keys(Keys.RETURN)

# Esperar a página carregar
time.sleep(3)

# Pesquisar por usuários
busca_input = driver.find_element_by_xpath("//input[@placeholder='Pesquisar']")
busca_input.send_keys(busca)
time.sleep(3)
busca_input.send_keys(Keys.RETURN)
time.sleep(3)
busca_input.send_keys(Keys.RETURN)

# Seguir usuários
for i in range(1, 4): # Seguir os 3 primeiros usuários
    try:
        usuario = driver.find_element_by_xpath(f"//div[@class='v1Nh3 kIKUG  _bz0w']/a[{i}]")
        usuario.click()
        time.sleep(2)
        seguir = driver.find_element_by_xpath("//button[text()='Seguir']")
        seguir.click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    except:
        pass

# Fechar o navegador
driver.quit()
