### 📞 Extração de Contato Comercial de Páginas do Facebook com Selenium

Este script automatiza o processo de extração de números de telefone comercial a partir de links de páginas do Facebook presentes em uma planilha Excel. Utilizando Selenium, BeautifulSoup e Pandas, ele acessa cada link, tenta localizar o número de contato via XPATH ou, alternativamente, via parsing do HTML.

## 🔧 Funcionalidades

- Leitura de planilha Excel com links de páginas do Facebook.

- Login automático no Facebook usando Selenium.

- Extração de números de telefone utilizando XPATHs fornecidos.

- Parsing alternativo do HTML via BeautifulSoup, caso o número não seja encontrado por XPATH.

- Atualização da planilha com os contatos extraídos.


## 🧰 Requisitos

- Python 3.8+

- Google Chrome instalado

- Chromedriver compatível com a versão do seu navegador

## 📦 Bibliotecas necessárias
<img width="766" height="44" alt="image" src="https://github.com/user-attachments/assets/bedcd98c-e876-4662-a783-3b74cf313f97" />

## 📁 Estrutura Esperada da Planilha

A planilha deve conter ao menos uma coluna chamada "Facebook" com os links das páginas.
Se a coluna "Contato_Comercial" não existir, ela será criada automaticamente.

## 🚀 Como Usar

Configure seu ambiente:

Preencha os seguintes campos no código:

excel_file = 'NOME DA SUA PLANILHA.xlsx'

username = 'LOGIN DO FACEBOOK'

password = 'SENHA DO FACEBOOK'

main_xpath = 'XPATH DA SUA PAGINA'

alternative_xpaths = ['XPATH ALTERNATIVO']

1. Execute o script:
<img width="766" height="44" alt="image" src="https://github.com/user-attachments/assets/da9bcd3c-3ed2-4237-9a2c-7790d50a58fe" />

1.1 Resultado:

A planilha será atualizada com uma nova coluna chamada Contato_Comercial contendo os números extraídos (ou mensagem de erro caso não seja encontrado).

## ⚠️ Atenção

- O Facebook pode bloquear ou limitar acessos automatizados. Use com cautela e respeite os Termos de Uso do Facebook.

- Certifique-se de que o login não exige autenticação em duas etapas.

- O uso de scraping em plataformas como o Facebook pode ser frágil, pois qualquer mudança na estrutura da página pode quebrar o script.

- Este projeto foi criado com redundância proposital para maximizar a taxa de sucesso na extração.

## 📌 Observações Finais

O script está preparado para lidar com páginas que não carregam o número de telefone diretamente via XPATH, utilizando regex e parsing do HTML como fallback.

Ideal para pequenas automações ou uso em bases limitadas.

Revise e ajuste os XPATHs conforme necessário para garantir a precisão da extração.


## ✒️ Autores
- Elnatan A.
   
**Que a força esteja com vocês!** <img width="17" height="17" src="https://img.icons8.com/ios/100/stormtrooper.png" alt="stormtrooper"/>

<img src="https://github.com/ElnatanAlves/scrapping-facebook/assets/156375539/ebf63ac2-ff52-4a61-b0f2-6e7537c8f39c</img" alt="Imagem de teste"/>
<img src="https://github.com/ElnatanAlves/scrapping-facebook/assets/156375539/06225869-c681-477a-a90c-f0ecfb3cb66d</img alt="Imagem Teste2/>


