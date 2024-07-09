from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configuração do chromedriver
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--headless")  # Opcional, executa o Chrome em modo headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('C:/chromedriver/chromedriver.exe')  # Atualize com o caminho do seu chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL do site a ser visitado
url = 'https://ibmec.br'

# Função para esperar elementos específicos na página
def wait_for_element(xpath, timeout=10):
    for _ in range(timeout):
        try:
            if driver.find_element(By.XPATH, xpath):
                return True
        except:
            time.sleep(1)
    return False

# Visitando a página
driver.get(url)
print(f"Visiting: {url}")

# Aguardando a página carregar completamente
time.sleep(10)  # Ajuste o tempo conforme necessário para garantir a carga completa da página

# Simulação de navegação
actions = ActionChains(driver)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
actions.send_keys(Keys.PAGE_UP).perform()
time.sleep(2)

# Verificando a captura de eventos do GA4
requests = driver.requests
ga4_events = [request for request in requests if 'https://analytics.google.com/g/collect' in request.url]

if ga4_events:
    print("GA4 Events found:")
    for event in ga4_events:
        print(event.url)
else:
    print("No GA4 Events found")

# Fechando o navegador
driver.quit()
