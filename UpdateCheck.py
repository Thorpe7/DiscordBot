import os
import time
from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
# Load .env variables
load_dotenv()

def hhLogin_update(updateStr):
    """Takes the server name from ArkBot and finds its current status through webscrapping host havoc"""
    # Chrome options for running in heroku
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("disable-dev-shm-usage")
    browser = webdriver.Chrome(options=gChromeOptions,
    executable_path=ChromeDriverManager().install())

    # Load serverIDs
    server1 = os.environ.get("VSV1")
    server2 = os.environ.get("OSV2")
    server3 = os.environ.get("FSV3")
    serverList = [server1, server2, server3]

    # Login information
    username_hh = os.environ.get("HHLOGIN")
    psswd_hh = os.environ.get("HHPWD")

    # Bot to navigate to host havoc url
    # browser = webdriver.Chrome() # Taken out with introduction of chrome options
    browser.get(('https://gamepanel.hosthavoc.com/Login?ReturnUrl=%2f'))

    # Fill in login information
    username = browser.find_element_by_id("UserName")
    username.send_keys(username_hh)
    psswd = browser.find_element_by_id("Password")
    psswd.send_keys(psswd_hh)

    # Sign-in
    signInButton = browser.find_element_by_id('loginButton')
    signInButton.click()

    # Create empty list for update statuses and parallel list for server names
    serverNamesList = ["Valguero", "Olympus", "Primal Fear"]
    updateStatusList = []

    # Search for badges, if no badges return no updates, if badges return updates requried
    # Click on server, search for updates, store if updates present, go back and check remaining servers
    for i in range(0,3,1):
        updateStatus = "No pending updates found"
        browser.switch_to.frame(browser.find_element_by_id('aspxcontent'))
        serverLink = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID,serverList[i])))
        serverLink.click()
        if updateStr == 'update':
            try:
                updateStatus = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'workshop-badge'))).text
            except TimeoutException as ex:
                updateStatus = updateStatus
                pass
        updateStatusList.append(updateStatus)
        browser.back()

    # Quit browser
    browser.quit()

    # Format the updatesList elements
    for i, e in enumerate(updateStatusList):
        if e != 'No pending updates found':
            updateStatusList[i] = 'Update(s) required.'
    
    # Formate the outputString
    outputString = ""
    for i, e in enumerate(serverNamesList):
        outputString += serverNamesList[i] + ": " + updateStatusList[i] + "\n"

    # Return server status
    return outputString
