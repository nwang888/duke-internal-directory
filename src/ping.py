import requests
import csv
from bs4 import BeautifulSoup
import os
import config

DATA_PATH = os.environ['DATA_PATH']
YEARS = os.environ['YEARS'].split(',')
PROGRAMS = os.environ['PROGRAMS'].split(',')

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith('.csv') and not f.endswith('OUT.csv')]

# query the internal directory by netid and returns json
def get_directory_info(netid):
    url = 'https://directory.duke.edu/directory/search'
    data = {'search': netid}
    response = requests.post(url, data=data, verify=False)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table row containing the result details
    result_detail = soup.find('div', {'class': 'person-data'})

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

# for each CSV File
for csv_file in csv_files:
    # Read the CSV file and extract all of the data
    with open(DATA_PATH + csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        # data = [[c.replace('\ufeff', '') for c in row] for row in reader]
        netids = [row['netID'] for row in reader]
        # fieldnames = [fieldname.replace('\ufeff', '') for fieldname in reader.fieldnames]

    # write to a new csv file that contains netid and valid
    with open(DATA_PATH + csv_file[:-4] + 'OUT.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['netID', 'valid'], lineterminator="\n")
        writer.writeheader()

        # go through each netid and check if it exists and graduation term matches the year
        for netid in netids:
            isValid = True
            directory_details = get_directory_info(netid)
            if (directory_details == None or
                'Graduation Term' not in directory_details.keys() or
                directory_details['Graduation Term'] not in YEARS or
                'Program' not in directory_details.keys() or
                directory_details['Program'] not in PROGRAMS):
                isValid = False
            if isValid:
                writer.writerow({'netID': netid, 'valid': 'True'})
            else:
                writer.writerow({'netID': netid, 'valid': 'False'})
        print('done')