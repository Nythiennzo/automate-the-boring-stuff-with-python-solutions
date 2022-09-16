from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://play2048.co/')
print('Waiting for page to load...')

html_element = browser.find_element(By.TAG_NAME, 'html')

keys = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)

print('Playing!')
while True:
    for key in keys:
        html_element.send_keys(key)

    try:
        browser.find_element(By.CLASS_NAME, 'game-over')
        break
    except:
        pass

print('Game Over!')