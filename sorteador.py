from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import random


def sorteador(url, number, username, password):

    #define app options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #comment the line bellow if you want the app to run the web service in the screen
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)

    #web application url
    url_1 = "https://instagram.com/"

    #go to url
    driver.get(url_1)
    sleep(3)


    #login structure
    input_username = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_password = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
    button_login = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button')

    #login
    input_username.send_keys(username)
    input_password.send_keys(password)
    button_login.click()
    sleep(5)

    #remove pop-ups
    try:
        button_dont_save = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        sleep(1)
        button_dont_save.click()
        sleep(3)
    except:
        pass
    try:
        button_dont_notify = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        sleep(1)
        button_dont_notify.click()
        sleep(3)
    except:
        pass

    #go to required publication
    driver.get(url)
    sleep(3)

    #check if there are more comments
    while True:
        try:
            driver.find_element('xpath', '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button').is_displayed()
            button_more_comments = driver.find_element('xpath', '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')
            button_more_comments.click()
            sleep(5)
        except:
            break


    #Findo comments and create a list with the users / remove repeated users
    comments = driver.find_elements(By.CLASS_NAME, "_a9zr")
    list_users = []
    list_checked = []
    for comment in comments:
        user_name = comment.find_element(By.CLASS_NAME, "_a9zc").text
        list_users.append(user_name)
    list_users = set(list_users)
    for user in list_users:
        list_checked.append(user)

    #random the winner
    
    list_ch_len = len(list_checked)
    if list_ch_len == 0:
        driver.close()
        info = ["Publicação sem comentários", ""]
    else:
        winners = random.choices(list_checked, k = number)
        info = [list_ch_len, winners]
        #end app
        driver.close()
    return info