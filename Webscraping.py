# Chapter 12 Web Scraping
# What is web scraping?

# Project mapIt.py
# Insert address in command line
    # import webbrowser, sys, pyperclip
    # if len(sys.argv) > 1:
    #     address = ' '.join(sys.argv[1:])
    # else:
    #     address = pyperclip.paste()

    # webbrowser.open('http:://www.google.com/maps/place' + address)

# Selenium is actually much easier to manage

# Project OpenWeb.py (Self)
from selenium import webdriver
Browser = webdriver.Chrome()
Browser.get('http://www.google.com/maps/place')

# Open another tab
Browser.execute_script("window.open('about:blank','secondtab');")
Browser.switch_to.window("secondtab")
Browser.get('http://www.wikipedia.org')
