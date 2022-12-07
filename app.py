from configparser import ConfigParser
import csv

config = ConfigParser()
config.read('cofig.ini')

def checker():
    data = config['SETTINGS']
    dbs = list(data['dbs'].split("}"))

    dataToInsert = []


    exitChoice = input(f'This program will overwrite the data in `{data["outputfilename"]}` if exists!\nBe Careful and backup the data there\nPress Enter to continue, "E" to exit.  ')
    if exitChoice.lower() == 'e':
        quit()

    csv_fields = ['dstIP', 'dstCountry', 'dstCity', 'dstAsn']

    with open(data["outputfilename"], 'w') as file:
        writer = csv.writer(file)
        writer.writerow(csv_fields)


    choice = input('1 For search an ip.\n2 For checking from a csv file\n: ')

    if choice == '1':
        ip = input('enter the ip: ')
        print('\n'+ip)
        dataToInsert.append(ip)
        ipParted = ip.split('.')

        for db in dbs:
            dataToInsert.append(checkIP(ipParted,db, ""))
        
        with open(data['outputfilename'],'a') as file:
            writer = csv.writer(file)
            writer.writerow(dataToInsert)
            

    elif choice == '2':
        dbChoice = input(f"it will look in {data['inputfilename']}, do you want to choose another file y/N:  ")

        if dbChoice =='' or dbChoice.lower() == 'n' or dbChoice.lower()=='no':
            with open(data['inputfilename'],'r') as file:
                reader = csv.reader(file)
                for ip in reader:
                    if ip:
                        print('\n'+ip[0])
                        dataToInsert.append(ip[0])
                        ipParted = ip[0].split('.')

                        for db in dbs:
                            dataToInsert.append(checkIP(ipParted,db, ""))
                
def checkIP(ipParted,fileName,fileType):
    with open(fileName,'r') as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            firstIP = line[0].split(".")
            seconIP = line[1].split(".")

            if int(ipParted[0]) == int(firstIP[0]):
                
                if int(ipParted[1]) >= int(firstIP[1]) and int(ipParted[1]) <= int(seconIP[1]):
                    
                    if int(ipParted[2]) >= int(firstIP[2]) and int(ipParted[2]) <= int(seconIP[2]):

                        if int(ipParted[3]) >= int(firstIP[3]) and int(ipParted[3]) <= int(seconIP[3]):
                            data = ''
                            for i in range(2,len(line)):
                                data +=line[i] +" "
                            print(data)
                            return(data)



checker()