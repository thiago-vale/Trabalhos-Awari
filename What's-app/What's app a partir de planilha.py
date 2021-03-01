from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd

NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'
CONTACT_FIELD = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
PRIMEIRO_CONTATO = 'TbtXF'
MSG_BOX = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
SEND_MSG = "_1E0Oz"

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://web.whatsapp.com/")

sleep(10)
def enviar_mensagem(contato, mensagem):
    new_chat = driver.find_element_by_xpath(NEW_CHAT)
    new_chat.click()
    sleep(2)
    contact_field = driver.find_element_by_xpath(CONTACT_FIELD)
    contact_field.click()
    contact_field.send_keys(contato)
    sleep(2)
    primeiro_contato = driver.find_element_by_class_name(PRIMEIRO_CONTATO)
    primeiro_contato.click()
    sleep(3)
    msg_type = driver.find_element_by_xpath(MSG_BOX)
    msg_type.click()
    msg_type.send_keys(mensagem)
    send_msg = driver.find_element_by_class_name(SEND_MSG)
    send_msg.click()
    sleep(1)

planilha = pd.read_excel('C:/Users/Thiago/Desktop/Contatos.xlsx') #Lista de contatos com mensagem 
print(planilha.head())
for cont in planilha['Nome'].unique():
    enviar_mensagem(cont, planilha.loc[planilha['Nome']== cont, 'Mensagem']) #comando para buscar dentro da planilha
