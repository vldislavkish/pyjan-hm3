import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get('https://www.saucedemo.com/')

try:
    browser.find_element(By.CSS_SELECTOR, '[name="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, "//input[@name='password']").send_keys('secret_sauce')
    time.sleep(1)
    browser.find_element(By.XPATH, "//input[@name='login-button']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//div[contains(text(), 'Fleece')]/../../..//button").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//input[@name="firstName"]').send_keys('qwerty')
    browser.find_element(By.XPATH, '//input[@name="lastName"]').send_keys('asdfg')
    browser.find_element(By.XPATH, '//input[@name="postalCode"]').send_keys('1234')
    time.sleep(1)
    browser.find_element(By.XPATH, '//input[@name="continue"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//button[@name="finish"]').click()
    time.sleep(3)
finally:
    browser.quit()
