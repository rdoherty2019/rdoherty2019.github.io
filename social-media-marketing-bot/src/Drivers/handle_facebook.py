"""Module to interact with Facebook."""

import facebook
import json
import os
import pyautogui
import requests
import sys
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Images')
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Secrets')
sys.path.append('/home/machine/projects/social-media-marketing-bot/src/PyAutoGUI')

from my_secrets import FACEBOOK_PERMANENT_TOKEN
from my_secrets import FACEBOOK_PASSWORD
from my_secrets import FACEBOOK_USERNAME
from my_secrets import FACEBOOK_LOGIN_URL
from my_secrets import FACEBOOK_BUSINESS_PAGE
from my_secrets import FACEBOOK_POST_BASE_URL

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class FacebookBot:
    """Class to handle the Facebook API"""
    def __init__(self):
        """Initialize"""
        os.system('clear')
        print('Initializing the Facebook bot')


    def postContent(self, content_image, content_message, content_location, content_hashtags):
        """Adds a post to Facebook."""
        fb = facebook.GraphAPI(FACEBOOK_PERMANENT_TOKEN)
        fb_tags = []
        for hashtag in content_hashtags.split(', '):
            hashtag = '#' + hashtag
            fb_tags.append(hashtag)
        fb_tags_str = ' '.join(fb_tags)
        fb_message = f'{content_message}\n\n{fb_tags_str}'
        self.post_location = content_location
        # Post to Facebook
        fb_response = fb.put_photo(open(content_image, 'rb'), caption=fb_message)
        self.fb_post_id = fb_response['id']
        print(f'Post added to Facebook, ID: {self.fb_post_id}')

    '''def addPostLocation(self):
        """Adds a location to the Facebook post."""
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        self.chrome_path = r'//Users//Mackdig25//chromedriver_mac64//chromedriver'
        self.browser = webdriver.Chrome(self.chrome_path, options=options)
        self.FACEBOOK_USERNAME = FACEBOOK_USERNAME
        self.FACEBOOK_PASSWORD = FACEBOOK_PASSWORD

        # Get the Facebook login page
        self.browser.get(FACEBOOK_LOGIN_URL)
        # Wait for the element:
        while True:
            try:
                username_field = self.browser.find_element_by_name('email')
                password_field = self.browser.find_element_by_name('pass')
                break
            except NoSuchElementException:
                continue

        # Type the username
        for username_char in self.FACEBOOK_USERNAME:
            username_field.send_keys(username_char)
            sleep(0.1)
        # Type the password
        for password_char in self.FACEBOOK_PASSWORD:
            password_field.send_keys(password_char)
            sleep(0.1)
        # Click on the log in button
        log_in_button = self.browser.find_element_by_name('login').click()
        # Wait for dashboard page to load
        while True:
            try:
                dashboard_menu_item = self.browser.find_element_by_class_name('_1vp5')
                print('Successfully logged in to Facebook.')
                sleep(2)
                break
            except NoSuchElementException:
                continue
        facebook_post_url = f'{FACEBOOK_POST_BASE_URL}{self.fb_post_id}/'
        self.browser.get(facebook_post_url)
        # Wait for post to load
        while True:
            try:
                browser_sizes = pyautogui.locateOnScreen(
                    '//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//PyAutoGUI//browser_sizes.png')
                print('Post has loaded')
                sleep(2)
                break
            except:
                continue
        pyautogui.click('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//PyAutoGUI//browser_sizes.png')
        sleep(2)
        # Stops the block button from affect seliunm path
        #pyautogui.click('/home/machine/projects/social-media-marketing-bot/src/PyAutoGUI/block_notification_button.png')
        #sleep(2)
        
        ## Adding a location
        while True:
            try:
                pyautogui.click('/home/machine/projects/social-media-marketing-bot/src/PyAutoGUI/add_location_button.png')
                sleep(2)
                break
            except:
                print('Not found')
                continue
                
        while True:
            try:
                pyautogui.click('/home/machine/projects/social-media-marketing-bot/src/PyAutoGUI/photo_location.png')
                sleep(2)
                pyautogui.typewrite(self.post_location, interval=0.1)
                break
            except:
                print('Not found')
                continue
        sleep(1)
        pyautogui.press('tab')
        save_button = self.browser.find_element_by_id('inlineEditorSave')
        save_button.click()
        print('Location successfully added to post.')
        print('Closing browser.')
        self.browser.close()
        '''