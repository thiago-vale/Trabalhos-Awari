from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span'
CONTACT_FIELD = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
PRIMEIRO_CONTATO = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]'
MSG_TYPE = '//*[@id="main"]/footer/div[1]/div[2]/div'
SEND_MSG = '//*[@id="main"]/footer/div[1]/div[3]'


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://web.whatsapp.com/")

def enviar_mensagem(contato, mensagem):
    new_chat = driver.find_element_by_xpath(NEW_CHAT)
    new_chat.click()
    sleep(2)
    contact_field = driver.find_element_by_xpath(CONTACT_FIELD)
    contact_field.click()
    contact_field.send_keys(contato)
    sleep(2)
    primeiro_contato = driver.find_element_by_xpath(PRIMEIRO_CONTATO)
    primeiro_contato.click()
    sleep(2)
    msg_type = driver.find_element_by_xpath(MSG_TYPE)
    msg_type.click()
    msg_type.send_keys(mensagem)
    sleep(2)
    send_msg = driver.find_element_by_xpath(SEND_MSG)
    send_msg.click()
    sleep(1)
  
  
lista_de_contatos = ['Thiago Pessoal']
msg_padrão = 'Olá eu sou o Thiago BOT'
for cont in lista_de_contatos:
    enviar_mensagem(cont,msg_padrão)