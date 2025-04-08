import pyautogui
import time

# pyautogui.click --> clicar em algum lugar
# pyautogui.press --> apertar 1 tecla
# pyautogui.write --> escrever um texto
# pyautogui.hotkey --> apertar uma combinação de teclas 

pyautogui.PAUSE = 0.5

# abrir o navegador (FireFox)
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")
# selecionar a primeira conta do navegador
time.sleep(2) # espera 2 segundos
pyautogui.hotkey("tab", "enter")

# digitar o link e entrar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # espera 3 segundos para carregar o site

# fazer login 
pyautogui.click()


# selecionar o campo de email
# escrever email
# preencher senha

# importar a base de produtos pra cadastrar

# cadastrar um produto
# preencher campos

# dar scroll de tudo pra cima

# repetir o processo até o fim.