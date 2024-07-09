from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from tabulate import tabulate
import urllib.parse as urlparse
import json
import os
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Caminho para o chromedriver
chromedriver_path = 'C:/chromedriver/chromedriver.exe'

# Configuração do Selenium Wire com o chromedriver
service = Service(chromedriver_path)
options = Options()
options.add_argument("--ignore-certificate-errors")

# Inicializa o driver
driver = webdriver.Chrome(service=service, options=options)

# URL para visitar
url = 'https://estacio.br'
print(f'Visiting: {url}')

# Visita a URL
driver.get(url)

# Espera carregar a página
time.sleep(3)

# Função para rolar a página suavemente até o rodapé
def scroll_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Rola a página até o final
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Executa a função de rolar a página
scroll_page(driver)

# Função para simular evento contextmenu em todos os links e botões
def simulate_contextmenu(driver):
    elements = driver.find_elements(By.XPATH, "//a | //button")
    actions = ActionChains(driver)
    for element in elements:
        try:
            actions.move_to_element(element).context_click().perform()
            time.sleep(0.5)  # Pausa para simular tempo real entre cliques
        except Exception as e:
            print(f"Erro ao clicar em elemento: {e}")

# Executa a função para simular cliques
simulate_contextmenu(driver)

# Captura as requisições feitas pelo site
requests = driver.requests
ga4_events = [request for request in requests if 'https://analytics.google.com/g/collect' in request.url]

# Exibe os eventos do GA4
def parse_ga4_event(url):
    query = urlparse.urlparse(url).query
    params = urlparse.parse_qs(query)
    return params

events_data = []
if ga4_events:
    print(f'{Fore.GREEN}GA4 Events found: {len(ga4_events)}')
    for event in ga4_events:
        parsed_event = parse_ga4_event(event.url)
        event_name = parsed_event.get('en', ['N/A'])[0]
        event_params = {k: v[0] for k, v in parsed_event.items()}
        events_data.append({"event_name": event_name, "parameters": event_params})
    
    print(tabulate([[f"{Fore.BLUE}{event['event_name']}{Style.RESET_ALL}", event["parameters"]] for event in events_data], headers=["Event Name", "Parameters"]))
else:
    print('No GA4 Events found.')

# Gera o arquivo de log em formato JSON
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, 'ga4_events_log.json')
with open(log_file_path, 'w') as log_file:
    json.dump(events_data, log_file, indent=4)

print(f'Log file created: {log_file_path}')

# Fecha o driver
driver.quit()
