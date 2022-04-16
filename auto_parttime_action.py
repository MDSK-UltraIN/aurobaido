from lib2to3.pgen2 import driver
import os
from ssl import Options
from tabnanny import check
from dotenv import load_dotenv
import os
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time


load_dotenv()
dcemail = os.getenv('email')
dcpassword = os.getenv('password') 
dcchannel = os.getenv('dcchannel')

driver_path = './chromedriver.exe'
#brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
#option = webdriver.ChromeOptions
#option.binary_location = brave_path



if __name__ == '__main__':
    

    chrome_options = Options()

    #Healess hrome setting
    '''
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')'''

    #忽略無用的log
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    
    #Show in Chrome when running
    #driver = webdriver.Chrome()
    
    #Running in headless Chrome
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)


    driver.get(dcchannel)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(dcemail)
    driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(dcpassword)
    driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
    sleep(10)

    
    
    try:                
            
        #work
        driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div/span').send_keys('/daily')
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="autocomplete-0"]/div').click()
        #driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div/div/span/span/span').send_keys(Keys.ENTER)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/main/form/div/div/div/div[2]/div/div[2]/div/div/div/span[1]').send_keys(Keys.ENTER) 
        sleep(5)
        #dice 240
        '''
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div').send_keys('/dice amount:240')
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div').send_keys(Keys.SPACE)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div/main/form/div/div/div/div[2]/div/div[3]/div/div').send_keys(Keys.ENTER)
        sleep(2)
        '''
        
        driver.close()

        #waiting & countdown for 1 HR
        
        '''if(i >= 1000):
            print("Working: {0}".format(i), end = "\r")
        elif(i >= 100):
            print("Working: {0} ".format(i), end = "\r")
        else:
            print("Working: {0}  ".format(i), end = "\r")

        time.sleep(1)'''

        #sleeptime = 3630
        #time.sleep(sleeptime)
    except Exception as err:
        print(err)
            
