# IP Lookup Tool
This tool allows you to search for information about an IP address using one or more CSV databases containing IP ranges and their associated data.

## Requirements
Python 3.x

## Installation
* Clone this repository to your local machine.
* Additionally, if you want to use more databases, you can download them from [here](https://www.dropbox.com/sh/b7cud54ym8pkl3t/AACLuhff7u6lIN9F0MFCPciia?dl=0). These databases are taken from [db-ip](https://db-ip.com/db/) and can be used as an alternative to the default databases provided. To use these databases, simply add them to the dbs list in the config.ini file.

## Usage
1. Open a terminal window and navigate to the directory where you cloned the repository.
2. Run the `app.py` file by entering `python app.py` in the terminal.
3. Follow the prompts to search for an IP address or to check a list of IP addresses from a CSV file.

#### Example
```  vbnet
$ python app.py
This program will overwrite the data in `output.csv` if exists!
Be careful and backup the data there.
Press Enter to continue, "E" to exit: 

1 For search an ip.
2 For checking from a csv file
: 1

Enter the IP: 8.8.8.8

8.8.8.8
Google LLC United States Mountain View AS15169 Google LLC 

Data written to output.csv
Press Enter to continue, "E" to exit:
```

## Adding Custom Databases
To add a custom CSV database, simply create a new file in the `dbs` directory and add the IP ranges and their associated data in the following format:

```
startIP,endIP,data1,data2,data3...
```
Note that the `startIP` and `endIP` should be in dotted-decimal notation (e.g. `192.168.0.0`). Once you have created the CSV file, simply add the filename (without the `.csv` extension) to the `dbs` setting in the `config.ini` file, separated by commas if there are multiple files.