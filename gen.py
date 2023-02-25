
def write_credentials_to_file(email, password):
    with open("credentials.txt", "a") as f:
        f.write(f"{email}:{password}\n")

def create_interia():
    print("Creating interia.pl account!")
    print("Waiting for browser to load!")
    driver.get("https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe")
    print("Waiting for website to load!")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'rodo-popup-agree'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[1]/input'))).send_keys(firstname)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(lastname)
    driver.find_element(By.ID, "birthdayDay").send_keys("04")
    driver.find_element(By.CLASS_NAME, 'icon-arrow-right-full').click()
    driver.find_element(By.CLASS_NAME, 'account-select__options__item').click()
    driver.find_element(By.ID, "birthdayYear").send_keys("2000")
    driver.find_element(By.XPATH, "//*[contains(text(), 'Płeć')]").click()
    time.sleep(.3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[4]/ul/li[1]').click()
    time.sleep(.3)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Nazwa konta')]").click()
    time.sleep(.3)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Nazwa konta')]").click()
    time.sleep(.3)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Nazwa konta')]").click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "rePassword").send_keys(password)
    driver.find_element(By.CLASS_NAME, 'checkbox-container').click()
    time.sleep(.6)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(.3)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(.3)
    write_credentials_to_file(email, password)

def finish_interia():
    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    print("Waiting for user to complete interia.pl captcha!")
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/button")))
    get_url = driver.current_url
    while True:
        if get_url != driver.current_url:
            if driver.current_url.find('logowanie') != -1:
                wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
                get_url = driver.current_url
                continue
            break
    while True:
        try:
            driver.find_element(By.CLASS_NAME, 'rodo-popup-agree').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/button[2]").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/button[2]"))).click()
            break
        except:
            pass
        try:
            driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/div/div/div[2]/div/div").click()
            break
        except:
            pass

if __name__ == '__main__':

    import os
    import os.path
    import random
    import string
    import sys
    import time
    import requests,json,os,time,re
    import random 
    from random import choice
    import inquirer
    from pystyle import *
    import colorama
    from colorama import *
    from rich.traceback import install
    from rich.console import Console
    os.system("cls" if os.name == "nt" else "clear"); os.system("title Interia.pl Mail Generator" if os.name == "nt" else "")
    txt = f"""{Fore.MAGENTA}

███╗░░░███╗░█████╗░██╗██╗░░░░░  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██╔████╔██║███████║██║██║░░░░░  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║╚██╔╝██║██╔══██║██║██║░░░░░  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░╚═╝░██║██║░░██║██║███████╗  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                            Created by Inxx
                  """
    print(Center.XCenter(txt))
    print(f'{Fore.GREEN}')
    username = 'unknown'
    wusername = False
    print("Attempting to make an mail account!")
    try:
        import undetected_chromedriver as uc
    except:
        os.system('pip.exe install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org undetected-chromedriver')
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    try:
        open('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')
    except:
        print("brave browser not found..... installing brave")
        os.system('curl https://referrals.brave.com/latest/BraveBrowserSetup.exe --output install_brave.exe')
        os.system('install_brave.exe')
        os.system('taskkill /f /im brave.exe')
        os.remove('install_brave.exe')
    options = uc.ChromeOptions()
    if input('Type ENTER to start! : ') == 'y': wusername = True
    else: username = f"a{''.join(random.sample(string.ascii_lowercase + string.digits, 15))}"
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    firstname = f"A{''.join(random.sample(string.ascii_lowercase, 8))}"
    lastname = f"A{''.join(random.sample(string.ascii_lowercase, 8))}"
    password = f"A{''.join(random.sample(string.ascii_lowercase + string.digits, 15))}&*"
    email = f"{firstname}.{lastname}@interia.pl"
    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    create_interia()
    finish_interia()