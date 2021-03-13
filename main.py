from facebook_bot import facebook_bot_cls       # facebook_bot.py
import json     # python 83 tutorialo
import time
if __name__=="__main__":
    with open("config.json") as file:       
        config=json.load(file)
    
    driver=config["driver"]
    username=config["username"]
    password=config["password"]
    media=config['media']

    # facebook_bot_cls(driver,username,password)
    fb=facebook_bot_cls(driver,username,password)
    # time.sleep(5)
    fb.upload(media,'This is posted by my AI.Special thanks to "JOSSEFINE" ')




































    #  "username": "FazleWorld@gmail.com",
    # "password": "fazlerabbi@01",


    
    # "username": "fazlerabbibepza@gmail.com",
    # "password": "mypass2010",