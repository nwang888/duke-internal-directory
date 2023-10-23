import requests
import csv
from bs4 import BeautifulSoup
import os
import config
import threading

DATA_PATH = os.environ['DATA_PATH']
YEARS = os.environ['YEARS'].split(',')
PROGRAMS = os.environ['PROGRAMS'].split(',')

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

# Function to process a single CSV file
def process_csv_file(csv_file):
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
            print(directory_details)
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

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith('.csv') and not f.endswith('OUT.csv')]
print(csv_files)

# Create a thread for each CSV file and run the operation on each file in a separate thread
threads = []
for csv_file in csv_files:
    thread = threading.Thread(target=process_csv_file, args=(csv_file,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()