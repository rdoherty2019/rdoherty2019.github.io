"""Module to route to the correct social media class."""

import sys
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Drivers')
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Secrets')
from handle_facebook import FacebookBot
from my_secrets import max_character_limit
from random import randint

class SocialMedia:
    """Module to handle different social media classes."""
    def __init__(self, social_media_account):
        """Initialize"""
        self.social_media_account = social_media_account

    def setSocialMediaClass(self):
        """Gets the appropriate social media class for the current iteration."""
        if self.social_media_account == 'facebook':
            self.social_media_class = FacebookBot()

    def composeSocialMediaContent(self, image_filename, post_details):
        """Compose the post for social media."""
        self.post_content_image = f'//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Images{image_filename}'
        self.post_content_message = post_details['post_message']
        self.post_content_location = post_details['post_location']

        if len(self.post_content_message + '#RdohertyMarketing') < max_character_limit[self.social_media_account]:
            if 'RocketMovingApp' in post_details['post_hashtags']:
                self.post_content_hashtags = post_details['post_hashtags']
            else:
                probability = randint(0, 4)
                if probability == 1:
                    self.post_content_hashtags = post_details['post_hashtags'] + ', RdohertyMarketingApp'
                else:
                    self.post_content_hashtags = post_details['post_hashtags']
        else:
            self.post_content_hashtags = post_details['post_hashtags']

    def postSocialMediaContent(self):
        """Posts the content to social media."""
        self.social_media_class.postContent(content_image=self.post_content_image,
                                            content_message=self.post_content_message,
                                            content_location=self.post_content_location,
                                            content_hashtags=self.post_content_hashtags)

    def addLocationSocialMediaContent(self):
        self.social_media_class.addPostLocation()