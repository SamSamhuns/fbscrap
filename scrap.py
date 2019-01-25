#!/usr/bin/env python3
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if len(sys.argv) != 3:
    print("Usage ./scrap.py <headless_state_1_0> <interval_in_secs>")
    sys.exit(1)

USER = "user@email.com"  # USEREMAIL
PASS = "password"       # PASSWORD
HEADLESS = int(sys.argv[1])
INTERVAL = int(sys.argv[2])

CHROMEDRIVER_PATH = './chromedriver'
WINDOW_SIZE = "1920,1080"

# Make sure the paths for the chromedriver and chrome is correct
if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    CHROME_PATH = '/usr/bin/google-chrome'
elif sys.platform == "darwin":
    # OSX
    CHROME_PATH = ('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
elif sys.platform == "win32":
    # Windows
    CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


chrome_options = Options()
if HEADLESS:
    chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=chrome_options)


def login():
    driver.get('https://mbasic.facebook.com/')
    time.sleep(1.0)

    username_box = driver.find_element_by_id('m_login_email')
    username_box.send_keys(USER)
    time.sleep(0.8)

    password_box = driver.find_element_by_name('pass')
    password_box.send_keys(PASS)

    login_box = driver.find_element_by_name('login')
    login_box.click()
    time.sleep(0.5)

    body = driver.find_element_by_tag_name('body')

    # Check for login page with one tap login prompt
    if (body.text.find("Log In With One Tap") != -1 and body.text.find(
            "Next time you log in on this device, just tap your account instead of typing a password.") != -1):
        # Click the Ok OK_btn
        OK_btn = driver.find_element_by_xpath(
            "//input[@value='OK' and @type='submit']")
        OK_btn.click()


def goto_chat_page():
    """ Changes the current window to the Chat page
    """
    chat_btn = driver.find_element_by_xpath(
        "//div[@role='banner']/div[@role='navigation']/a[@accesskey='6']")
    chat_btn.click()


def parse():
    # Set the reload to a constant loop
    while True:
        goto_chat_page()
        time.sleep(INTERVAL)

        status_containers = driver.find_elements_by_xpath(
            "//table[@role='presentation']")

        current_time = time.time()
        current_active_set = set()
        # making sure element not found erros are ignored
        # any errors will be logged in the error_log file
        with open('error_log', 'a') as elog:
            try:
                for item in status_containers:
                    name = (item.find_element_by_xpath(".//tbody/tr/td[1]/a")).text
                    if name != '' and name != "Active Status":
                        current_active_set.add(name)
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                elog.write((message+'\n'))

        # Writing to the active_friend_list file
        output_file = "active_friend_list.txt"
        with open(output_file, 'a') as fw:
            for friend in current_active_set:
                fw.write(friend+','+str(current_time)+'\n')


def main():
    login()
    parse()
    driver.quit()


if __name__ == "__main__":
    main()
