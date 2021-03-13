# This code may not work because of changing xpath...Just change the xpath
# Here we only assume that your default audience is "only me" ... If you have othat just handle it .Easy.
# This will automatically post an caption and image called "pk.jped"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # WE can type using it
from selenium.common.exceptions import *        # If our programme give any exception Than it will handle it

from selenium.webdriver.common.by import By


import sys      # To quite our programme

from time import sleep

from selenium.webdriver.support.ui import WebDriverWait             # For waitng until load the page
from selenium.webdriver.support import expected_conditions as EC  # For waitng until load the page

import pyautogui

# Extra....If your run this newer version
from selenium.webdriver.chrome.options import Options


class facebook_bot_cls():
    def __init__(self,driver,userName,passWord) :
        
        # chrome_options_baby=Options()
        # chrome_options_baby.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # self.driver=webdriver.Chrome(driver,options=chrome_options_baby) 


        # self.driver=webdriver.Chrome(driver) 
        # self.driver.get("https://web.facebook.com")

        # from selenium import webdriver
        # from selenium.webdriver.chrome.options import Options

        # This will prevent facebook want's to send you notification *********************************************

        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 1 
        })
        # This will prevent facebook want's to send you notification  End*********************************************


        self.driver = webdriver.Chrome(chrome_options=option, executable_path=driver)
        self.driver.get('https://www.facebook.com')


        self.log_in_Func(userName,passWord)


    def show_exception_Func(self,e):
        print(e)
        self.driver.quit()
        sys.exit()          # Exit the programme


    def log_in_Func(self,userName,passWord):
        
        try:

            email_box=self.driver.find_element_by_id("email")
            email_box.send_keys(userName)          

            pass_box=self.driver.find_element_by_id("pass")
            pass_box.send_keys(passWord)          

            login_btn=self.driver.find_element_by_name("login")
            login_btn.click()
            # login_btn.send_keys(Keys.RETURN)       # press enter

        except Exception as e:
            self.show_exception_Func(e)





    def upload(self,img_path,caption):
        try:
            btn1 = WebDriverWait(self.driver,200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/span/div/i')))
            btn1.click()
            btn2 = WebDriverWait(self.driver,200).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]')))
            btn2.click()
            print(img_path,caption)
            # try:
            cap = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="facebook"]/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div')))
            
                # print(caption)
            cap.send_keys(caption)
            
            sleep(3)
            btn3= WebDriverWait(self.driver,200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="facebook"]/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/span/div/div/div/div')))
            btn3.click()

            sleep(3)
            print(img_path)
            print(type(img_path))
            pyautogui.write(img_path)



            pyautogui.press('enter')
            sleep(5)

            audience_only_me_to_public=pyautogui.locateCenterOnScreen("only_me.PNG")        # only handling "only me" if your default is "Friend or public or other without only me" it will now work...So remember
            pyautogui.click(audience_only_me_to_public)
            sleep(5)
            public_check=pyautogui.locateCenterOnScreen("public_check.PNG")
            pyautogui.click(public_check)
            sleep(6)
            
        

            btn_post = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By
            .XPATH,'//*[@id="facebook"]/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]')))
            print(1)
            btn_post.click()


            print(2)
        except Exception as e:
            print(e)
            print('Something Went Wrong While ')

# facebook_bot.py
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"

# http://127.0.0.1:9222

