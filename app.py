import csv
import ipCheck


exportCsv = 'exportedCsv.csv'
fields = ['dstIP', 'dstCountry', 'dstCity', 'dstAsn']

with open(exportCsv, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(fields)


ips_list = input(
    "copy the csv file to here then tell me what the name of it: ")

with open(ips_list, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            row_p = row[0].split('.')
            
            ipCheck.ip_check(row_p, row[0], exportCsv)