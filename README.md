# NetID-Verification

A quick script that is able to verify the netid against the rest of the fields in the duke internal directory.

For example, if you wanted to validate that a netid is a valid Duke student who is in an Engineering Program with the graduating term of 2025 Spring, you can use this script to do so.

## Getting Started

Create a data folder that contains the csvs that you want to process. As of now, each csv must contain a column named "netid" that contains the netids that you want to verify. You will need to specify the path to this folder in config.py (preferably, this folder should exist in this project directory)

Make sure your data has the correct format! Most importantly, there should be a column called NetID that contains the netids that you want to verify.

Usage via cli:
Navigate to the directory in which this project exists.
Make sure to set config.py to your specified values. The parameters are dictated in the comments of the file.
Then run the following command:

```
./ping.py
```

The results will be stored in the data folder that you specified in config.py.

You can also directly run the script with the parameters:

```
python ping.py --DATA_PATH /path/to/data/ --YEARS 2025 Sprng,2024 Fall --PROGRAMS E-UGD,A&S
```

Usage via Google Colab and Google Sheets:
This will hopefully be supported in the future. It is not functional right now.

## Config

Current Options for Config:
DATA_PATH: The directory of the data folder that contains the csvs that you want to process.
YEARS: i.e. '2025 Fall','2025 Spring' etc... Please use the format 'YYYY Term' for each eyar that you want to filter by. If you do not want to filter by year, set this to an empty list. Make sure to leave no spaces between the commas.
PROGRAMS: i.e. 'E-UGD', 'A&S' etc... Please use the full name of the program as it appears in the directory. If you do not want to filter by program, set this to an empty list. (Note. Starting with Class of 2027 they begin using A&SU for Arts and Sciences Undeclared)

## Other Notes

If you do not require filtering by year, it may be faster to run a script based on the [Duke OIT streamer API](https://streamer.oit.duke.edu/dev_console) directly. This script instead queries the internal directory specifically, because the streamer API does not contain graduation term.

Additionally, the authentication for usage of the internal directory API relies on connection to the DukeBlue network. If you are not connected to the DukeBlue network, you will need to use a VPN to connect to the DukeBlue network.
