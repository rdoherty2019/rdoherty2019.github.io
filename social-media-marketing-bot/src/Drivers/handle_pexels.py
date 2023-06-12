"""Module to handle Pexels API."""

import json
import os
import requests
import sys
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Secrets')
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Images')
from my_secrets import PEXELS_API_KEY

class Pexels:
    """Class for handling Pexels"""
    def __init__(self):
        """Initialize"""
        self.SINGLE_IMAGE_URL = f'https://api.pexels.com/v1/photos/'
        self.HEADERS = {
            'Authorization': PEXELS_API_KEY,
        }

    def getImage(self, image_id):
        """Calls the Pexels API for the single image"""
        self.image_id = image_id
        single_image_url = self.SINGLE_IMAGE_URL + self.image_id
        r = requests.get(url=single_image_url, headers=self.HEADERS)
        content = r.json()
        self.download_url = content['src']['original']
        print(f'Download the original image from {self.download_url}')

    def saveImage(self):
        """Downloads the original image"""
        original_image = requests.get(self.download_url).content
        os.chdir('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Images//')
        image_filename = f'image-{self.image_id}.jpg'
        with open(f'{image_filename}', 'wb') as image_download:
            image_download.write(original_image)
            image_download.close()
        print(f'Image saved')
        os.chdir('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Bots//')
        return image_filename