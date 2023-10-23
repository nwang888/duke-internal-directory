# this is a template for the config.py file
# replace the empty strings with the appropriate values
# and rename the file to config.py

import os

os.environ['DATA_PATH'] = '' #ex: '/Users/nwang888/'
os.environ['YEARS'] = '' #ex: '2024 Fall' or '2025 Sprng,2024 Fall']
os.environ['PROGRAMS'] = '' #ex: 'E-UGD' or 'E-UGD,A&S,KUGD'

# P.S. If you do not require filtering by year, it may be faster to run a script based on the Duke OIT streamer API directly.