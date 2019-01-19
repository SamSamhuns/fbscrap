from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

USER = #USEREMAIL
PASS = #PASSWORD
debug_msg_status = 0           # For printing debug messages

def login():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get('https://mbasic.facebook.com/')
    if debug_msg_status:
        print ("Opened facebook")
    sleep(1)


    username_box = driver.find_element_by_id('m_login_email')
    username_box.send_keys(USER)
    if debug_msg_status:
        print ("Email Id entered")
    sleep(1)

    password_box = driver.find_element_by_name('pass')
    password_box.send_keys(PASS)
    if debug_msg_status:
        print ("Password entered")

    login_box = driver.find_element_by_name('login')
    login_box.click()

    # Check for login with one tap page
    body = driver.find_element_by_tag_name('body')

    if (body.text.find("Log In With One Tap") != -1 and body.text.find(
        "Next time you log in on this device, just tap your account instead of typing a password.") != -1):
        OK_btn = driver.find_element_by_xpath("//input[@value='OK' and @type='submit']")
        OK_btn.click()

    chat_btn = driver.find_element_by_xpath("//div[@role='banner']/div[@role='navigation']/a[@accesskey='6']")
    chat_btn.click()

    print("Input Anything to quit")
    x = input()
    driver.quit()

def main():
    login()

if __name__ == "__main__":
    main()
