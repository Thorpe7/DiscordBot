import os
import time
from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def hhLogin(serverNameStr):
    """Takes the server name from ArkBot and finds its current status through webscrapping host havoc"""
    # Create temp server key
    temp_key = 0
    if serverNameStr == "valguero": 
        temp_key = 1
    elif serverNameStr == "olympus":
        temp_key = 2
    elif serverNameStr == "fear":
        temp_key = 3

    # Pull server IDs from text document
    serverIDs = open('serverIDs.txt', 'rt')
    id_List =[]
    for i in serverIDs:
        i = i.rstrip()
        # print(i)
        id_List.append(i)
 

    # Login information
    username_hh = os.environ.get("HHLOGIN")
    psswd_hh = os.environ.get("HHPWD")

    # Bot to navigate to host havoc url
    browser = webdriver.Chrome()
    browser.get(('https://gamepanel.hosthavoc.com/Login?ReturnUrl=%2f'))

    # Fill in login information
    username = browser.find_element_by_id("UserName")
    username.send_keys(username_hh)
    psswd = browser.find_element_by_id("Password")
    psswd.send_keys(psswd_hh)

    # Sign-in
    signInButton = browser.find_element_by_id('loginButton')
    signInButton.click()

    # Switch to iframe
    browser.switch_to.frame(browser.find_element_by_id('aspxcontent'))

    # Click on server after explicit wait time
    if temp_key == 1:
        serverLink = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID,id_List[0]
        )))
        serverLink.click()
    elif temp_key == 2:
        serverLink = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID,
        id_List[1])))
        serverLink.click()
    elif temp_key == 3:
        serverLink = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID,
        id_List[2])))
        serverLink.click()

    # Get Server Status
    statusDetails = browser.find_elements_by_id("ServiceInformation")
    detailStr = ''
    for i in statusDetails:
        detailStr = i.text

    # Format elements
    detailElements = detailStr.split('\n')
    # print(detailElements)
    ServerStatus = detailElements[12]
    return ServerStatus


    # Wait after entering server page then
    time.sleep(10)
    browser.quit()



thing = hhLogin('olympus')
print(thing)