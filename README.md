# fbscrap

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2ddcd031f54240ebbc0497ad8bdcb662)](https://app.codacy.com/app/samhunsadamant/fbscrap?utm_source=github.com&utm_medium=referral&utm_content=SamSamhuns/fbscrap&utm_campaign=Badge_Grade_Dashboard)
[![Updates](https://pyup.io/repos/github/SamSamhuns/fbscrap/shield.svg)](https://pyup.io/repos/github/SamSamhuns/fbscrap/)
[![Python 3](https://pyup.io/repos/github/SamSamhuns/fbscrap/python-3-shield.svg)](https://pyup.io/repos/github/SamSamhuns/fbscrap/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

This project depicts the privacy concerns that exist with social media like facebook and how easy it is monitor your facebook friends. The scripts automatically scrap the online/offline status of your friends. This highlights some of the rising concerns with what can be derived from social media activity such as the wake-sleep cycle as in this case and much more private information.

**Warning**: This project meant to purely show a segment of  social media information that is freely available to be scraped by bots online and should not be used for any malicious purposes. It is a purely educational experiment. The format of facebook pages might also be changing constantly.

This is an alternative approach to using the facebook Graph API. This approach uses Selenium in python. The script opens a new Chromium browser window and mimics the manual process of a user logging into facebook. 

The script does not scrap the online status of friends who are removed from the chat or have not engage with the original user or any of the original user's content for a long time.

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

*   To use the scraper make sure the paths for the chrome binary and chromedirver is correct for all OS. The scraped output file is named as 'active_friend_list.txt'.

`$ ./scrap.py <HEADLESS_flag_1_or_0> <INTERVAL_in_sec>`

Examples: 

`$ ./scrap.py 1 60` would open a chrome tab in a headless state without visuals and probe active friend list every minute.

`$ ./scrap.py 0 300` would open a chrome tab with visuals and probe active friend list every five minutes.
 
*   To run the grapher. (In program options to graph will be available)

`$ ./graph.py`

## Acknowledgements
Inspired by [zzzzz][2] project on GitHub that creates a tracking graph of the sleep patterns of your facebook friends.

[1]: http://chromedriver.chromium.org/downloads
[2]: https://github.com/defaultnamehere/zzzzz
