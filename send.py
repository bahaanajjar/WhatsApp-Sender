# coding=utf-8
# -*- coding: <ascii> -*-
# -*- coding: ascii -*-
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: utf-42 -*-

import os
clear = lambda: os.system('cls')
pipselenium = lambda: os.system('pip3 install selenium')
pipselenium()
clear()
pipcolored = lambda: os.system('pip3 install colored')
pipcolored()
clear()
pipcolorama = lambda: os.system('pip3 install colorama')
pipcolorama()
pipgetmac = lambda: os.system('pip3 install getmac')
pipgetmac()
clear()
pipcolored = lambda: os.system('pip3 install python-telegram-botd')
pipcolored()
clear()
import time
clear()
import selenium
clear()
from selenium import webdriver
clear()
from getmac import get_mac_address as gma
clear()
from termcolor import colored
clear()
from time import sleep
clear()
import random
clear()
import colorama
import string
clear()

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from colorama import init, Fore, Back, Style
from termcolor import colored
from colorama import init,Fore
from time import sleep
import threading
import string,random
from bs4 import BeautifulSoup
import json
import requests

import warnings
warnings.filterwarnings("ignore")


options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
#options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--silent")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
#driver.set_window_position(-10000,0)

bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE


def banner():
    print(f'''
                            {red} Whatsapp Send SMS {res}
                            {yl}https://github.com/bahaanajjar{res}
''')


driver.get('https://web.whatsapp.com/')

banner()

print (f"{gr}login on your Whatsapp and press Enter  . . . {res}")
input(f"{yl}press Enter .. {res}\n")

urlFile = open("message.txt",'r',encoding = 'utf-8')
url =urlFile.read()

i=0

with open('number.txt', 'r') as use:
    num = use.read().splitlines()
   
for f in num:
    i+=1
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={f}&text={url}&app_absent=1")
        sleep(5) 
        element = lambda d : d.find_elements(by=By.XPATH, value="//div//button/span[@data-icon='send']")
        sleep(1) 
        print(f"[{i}]{yl} sent sms to {f}  ==> {gr}[Successful]{res}")
        sleep(1)
    except:
        print(f" [{i}]{yl} sent sms to {f}  ==> {red}[Failed]{res}")
        pass    
        
         

