from selenium import webdriver
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')


webd = webdriver.Chrome('/usr/bin/chromedriver')
webd.get('https://www.facebook.com/')

element_user = webd.find_element_by_id("email")
element_user.send_keys(username)

element_pass = webd.find_element_by_id("pass")
element_pass.send_keys(password)

login_b = webd.find_element_by_id("u_0_d")
login_b.submit()

