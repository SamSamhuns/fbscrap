import time
from selenium import webdriver

USER = "user@email.com" #USEREMAIL
PASS = "password"       #PASSWORD
driver = webdriver.Chrome(executable_path='./chromedriver')

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
        time.sleep(5.0)

        status_containers = driver.find_elements_by_xpath(
            "//table[@role='presentation']")

        current_time = time.time()
        current_active_set = set()
        # making sure element not found erros are ignored
        try:
            for item in status_containers:
                name = (item.find_element_by_xpath(".//tbody/tr/td[1]/a")).text
                if name != '' and name != "Active Status":
                    current_active_set.add(name)
        except:
            pass

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
