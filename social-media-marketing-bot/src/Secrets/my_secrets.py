"""Module to manage credentials"""

# Google Sheets
POST_CONTENT_SHEET_ID = '19c0vHwYJ2K1kMjZON0Skf9hwIEcU2cvfkVr9ERER1AE' # Enter the spreadsheet id here

# Facebook Credentials
## Expires in two month, could not get permanent
FACEBOOK_PERMANENT_TOKEN = "EAASPtBUrKlYBANGzXWfZBRrvkAgW9x1G1jkCwhtS4cffCxhWZAAqZCYZCjLEtlEKZAOZAwOSp6HNTRyuagC13YtKZBJE9a7PmR1USwmUJLZBHhUKLeyrMgATlH3Td9KcGBpfJpGj1QfN5tYwyUaZAwqfaYe34YVfrMUHpYAbUcGiW9bKSZB8vKrb1a2NxS4Pq8LyoZD"
FACEBOOK_ACCOUNT_ID="7005842726098566"
FACEBOOK_SHORT_LIVED_TOKEN=''EAASPtBUrKlYBABk3LXFG0qJG6CSuP43YsZBAuQj82LMrKETlMJLkOV1LSw8cxKAbkcTrppWz1sVy1XUQfwXRZAeQuqsHo1OlccTjZBoJA0BC3aakWKL0nqlNhnDueyS4M2Tb1K5SNCZBEIPOJxiKJ8p2Rw1tZBV2oHyXfqkRQjdUZA4jNp4ZCLutgg2ZC8anSoNqTPle9ZA0I1KZBs933eOEXg0nJQmfqo8PtBYeE6bwAxRQNDoQ0YFznNRUxaWhSBDMQZD"
FACEBOOK_ACCESS_TOKEN="EAASPtBUrKlYBANGzXWfZBRrvkAgW9x1G1jkCwhtS4cffCxhWZAAqZCYZCjLEtlEKZAOZAwOSp6HNTRyuagC13YtKZBJE9a7PmR1USwmUJLZBHhUKLeyrMgATlH3Td9KcGBpfJpGj1QfN5tYwyUaZAwqfaYe34YVfrMUHpYAbUcGiW9bKSZB8vKrb1a2NxS4Pq8LyoZD"
FACEBOOK_ACCOUNT_ID="7005842726098566"
FACEBOOK_USERNAME = "richie.rich98@yahoo.com"
FACEBOOK_PASSWORD = "Ruskin630"
FACEBOOK_LOGIN_URL = 'https://www.facebook.com/login/'
FACEBOOK_BUSINESS_PAGE = 'https://www.facebook.com/RDohertyMarketing/'# Enter your Facebook business page url
FACEBOOK_POST_BASE_URL = 'https://www.facebook.com/RDohertyMarketing/' # Enter the base url for a Facebook post. Replace "####" with the data from your url



SOCIAL_MEDIA_COLUMNS = {
    'facebook': 'Main!A2:A',
    'instagram': 'Main!B2:C',
    'twitter': 'Main!C2:D',
    'pinterest': 'Main!D2:E',
    'linkedin': 'Main!E2:F',
    'youtube': 'Main!F2:G',
    'reddit': 'Main!G2:H',
    'snapchat': 'Main!H2:I',
    'tumblr': 'Main!I2:J',
    'quora': 'Main!J2:K',
    'spreely': 'Main!K2:L',
}

# Images
post_size_guide = {
    'facebook': (940, 788),
    'instagram': (1080, 1080),
    'twitter': (1024, 512),
    'pinterest': (735, 1102),
}

# Maximum character limits
max_character_limit = {
    'facebook': 63206,
    'twitter': 280,
    'instagram': 2200,
    'pinterest': 500,
    'linkedin': 700,
}

# Pexels
PEXELS_API_KEY = "54YKWV2bktpIAYGi4hyjTPzBuOT1ZztDhvKoXq7V0Z7n3ZhQdHmljMLl"

# Pixabay
PIXABAY_API_KEY = "37190711-68074fcad0b70a974616cf49e"