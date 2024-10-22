import pyautogui
from botcity.core import DesktopBot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
from botcity.maestro import BotMaestroSDK

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")

    chrome_driver_path = 'C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\BOTS\\EPAusuario\\chromedriver-win64\\chromedriver.exe'  # Substitua com o caminho real

    # Atualize para a forma correta de inicializar o webdriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    driver.get("https://funev.sysepa.com.br/epa/login.php")

    bot = DesktopBot()

    # Lógica para automação
    nome_usuario = "testing00"
    data_nascimento = "17/09/1990"
    cargo = "farmace"
    unidade = "pslmb"

    nomes = nome_usuario.split()
    primeiro_nome = nomes[0].upper()
    ultimo_nome = nomes[-1].upper()
    unidade_selecionada = unidade.upper()
    usuarioEpa = f"{primeiro_nome}.{ultimo_nome}.{unidade_selecionada}"

    loginUser = driver.find_element(By.ID, "cbousuario")
    loginUser.clear()
    loginUser.send_keys('GABRIELOLIVEIRA.FUNEV')

    passUSer = driver.find_element(By.ID, "txtsenha")
    passUSer.clear()
    passUSer.send_keys('FUNEV@123')

    print("Logado")

    button = driver.find_element(By.CSS_SELECTOR, ".pull-right.btn.btn-langer.btn-success")
    button.click()

    bot.wait(10000)

    pyautogui.click(pyautogui.locateCenterOnScreen('img\\confi.png', confidence=0.8), duration=1)
    bot.mouse_move(871, 235)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\funcionario.png', confidence=0.8), duration=1)

    print("Entrou no campo de criação de usuário")

    bot.wait(5000)

    if not bot.find_text("name", threshold=230, waiting_time=10000):
        not_found("name")
    bot.click_relative(11, 45)
    bot.type_keys(nome_usuario)

    if not bot.find_text("date", threshold=230, waiting_time=10000):
        not_found("date")
    bot.double_click_relative(44, 46)
    bot.type_keys(data_nascimento)

    if not bot.find_text("cargo", threshold=230, waiting_time=10000):
        not_found("cargo")
    bot.click_relative(45, 41)
    bot.type_keys(cargo) 
    bot.enter()

    if not bot.find_text("unidade", threshold=230, waiting_time=10000):
        not_found("unidade")
    bot.click_relative(27, 48)
    bot.type_keys(unidade)
    bot.enter()

    bot.scroll_down(5)

    if not bot.find_text("salvar", threshold=230, waiting_time=10000):
        not_found("salvar")
    bot.click()

    bot.wait(5000)
    print("Criado!!")

    pyautogui.click(pyautogui.locateCenterOnScreen('img\\confi.png', confidence=0.8), duration=1)
    bot.mouse_move(829, 265)

    if not bot.find_text("gerenciarUser", threshold=230, waiting_time=10000):
        not_found("gerenciarUser")
    bot.click()

    if not bot.find("+", matching=0.97, waiting_time=10000):
        not_found("+")
    bot.click()

    if not bot.find_text("nomeCriado", threshold=230, waiting_time=10000):
        not_found("nomeCriado")
    bot.click_relative(25, 66)
    bot.type_keys(nome_usuario)
    bot.enter()

    bot.mouse_move(115, 809)
    bot.click()

    if not bot.find_text("next", threshold=230, waiting_time=10000):
        not_found("next")
    bot.click()

    print("Usuário Encontrado e selecionado!")

    bot.wait(5000)

    if not bot.find_text("loginFUNEV", threshold=230, waiting_time=10000):
        not_found("loginFUNEV")
    bot.click_relative(40, 41)
    bot.type_keys(usuarioEpa)

    if not bot.find_text("senhaFUNEV", threshold=230, waiting_time=10000):
        not_found("senhaFUNEV")
    bot.click_relative(14, 46)
    bot.type_keys("funev2024")

    if not bot.find_text("confirmarSenha", threshold=230, waiting_time=10000):
        not_found("confirmarSenha")
    bot.click_relative(13, 34)
    bot.type_keys("funev2024") 

    if not bot.find("dep", matching=0.97, waiting_time=10000):
        not_found("dep")
    bot.click()

    pyautogui.click(pyautogui.locateCenterOnScreen('img\\apoioOperacional.png', confidence=0.8), duration=1)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\image.png', confidence=0.8), duration=1)
    pyautogui.click(x=108, y=846)

    if not bot.find_text("ACA2", threshold=230, waiting_time=10000):
        not_found("ACA2")
    bot.click_relative(53, 46)
    bot.type_keys(unidade) 
    bot.enter()

    if not bot.find_text("checkbox", threshold=230, waiting_time=10000):
        not_found("checkbox")
    bot.click_relative(-19, 7)

    if not bot.find_text("save", threshold=230, waiting_time=10000):
        not_found("save")
    bot.click()

    bot.wait(3000)

    if not bot.find("perfil", matching=0.97, waiting_time=10000):
        not_found("perfil")
    bot.click()

    bot.wait(2000)
    bot.scroll_down(5)

    checkbox = driver.find_element(By.CSS_SELECTOR, f"input[type='checkbox'][name='{pslmbGeral}']")
    checkbox.click()

    bot.wait(2000)

    print("Check selecionado!!")

    mensagem = f"{usuarioEpa} , senha: funev2024"
    print(mensagem)
    pyperclip.copy(mensagem)

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
