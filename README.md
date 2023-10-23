# NetID-Verification

A quick script that is able to verify any one field given from the duke internal directory against the rest of the fields.

## Getting Started

Usage via cli:

Usage via Google Colab and Google Sheets:

## Other Notes

If you do not require filtering by year, it may be faster to run a script based on the [Duke OIT streamer API](https://streamer.oit.duke.edu/dev_console) directly. This script instead queries the internal directory specifically, because the streamer API does not contain graduation term.

Additionally, the authentication for usage of the internal directory API relies on connection to the DukeBlue network. If you are not connected to the DukeBlue network, you will need to use a VPN to connect to the DukeBlue network.
