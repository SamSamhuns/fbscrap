# fbscrap
This project depicts the privacy concerns that exist with social media like facebook and how easy it is monitor your facebook friends. The scripts automatically scrap the online/offline status of your friends. This highlights some of the rising concerns with what can be derived from social media activity such as the wake-sleep cycle as in this case and much more private information.

**Warning**: This project meant to purely show a segment of  social media information that is freely available to be scraped by bots online and should not be used for any malicious purposes. It is a purely educational experiment.

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
## Acknowledgements
Inspired by [zzzzz][2] project on GitHub that creates a tracking graph of the sleep patterns of your facebook friends.

[1]: http://chromedriver.chromium.org/downloads
[2]: https://github.com/defaultnamehere/zzzzz
