import time

import button as button
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox as MessageBox

driver = webdriver.Chrome()

try:
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    time.sleep(7)
    chat = driver.find_element(By.CSS_SELECTOR, "#pane-side > div:nth-child(1) > div > div > div:nth-child(11) > div > div > div._3OvU8 > div._3vPI2 > div.zoWT4 > span > span")
    chat.click()
    text_box = driver.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
    text_box.clear()
    text_box.send_keys("hola esto esta mandado desde python, pero tranquila no voy a automatizar la despedida de buenas noches solo esoty probando a hacer esto, 爱你")
    boton = driver.find_element(By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k > button")
    boton.click()
finally:
    time.sleep(1)
