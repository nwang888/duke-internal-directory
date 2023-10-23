# NetID-Verification

A quick script that is able to verify the netid against the rest of the fields in the duke internal directory.

For example, if you wanted to validate that a netid is a valid Duke student with the graduating term of 2025 Spring, you can use this script to do so.

## Getting Started

Usage via cli:
Navigate to the directory in which this project exists.
Make sure to set config.py to your specified values. The parameters are dictated in the comments of the file.
Then run the following command:

```
./pingmultithread.py
```

Usage via Google Colab and Google Sheets:
This will hopefully be supported in the future. It is not functional right now.

## Other Notes

If you do not require filtering by year, it may be faster to run a script based on the [Duke OIT streamer API](https://streamer.oit.duke.edu/dev_console) directly. This script instead queries the internal directory specifically, because the streamer API does not contain graduation term.

Additionally, the authentication for usage of the internal directory API relies on connection to the DukeBlue network. If you are not connected to the DukeBlue network, you will need to use a VPN to connect to the DukeBlue network.
