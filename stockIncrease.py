# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from mail import sendmail
import time

# initial declaration
stockName = input("What is the stock you are looking for: ")
watchPrice = input("What is your watch price for the stock?")
sender_email1 = input("Bot email: ")
password1 = input("Bot email password: ")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
message1 = """\
Subject: Your Stock has hit your specified price of """ + watchPrice
'''
Finds the Stock
'''
driver.get("https://www.nasdaq.com/market-activity/stocks")
search_bar = driver.find_element(By.CLASS_NAME,"jupiter22-find-symbol__input")
search_bar.send_keys(stockName, Keys.ENTER)
time.sleep(4)
stockPrice = driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span/span[2]")
print("Found the stock price")
initial_stockPrice = stockPrice.get_attribute("innerText")
driver.minimize_window()

# Main code Execution
while True:
    updated_stockPrice = driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span/span[2]")
    updated_stockPrice_text = updated_stockPrice.get_attribute("innerText")

    if updated_stockPrice_text > initial_stockPrice:
        print(
            "The Stock Price of " + stockName + " has increased from " + initial_stockPrice + "to " + updated_stockPrice_text)
        initial_stockPrice = updated_stockPrice_text

    elif updated_stockPrice_text < initial_stockPrice:
        print(
            "The Stock Price of " + stockName + " has decreased from " + initial_stockPrice + "to " + updated_stockPrice_text)

        initial_stockPrice = updated_stockPrice_text

    else:
        print(
            "The Stock Price of " + stockName + " has not changed and the current to price is: " + updated_stockPrice_text)
    # watch price target
    if watchPrice == updated_stockPrice_text:
        print("email sending")
        sendmail(message1, sender_email1, password1)

    time.sleep(10)

