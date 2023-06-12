"""Module to handle images."""

import os
import sys
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Drivers')
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Images')
from handle_pexels import Pexels
from handle_pixabay import Pixabay
from my_secrets import post_size_guide
from PIL import Image


class HandleImage:
    """Class for handling images."""
    def __init__(self):
        """Initialize"""
        self.image_size_guide = post_size_guide

    def getImageFromSource(self, image_link):
        """Gets the source of the image."""
        image_id = image_link.split('-')[-1].replace('/', '')
        print(f'Image id {image_id}')
        if 'pexels.com' in image_link:
            image_handler = Pexels()
        elif 'pixabay.com' in image_link:
            image_handler = Pixabay()
        image_handler.getImage(image_id=image_id)
        self.image_filename = image_handler.saveImage()

    def resizeImage(self, social_media_account):
        """Resizes the image for social media."""
        FIT_SIZE = post_size_guide[social_media_account]
        os.chdir('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Images')
        original_image = Image.open(self.image_filename)
        image_width, image_height = original_image.size
        # Check if the image needs to be resized.
        if image_width > FIT_SIZE[0] and image_height > FIT_SIZE[1]:
            # Calculate the new width and height to resize to
            if image_width > image_height:
                new_height = int((FIT_SIZE[1] / image_width) * image_height)
                new_width = FIT_SIZE[0]
            else:
                new_width = int((FIT_SIZE[0] / image_height) * image_width)
                new_height = FIT_SIZE[1]
            # Resize the image
            print(f'Resizing {self.image_filename} from {image_width} x {image_height} to {new_width} x {new_height}')
            resized_image = original_image.resize((new_width, new_height))
            resized_image.save(self.image_filename)