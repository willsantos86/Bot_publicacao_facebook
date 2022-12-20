from tabnanny import check
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1400,1050', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()


# navegar até o site
driver.get('https://www.facebook.com/')
sleep(5)

campo_email = driver.find_element(By.ID, "email")
campo_email.send_keys("xxxxxxxxx")
sleep(3)
campo_senha = driver.find_element(By.ID, "pass")
sleep(1)
campo_senha.send_keys("xxxxxxxxxx")
sleep(3)
campo_login = driver.find_element(By.NAME, "login")
sleep(1)
campo_login.click()
sleep(10)
campo_status = driver.find_element(By.XPATH, "//div[@class='x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe xi81zsa']")
sleep(1)
campo_status.click()
sleep(3)
dentro_campo_status = driver.find_element(By.XPATH, "//div[@class='xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x9f619 x1lliihq x5yr21d xh8yej3 notranslate']")
sleep(1)
dentro_campo_status.click()
sleep(2)
dentro_campo_status.send_keys("Olá! Boa noite à todos!!")
sleep(3)
publicar = driver.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen x1s688f x1x80s81']")
publicar.click()



input('')
driver.close()
