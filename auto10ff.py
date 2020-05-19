from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialization
word_count = 0
PATH = '/home/ghostdog/chromedriver/chromedriver'
driver = webdriver.Chrome(PATH)

# Webpage: 10fastfingers
driver.get('https://10fastfingers.com/typing-test/english')
time.sleep(5)

inputfield = driver.find_element_by_id('inputfield')
print('')
print('Start typing:')
for i in range(500):
    highlight = driver.find_element_by_class_name('highlight')
    inputfield.send_keys(f'{highlight.text} ')
    time.sleep(0.1)
    word_count += 1
    if highlight.text == '':
        break
print('')
print(f'Words Typed = {word_count}\n')
print('Finished')
time.sleep(10)

driver.close()



































