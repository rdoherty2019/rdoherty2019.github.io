"""Module to interact with Google Sheets."""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

import sys
sys.path.append('//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//secrets')
from my_secrets import POST_CONTENT_SHEET_ID
from my_secrets import SOCIAL_MEDIA_COLUMNS

class GSheet():
    """Class for Google Sheets"""
    def __init__(self):
        """Initialize"""
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.POST_CONTENT_SHEET_ID = POST_CONTENT_SHEET_ID
        self.MAIN_RANGE = "'Main'!A2:S"
        self.SOCIAL_MEDIA_COLUMNS = SOCIAL_MEDIA_COLUMNS

    def buildService(self):
        """Returns a service from Google Sheets."""
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '//Users//Mackdig25//rdoherty2019.github.io//social-media-marketing-bot//src//Secrets//client_secret_desktop.json',
                    self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)
        self.sheet = self.service.spreadsheets()
        print('Building a service to Google Sheets.')

    def getPostContent(self, social_media_account):
        """Extracts the next content to post on social media"""
        sm_range = self.SOCIAL_MEDIA_COLUMNS[social_media_account]
        target_column = self.SOCIAL_MEDIA_COLUMNS[social_media_account][1]
        sm_result = self.sheet.values().get(spreadsheetId=self.POST_CONTENT_SHEET_ID,
                                            range=sm_range).execute()
        sm_values = sm_result.get('values', [])
        if not sm_values:
            print('No data found.')
        else:
            target_row = 0
            for idx, row in enumerate(sm_values):
                try:
                    if row[0] == 'No':
                        target_row = idx + 2
                        print(f'Found content on row # {target_row} to post on {social_media_account.title()}')
                        break
                    else:
                        continue
                except:
                    pass
            # Create the range for the second API call
            target_range_left = sm_range.split(':')[0][:-1]
            target_range_right = 'S'
            target_range = f'{target_range_left}{str(target_row)}:{target_range_right}{str(target_row)}'
            target_result = self.sheet.values().get(spreadsheetId=self.POST_CONTENT_SHEET_ID,
                                                            range=target_range).execute()
            target_values = target_result.get('values', [])
            if not target_values:
                print('No data found.')
            else:
                for row in target_values:
                    try:
                        post_details = {
                            'post_message': row[13],
                            'post_location': row[14],
                            'post_hashtags': row[15],
                            'post_image_link': row[16],
                            'post_character_count': row[17],
                        }
                        print(f'Extracted post details:')
                        print(f'Message text: {post_details["post_message"]}')
                        print(f'Location: {post_details["post_location"]}')
                        print(f'Hashtags: {post_details["post_hashtags"]}')
                        print(f'Image source: {post_details["post_image_link"]}')
                        print(f'Character count: {post_details["post_character_count"]}')
                        self.post_details = post_details
                        break
                    except:
                        pass
