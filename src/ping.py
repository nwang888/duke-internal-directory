import requests
import csv
from bs4 import BeautifulSoup
import os
import config

PATH = os.environ['CSV_PATH']
YEAR = os.environ['YEAR']

def get_directory(netid):
    url = 'https://directory.duke.edu/directory/search'
    data = {'search': netid}
    response = requests.post(url, data=data, verify=False)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table row containing the result details
    result_detail = soup.find('div', {'class': 'person-data'})
    # print(result_detail)

    # Extract the affiliation
    code_string = result_detail.get_text("\n")
    
    # Split the code string into lines
    lines = code_string.split('\n')

    combined = []
    for i in range(0, len(lines), 2):
        combined.append(lines[i] + lines[i+1])

    # Create a dictionary containing the key-value pairs
    result_dict = {}
    for line in combined:
        if ':' in line:
            key, value = line.split(':', 1)
            result_dict[key.strip()] = value.strip()

    return result_dict

# Read the CSV file and extract the netid column
with open(PATH, 'r') as f:
    reader = csv.DictReader(f)
    netids = [row['netID'] for row in reader]

# add a new column to the CSV file if it doesn't exist
with open(PATH, 'r') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    if 'Graduation Term' not in fieldnames:
        fieldnames.append('Graduation Term')

for netid in netids:
    directory_details = get_directory(netid)
    if directory_details['Graduation Term'] != YEAR:
        print(f'Graduation term does not match for {netid}')
    else:
        print(f'Graduation term matches for {netid}')

# def get_streamer_directory(netid):
#     if not isinstance(netid, str):
#         netid = str(netid)

#     url = 'https://streamer.oit.duke.edu/ldap/people/netid/' + netid +'?access_token=+' + API_KEY
#     response = requests.get(url)

#     if response.status_code != 200:
#         raise Exception('The request did not succeed. Status code: ' + str(response.status_code))
    
#     # Parse the JSON content of the response into a dictionary
#     result_dict = json.loads(response.content)[0]
#     # Create a dictionary containing the extracted information
#     result_dict = {
#         'affiliation': affiliation,
#         'graduation_term': graduation_term,
#         'display_name': result_dict['display_name'],
#         'mail': mail,
#         'netid': netid,
#         'program': program
#     }

#     return result_dict