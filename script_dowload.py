import os
import re
from tqdm import tqdm
import requests
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options

# Caminho para o ChromeDriver
# DRIVER_PATH = "./chromedriver/chromedriver-linux64"
DRIVER_PATH = "./chromedriver/chromedriver"

# Configurar o serviço do driver
service = Service(DRIVER_PATH)

# ../../datasets/chagas/insidewood/
 
# Define o diretório onde a imagem será salva
# SAVE_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'Data', 'imagens')
SAVE_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'datasets', 'chagas', 'insidewood')

# Configurar o WebDriver com serviço e opções
def setup_driver(options):
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Navega para a URL fornecida
def open_url(driver, url):
    driver.get(url)
    time.sleep(5)

# Aguarda o carregamento de um elemento e clica nele
def click_element(driver, selector_css):
    try:
        elemento = driver.find_element(By.CSS_SELECTOR, selector_css)
        ActionChains(driver).move_to_element(elemento).click().perform()
        print("Clique realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao clicar no elemento: {e}")

# Localiza e extrai as imagens e seus detalhes da página
def find_elements_grid(driver):
    ids_imagens = []

    # Localizar os elementos do grid
    images = driver.find_elements(By.CLASS_NAME, "image-link")
    for i, image in enumerate(images, start=1):
        image_id = image.get_attribute("id")
        id_img = image_id.split('-')[1]    
        download_href = f"https://iiif-images.lib.ncsu.edu/iiif/2/insidewood-{id_img}/full/full/0/default.tif"
        
        # Localize o elemento pelo XPath e recupere o texto
        species_text = driver.find_element(By.XPATH, f"//*[@id=\"search-container\"]/div[2]/div[{i}]/div[2]/div[1]").text
        family_text = driver.find_element(By.XPATH, f"//*[@id=\"search-container\"]/div[2]/div[{i}]/div[2]/div[2]").text
        
        species_text = re.sub(r"Species:\s*(\w+)\s*(\w+)", r"\1_\2", species_text)
        family = family_text.split(":")[1].strip()  # Divide pela ":" e remove espaços
        
        # Limpeza do texto convertido
        converted_text = re.sub(r'[^a-zA-Z0-9_]', '', species_text)  # Remove caracteres especiais
        specie = converted_text.replace(" ", "_").lower()  # Substitui espaços por "_" e converte para minúsculas
        
        ids_imagens.append((family, specie, id_img, download_href))
        # print(f"Imagem com ID: {image_id} | Specie: {specie} | Family: {family}")
        
    return ids_imagens

# Função para avançar para a próxima página
def next_pages(driver, target=1):
    pagina_atual = 1  # Variável para rastrear a página atual
    
    # Saltar até a {target}ª página
    while pagina_atual < target:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='top-nav']/div/span/button[2]"))
        )
        
        # Clique no botão "Next" para avançar
        next_button.click()
        print(f"Avançando para a página {pagina_atual + 1}...")
        pagina_atual += 1
        
        # Aguarde o carregamento da próxima página
        time.sleep(3)

# Função para realizar o download das imagens
def execute_download(ids_imagens):
    cont = 0
    
    # Use tqdm para mostrar a barra de progresso
    with tqdm(total=len(ids_imagens), desc="Baixando imagens", unit="imagem") as pbar:
        for i, (family, specie, id_img, img_download) in enumerate(ids_imagens):
            # Realiza o download do arquivo
            response = requests.get(img_download)
            
            path_family = os.path.join(SAVE_DIRECTORY, family)
            
            # Garante que o diretório de destino existe
            os.makedirs(path_family, exist_ok=True)
            
            if response.status_code == 200:
                file_name = f"{specie}_{i}_{id_img}.tif"
                file_path = os.path.join(path_family, file_name)
                
                # Salva o arquivo localmente
                with open(file_path, "wb") as f:
                    f.write(response.content)
                cont += 1
            else:
                print(f"Falha ao tentar baixar o arquivo: {img_download}")
            
            # Atualiza a barra de progresso
            pbar.update(1)
    
    print(f"{cont} de {len(ids_imagens)} imagens baixadas com sucesso!") 

# Função principal
def main(target=1, options=any):
    # Inicializa o driver
    driver = setup_driver(options)

    # Abra a página desejada
    URL = "https://insidewood.lib.ncsu.edu/browser/"
    open_url(driver, URL)

    # Clique em um elemento específico ou em coordenadas
    seletor_css = "#app > section > div.search-display > div.facets > div:nth-child(5) > div.body > ul > li:nth-child(1) > a"
    click_element(driver, seletor_css)
    # Aguarde a página carregar com o filtro completamente
    time.sleep(5)
    
    seletor_css = "#app > section > div.search-display > div.facets > div:nth-child(3) > div.body > ul > li:nth-child(3) > a"
    click_element(driver, seletor_css)
    # Aguarde a página carregar com o filtro completamente
    time.sleep(5)

    ids_imagens_completos = []  # Lista para armazenar todas as imagens de todas as páginas
    iteracao = target  # Variável para contar as iterações
    total_imagens = 1204  # Número total de imagens

    try:
        next_pages(driver, target=target)
        
        while True:
            ids_imagens = find_elements_grid(driver)
            ids_imagens_completos.extend(ids_imagens)  # Adiciona as imagens da página atual na lista geral
            iteracao += 1
            
            # A cada 10 iterações, faz o download
            if iteracao % 10 == 0 and iteracao > target:
                print(f"Realizando download após {iteracao} iterações...")
                execute_download(ids_imagens_completos)
                ids_imagens_completos = []  # Limpa a lista após o download
                
                # Calcula a porcentagem de progresso
                progress_percentage = (iteracao / total_imagens) * 100
                progress_bar = '#' * int(progress_percentage // 2)  # Divide a porcentagem por 2 para a barra de progresso
                print(f"Progresso: {progress_percentage:.2f}% | [{progress_bar:<50}]")
                
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='top-nav']/div/span/button[2]"))
            )
            
            if not next_button.is_enabled():
                print("Última página alcançada.")
                break

            # Clique no botão "Next" para avançar
            next_button.click()
            print(f"Avançando para a próxima página... {iteracao}")

            # Aguarde o carregamento da próxima página
            time.sleep(3)

    except NoSuchElementException:
        print("Botão 'Next' não encontrado. Encerrando a navegação.")
    except ElementNotInteractableException:
        print("Botão 'Next' não pode ser clicado. Encerrando a navegação.")

    # Realiza o download das imagens restantes (caso haja)
    if ids_imagens_completos:
        print(f"Realizando download final das imagens restantes...")
        execute_download(ids_imagens_completos, SAVE_DIRECTORY)

    # Feche o navegador após o uso
    time.sleep(5)
    driver.quit()

# Configuração para aceitar o parâmetro `target` pela linha de comando
if __name__ == "__main__":
    if os.path.exists(DRIVER_PATH):
        parser = argparse.ArgumentParser(description="Script para baixar imagens.")
        parser.add_argument('--target', '--t', type=int, default=1, help="Número da página alvo para iniciar.")
        args = parser.parse_args()
        
        # Garante que o diretório de destino existe
        os.makedirs(SAVE_DIRECTORY, exist_ok=True)
        
        # Configurar as opções do Chrome
        options = Options()
        options.add_argument("--headless")  # Modo sem interface gráfica
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")  # Reduz uso de memória compartilhada
        options.add_argument("--remote-debugging-port=9222")  # Evita problemas com DevTools
        options.binary_location = "/usr/bin/google-chrome"  # Substitua se necessário
        
        main(target=args.target, options=options)
    else:     
        print("O diretório inexistente!")
