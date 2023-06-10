"""Bot to post content to social media platforms"""

from time import sleep
import os
import sys
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Drivers')
from gsheets import GSheet

# Social media platforms to target
social_media_accounts = ['facebook']

# Launch the bot
if __name__ == '__main__':
    print(f'Launching Social Media Marketing Bot')
    print(f'Version: "Post Bot"')
    gsheet = GSheet()
    gsheet.buildService()
    sleep(2)
    # Handle each social media account
    for social_media_account in social_media_accounts:
        os.system('clear')
        gsheet.getPostContent(social_media_account=social_media_account)