import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import re
import traceback
import numpy as np

def check_file_existence(file_path):
    if os.path.exists(file_path):
        return True
    else:
        print(f"Arquivo {file_path} ADICIONE AQUI SUA PLANILHA")
        return False

def scrape_phone_numbers(url, driver, phone_number_xpath, alternative_xpaths):
    try:
        print(f"Acessando URL: {url}")
        driver.get(url)
        elements = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, phone_number_xpath)))
        phone_numbers = [el.text for el in elements]
        if not phone_numbers:
            for xpath in alternative_xpaths:
                elements = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
                phone_numbers = [el.text for el in elements]
                if phone_numbers:
                    break
        if not phone_numbers:
            phone_numbers = parse_html_for_phone_numbers(driver)
        return phone_numbers
    except TimeoutException:
        print("Elemento não encontrado após espera explícita.")
        return parse_html_for_phone_numbers(driver)
    except Exception as e:
        print("Ocorreu um erro:", e)
        traceback.print_exc()
        return []

def parse_html_for_phone_numbers(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    phone_numbers = soup.find_all(string=re.compile(r'\(\d{2}\)\s*\d{4,5}-\d{4}'))
    return [phone.text.strip() for phone in phone_numbers]

def login_to_facebook(driver, username, password):
    facebook_login_url = 'https://www.facebook.com/'
    driver.get(facebook_login_url)

    email_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    email_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()

excel_file = 'NOME DA SUA PLANILHA.xlsx'
if check_file_existence(excel_file):
    df = pd.read_excel(excel_file)

    df.dropna(subset=['Facebook'], inplace=True)
    df['Facebook'] = df['Facebook'].apply(lambda x: x if isinstance(x, str) and x.startswith('http') else np.nan)
    df.dropna(subset=['Facebook'], inplace=True)

    if 'Contato_Comercial' not in df.columns:
        df.insert(7, 'Contato_Comercial', np.nan)
    df['Contato_Comercial'] = df['Contato_Comercial'].astype(str)  # Converte a coluna para tipo string

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    username = 'LOGIN DO FACEBOOK'
    password = 'SENHA DO FACEBOOK*'

    login_to_facebook(driver, username, password)

    main_xpath = 'XPATH DA SUA PAGINA'
    alternative_xpaths = ['XPATH ALTERNATIVO']

    for index, row in df.iterrows():
        facebook_link = row['Facebook']
        phone_numbers = scrape_phone_numbers(facebook_link, driver, main_xpath, alternative_xpaths)
        contact_number = phone_numbers[0] if phone_numbers else 'Não foi encontrado'
        df.at[index, 'Contato_Comercial'] = contact_number  # Assegura que todos os dados sejam tratados como string

    new_filename = 'NOME DA SUA PLANILHA.xlsx'
    df.to_excel(new_filename, index=False)

    driver.quit()
    print("Processamento concluído com sucesso e arquivo salvo como:", new_filename)
else:
    print("Falha no processamento: arquivo Excel não encontrado.")

    ### OBSERVAÇÕES
    ### LEIA COM ATENÇÃO O CÓDIGO, REVISE E AJUSTE PARA A SUA NECESSIDADE REAL, CÓDIGO CRIADO COM REDUNDANÇAS PARA CAPTURAR DADOS VIA HTML E XPATH CUIDADO!!!!!!!

    ## QUE A FORÇA ESTEJA COM VOCÊ.
