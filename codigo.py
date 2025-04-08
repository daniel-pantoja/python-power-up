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
pyautogui.press("tab")
pyautogui.press("enter")

# digitar o link e entrar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # espera 3 segundos

# fazer login 
pyautogui.click(x=682, y=412)
pyautogui.write("danieljuniorpantojapureza@gmail.com")
# preencher senha 
pyautogui.press("tab")
pyautogui.write("semsenha")
# botão para logar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3) # espera 3 segundos

# importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# cadastrar um produto
for linha in tabela.index: 
  pyautogui.click(x=661, y=294)

  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(codigo)

  pyautogui.press("tab") # passar para o próximo campo
  marca = tabela.loc[linha, "marca"]
  pyautogui.write(marca)  

  pyautogui.press("tab") # passar para o próximo campo
  tipo = tabela.loc[linha, "tipo"]
  pyautogui.write(tipo)

  pyautogui.press("tab") # passar para o próximo campo
  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.write(categoria)

  pyautogui.press("tab") # passar para o próximo campo
  preco_unitario = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.write(preco_unitario)

  pyautogui.press("tab") # passar para o próximo campo
  custo = str(tabela.loc[linha, "custo"])
  pyautogui.write(custo)

  pyautogui.press("tab") # passar para o próximo campo
  obs = str(tabela.loc[linha, "obs"])
  
  if obs != "nan":
    pyautogui.write(obs)

  # passou para o botão de enviar
  pyautogui.press("tab") 
  pyautogui.press("enter")

  # dar scroll de tudo pra cima
  pyautogui.scroll(10000)

# repetir o processo até o fim.