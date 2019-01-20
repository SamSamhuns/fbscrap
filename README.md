# fbscrap
To automatically scrap online/offline status of your friends.

This is an alternative approach to using the facebook Graph API. This approach uses Selenium in python. The script opens a new Chromium browser window and mimics the manual process of a user logging into facebook.

## Build with
`Python3`

## Installation
Selenium requires [ChromeDriver][1]. The ChromeDriver file must be present in the same directory as scrap.py as the path configured in `driver = webdriver.Chrome(executable_path='/PATH/chromedriver')`.

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Usage
Set the `USER` (user email) and `PASS`(password) variables.
```bash
$ python3 scrap.py
```

[1]: http://chromedriver.chromium.org/downloads
