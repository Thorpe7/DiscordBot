import os
import time
from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
# Load .env variables
load_dotenv()

def hhLogin_cluster(clusterStr):
    """Takes the server name from ArkBot and finds its current status through webscrapping host havoc"""
    # Chrome options for running in heroku
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("disable-dev-shm-usage")
    browser = webdriver.Chrome(options=gChromeOptions,
    executable_path=ChromeDriverManager().install())

    # Create temp server key
    temp_key = 0
    if clusterStr == "cluster": 
        temp_key = 1
    
    # Pull server IDs
    server1 = os.environ.get("VSTAT")
    server2 = os.environ.get("OSTAT")
    server3 = os.environ.get("FSTAT")

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

    # Switch to iframe
    browser.switch_to.frame(browser.find_element_by_id('aspxcontent'))

    # Create endList variable
    endList = []

    # Grab status for each server
    if temp_key == 1:
        time.sleep(5)
        server1Status = browser.find_element_by_id(server1).text
        server2Status = browser.find_element_by_id(server2).text
        server3Status = browser.find_element_by_id(server3).text
        statusList = [server1Status, server2Status, server3Status]

        # Check elements of list
        for i in statusList:
            if i == str('Running'):
                endList.append("Running")
            else:
                endList.append("May require an update")

    # Create parallel list and output string
    serverNames = ["Valguero", "Olympus", "Primal Fear"]
    output_string = ''
    for i in range(0,3,1):
        output_string += serverNames[i] + ": " + endList[i] + ".\n"

    # Quit Browser
    browser.quit()

    # Return server status
    return output_string