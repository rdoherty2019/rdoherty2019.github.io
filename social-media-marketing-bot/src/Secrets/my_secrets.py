"""Module to manage credentials"""

# Google Sheets
POST_CONTENT_SHEET_ID = '19c0vHwYJ2K1kMjZON0Skf9hwIEcU2cvfkVr9ERER1AE' # Enter the spreadsheet id here

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