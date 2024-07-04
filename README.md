
# Web Crawler para Captura de Eventos GA4

Este projeto utiliza Selenium Wire para navegar em um site e capturar eventos do Google Analytics 4 (GA4). O script foi configurado para ignorar erros de certificado SSL e executar o Chrome em modo headless.

## Pré-requisitos

Antes de rodar o script, você precisará ter o seguinte instalado:

- Python 3.12 ou superior
- Google Chrome
- ChromeDriver compatível com a versão do seu Chrome
- Selenium Wire
- BeautifulSoup4

## Instalação

1. **Clone o Repositório**
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as Dependências**
   ```sh
   pip install selenium-wire beautifulsoup4
   ```

3. **Baixe o ChromeDriver**
   Baixe o ChromeDriver compatível com a versão do seu Google Chrome em [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

4. **Configure o Caminho do ChromeDriver**
   Atualize o caminho absoluto para o ChromeDriver no script `webdriver.py`:
   ```python
   service = Service('C:/caminho-para-o-chromedriver/chromedriver.exe')
   ```

## Execução

1. **Execute o Script**
   ```sh
   python webdriver.py
   ```

2. **Resultados**
   O script navegará pelo site `https://geekproject.com.br`, capturando e exibindo os eventos GA4 encontrados nas solicitações de rede.

## Estrutura do Projeto

```
.
├── webdriver.py
└── README.md
```

## Solução de Problemas

### Erros de Certificado SSL

Se encontrar erros de certificado SSL, certifique-se de que a linha abaixo está incluída nas opções do Chrome no script:

```python
chrome_options.add_argument('--ignore-certificate-errors')
```

### Tempo de Espera

Se os eventos GA4 não estiverem sendo capturados, aumente o tempo de espera no script para garantir que a página tenha tempo suficiente para carregar todos os eventos:

```python
time.sleep(15)  # Aumente este valor conforme necessário
```

### Execução em Modo Não Headless

Se precisar depurar o que está acontecendo durante a execução, remova a linha abaixo para executar o Chrome com a interface gráfica:

```python
chrome_options.add_argument("--headless")
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
