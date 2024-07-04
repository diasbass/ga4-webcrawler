from seleniumwire import webdriver  # Importa o Selenium Wire
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless (sem interface gráfica)
chrome_options.add_argument('--ignore-certificate-errors')  # Ignora erros de certificado SSL
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
service = Service('C:/chromedriver/chromedriver.exe')  # Caminho absoluto para o ChromeDriver

# Inicializa o driver com Selenium Wire
driver = webdriver.Chrome(service=service, options=chrome_options)

def navigate_and_collect_events(url):
    try:
        driver.get(url)
        print(f"Página carregada: {url}")
        
        # Aguarda tempo suficiente para o carregamento dos eventos de GA4
        time.sleep(15)
        
        # Identifica e coleta eventos de GA4 nas solicitações de rede
        ga4_events = set()
        for request in driver.requests:
            if request.response:
                if 'collect' in request.path and 'google-analytics.com' in request.host:
                    ga4_events.add(request.path)
                    print(f"Evento GA4 encontrado: {request.path}")
        
        return ga4_events
    except Exception as e:
        print(f"Erro ao navegar para {url}: {e}")
        return set()

def find_links_on_page(url):
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http') and url in href:
                links.add(href)
            elif href.startswith('/'):
                links.add(url + href)
        return links
    except Exception as e:
        print(f"Erro ao encontrar links na página {url}: {e}")
        return set()

def crawl_site(start_url):
    visited = set()
    to_visit = {start_url}
    all_events = set()

    while to_visit:
        current_url = to_visit.pop()
        if current_url not in visited:
            print(f"Visiting: {current_url}")
            visited.add(current_url)
            events = navigate_and_collect_events(current_url)
            all_events.update(events)
            links = find_links_on_page(current_url)
            to_visit.update(links)
    
    return all_events

# URL inicial
start_url = 'https://google.com.br'  # Substitua pela URL inicial

# Executa o crawler
ga4_events = crawl_site(start_url)

print("GA4 Events found:")
for event in ga4_events:
    print(event)

# Encerra o WebDriver
driver.quit()
