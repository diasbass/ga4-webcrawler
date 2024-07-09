
# Web Crawler para Identificação de Eventos GA4

Este projeto é um web crawler que utiliza Selenium Wire para navegar até um site específico e identificar eventos GA4.

## Pré-requisitos

- Python 3.12
- Google Chrome
- ChromeDriver

## Instalação

1. Clone o repositório para sua máquina local:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No MacOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração

Certifique-se de que o ChromeDriver está instalado e seu caminho é configurado corretamente no código. O caminho absoluto do ChromeDriver deve ser ajustado no script `webdriver.py`:
```python
CHROME_DRIVER_PATH = 'C:/chromedriver/chromedriver.exe'
```

## Execução

Para executar o web crawler e identificar eventos GA4, use o comando:
```sh
python webdriver.py
```

## Notas Adicionais

- Certifique-se de que o ChromeDriver está atualizado e compatível com a versão do Google Chrome instalada em sua máquina.
- Caso encontre problemas com certificados SSL, a opção `--ignore-certificate-errors` foi adicionada para ignorar esses erros durante a navegação.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
