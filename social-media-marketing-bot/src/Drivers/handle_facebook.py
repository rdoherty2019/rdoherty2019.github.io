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