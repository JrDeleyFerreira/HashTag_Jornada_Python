import pyautogui
import time
import csv

from pathlib import Path

# Tempo padrão de intervalo de cada passo
pyautogui.PAUSE = 0.5

pyautogui.press('win') # Pressiona a tecla do windows
pyautogui.write('edge') # Busca pelo navegador
pyautogui.press('enter') # Pressiona ENTER ao encontrar o navegador

pyautogui.click(x=433, y=65)
# Link do "Site"
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3) # Tempo para aguardar abrir o site

pyautogui.click(x=721, y=450) # Clica na caixa de Login
pyautogui.hotkey('ctrl', 'a') # Seleciona tudo caso o campo esteja com auto-preenchimento
pyautogui.write('junis_developer@gmail.com') # escrever o seu email
pyautogui.press('tab') # passando pro próximo campo
pyautogui.write('ssa8770qw')
pyautogui.click(x=961, y=652) # clique no botao de login

time.sleep(3) # Aguarda até o login

CAMINHO_CSV = Path(__file__).parent / 'produtos.csv'

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    tabela_prd = csv.DictReader(arquivo)
    
    for prod in tabela_prd:
        pyautogui.click(x=654, y=301) # Posiciona na 1ª caixa de texto 
        
        for chave, valor in prod.items():
            if chave == 'obs' and (valor is None or valor == ''):
                pyautogui.write(str('Sem observações.'))
                
            pyautogui.write(str(valor)) # preencher o campo
            pyautogui.press("tab") # passar para o proximo campo
        
        pyautogui.press("enter") # cadastra o produto (botao enviar)
        time.sleep(2)
        pyautogui.scroll(5000) # dar scroll de tudo pra cima
