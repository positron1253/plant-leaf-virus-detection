from selenium import webdriver
import time
import requests
import bs4
import os
import cv2
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
cService = webdriver.ChromeService(executable_path=r"C:\Users\ASUS\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = cService)


url='https://www.google.com/search?sca_esv=5075b59141659166&sxsrf=ADLYWIJWW5i_HeKR2J5wUExYq7uIpRY-vg:1721029472091&q=potato&udm=2&fbs=AEQNm0DPvcmG_nCbmwtBO9j6YBzM68ZanC7g01Skprhw5JoufVCiMv-hxC44jt6JduRQysBab-bgQXjPraaWFXMvOy8Kr1OAG3K-aj3De4zf3-LxKtkBtWaSCp743evHzhY6J0rIQUCXki65vOxhV0cGJtj0S1dF8YREnKrWtJctBkTv8-bs83YpB7p3IMTdYvjisDEty1xSxeLS4B_TKFXUiCrenmEMcA&sa=X&ved=2ahUKEwiFztOyxqiHAxXHxTgGHXwPAPcQtKgLegQIDBAB&biw=1600&bih=1032&dpr=1'
driver.get(url)

links=[]
for i in range(1,4):
    # str='hello i am {sed} years old'.format(sed=i)
    # print(str)
    image=driver.find_element("xpath",'//*[@id="rso"]/div/div/div[1]/div/div/div[{sed}]'.format(sed=i))
    imagesrc = image.get_attribute('src')
    print(imagesrc)

    image.click()
    time.sleep(2)


    img=driver.find_element("xpath",'//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img[1]')
    imgsrc=img.get_attribute('src')
    links.append(str(imgsrc))
    time.sleep(2)
    # imgsrc=img.get_attribute('src')
    # print(imgsrc)




for url in links:
    # Fetch the image
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Open the image
    image = Image.open(BytesIO(response.content))

    # Display the image using matplotlib
    plt.imshow(image)
    plt.axis('off')  # Hide the axes
    plt.show()
