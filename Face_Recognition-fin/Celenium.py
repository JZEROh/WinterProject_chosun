from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES
import base64
import cryptoCode as CD


import json

def login(user_name):
    global driver
    json_file_path="Client.json"

    with open(json_file_path,'r',encoding='utf-8') as file:
        Client=json.load(file)
        # print(json.dumps(Client,indent='\t'))
    
    service=Service(ChromeDriverManager().install())
    service.start()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    
    driver = webdriver.Remote(service.service_url,options=options)

    driver.get('https://clc.chosun.ac.kr/ilos/main/main_form.acl')

    id = Client[user_name]["ID"]
    pw = CD.decrypt(Client[user_name]["PW"],id)

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'utillmenu')))

        elem_btn = driver.find_element(By.CLASS_NAME, 'header_login')
        elem_btn.click() # 버튼 클릭

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'usr_id')))
        elem_id = driver.find_element(By.ID, 'usr_id')
        elem_id.send_keys(id) # id 입력

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'usr_pwd')))
        elem_pw = driver.find_element(By.ID, 'usr_pwd')
        elem_pw.send_keys(pw)

        login_btn = driver.find_element(By.XPATH, '//*[@id="myform"]/div/div/div/fieldset/div[2]/input[3]')
        login_btn.click()

    except:
        pass
    
def Logout():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    driver.quit()