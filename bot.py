from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import requests
import os
import time
import sys

chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
service=Service(executable_path='chromedriver.exe')

driver=webdriver.Chrome(service=service,options=chrome_options)

pname = sys.argv[1] #input("Enter the place to get image from ")
#str=input("Enter the image index")
#l=int(str)
l=2
driver.get(f"https://www.google.com/search?q={pname}&udm=2")


time.sleep(2)
path2= "//div//img"
path="//div//h3//a//div//g-img//img"


WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,path)))
images = driver.find_elements(By.XPATH,path)
dest ="images"
if images:
    print("Image found\n")
    img=images[l].get_attribute("src")
    #print(f"img is {img}")
    if img.startswith("data:image"):
        try :
            img_data= img.split(",")[1]
            img_data=base64.b64decode(img_data)
            with open(f"{dest}/{pname}.jpg","wb") as f:
                f.write(img_data)
            print("Downloaded image")
        except Exception as e:
            print(f"Could not download image from {img} .Error :{e}")
    else:
        try:
            img=images[l].get_attribute("src")
            img_data=requests.get(img).content
            with open(f"{dest}/{pname}.jpg","wb") as f:
                f.write(img_data)
            print("Downloaded image")
        except Exception as e:
            print(f"Could not download image from {img} .Error :{e}")
else:
    print("No image url found")
driver.quit()
exit(0)