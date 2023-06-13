from configparser import ConfigParser
import csv, os ,sys
from configs import mainConfig


config = ConfigParser()
config_path = './config.ini'

if not os.path.exists(config_path):
    mainConfig()

import csv
from configparser import ConfigParser

def check_ip(ip_parted, file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            first_ip = line[0].split(".")
            second_ip = line[1].split(".")

            if int(ip_parted[0]) == int(first_ip[0]) and int(ip_parted[1]) >= int(first_ip[1]) and int(ip_parted[1]) <= int(second_ip[1]) \
                and int(ip_parted[2]) >= int(first_ip[2]) and int(ip_parted[2]) <= int(second_ip[2]) \
                and int(ip_parted[3]) >= int(first_ip[3]) and int(ip_parted[3]) <= int(second_ip[3]):
                
                data = ' '.join(line[2:])
                print(data)
                return data

def checker():
    config = ConfigParser()
    config.read('config.ini')
    
    settings = config['SETTINGS']
    dbs = settings.get('dbs', '').split(',')
    output_filename = settings.get('outputfilename' )
    hide_warning = settings.get('hidewarning')

    if hide_warning == 'False' and os.path.exists(output_filename):
        exit_choice = input(f"This program will overwrite the data in '{output_filename}' if it exists!\n Be careful and backup the data before continuing.\n Press Enter to continue or 'E' to exit or 'H' to exit and never show this again: ")

        if exit_choice.lower() == 'h':
            print('This will never appere again.\n')
            config.set('SETTINGS', 'hidewarning', 'True')

            with open('config.ini', 'w') as config_file:
                config.write(config_file)
            
        if exit_choice.lower() == 'e':
            quit()
    # this is static for the time being, it will be changed soon.
    csv_fields = ['dstIP', 'dstCountry', 'dstCity', 'dstAsn']

    with open(output_filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(csv_fields)

    choice = input("1. Search for an IP.\n2. Check from a CSV file.\n: ")

    if choice == '1':
        ip = input('Enter the IP: ')
        print('\n' + ip)
        data_to_insert = [ip]

        ip_parted = ip.split('.')

        for db in dbs:
            data_to_insert.append(check_ip(ip_parted, f"dbs/{db}"))

        with open(output_filename, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data_to_insert)

    elif choice == '2':
        db_choice = input(f"It will look in '{settings.get('inputfilename', 'importips.csv')}'. "
                            "Do you want to choose another file? (y/N): ")

        if db_choice.lower() in ['y', 'yes']:
            input_filename = input("Enter the input filename: ")
        else:
            input_filename = settings.get('inputfilename')

        with open(input_filename, 'r') as file:
            reader = csv.reader(file)
            for ip in reader:
                if ip:
                    print('\n' + ip[0])
                    data_to_insert = [ip[0]]
                    ip_parted = ip[0].split('.')

                    for db in dbs:
                        data_to_insert.append(check_ip(ip_parted, f"dbs/{db}"))

                    with open(output_filename, 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow(data_to_insert)



checker()
