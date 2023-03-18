from configparser import ConfigParser

config = ConfigParser()

# asking for default output file name

while True:
    outFile = input('enter the new default output file name (press enter to leave it at default): ')
    outFileSplit = outFile.split('.')
    if outFile =='':
        outFile = 'exported.csv'
        break
    elif len(outFileSplit) == 2 and outFileSplit[1] == 'csv':
        break
    elif len(outFileSplit) == 1 :
        outFile = outFile+".csv"
        break    
    else:
        print('it should be a csv file, try again!')


# asking for databases to be included in the search, and weather add the default ones

dbs = ''

# the reason i am adding `}` between the database names is to convert the string to list later, i chose a charecter that probably will not be used in a name of a csv file. a file can include a spacebar. 
newdbAdddefaultdb = input('do you want to add the existed dbs Y/n: ')
if newdbAdddefaultdb =='' or newdbAdddefaultdb.lower() == 'y' or newdbAdddefaultdb == 'yes':

    dbs +='ipCountry.csv'

print('for custom databases it sould be a csv file and it should be in this structure \n starting ip, ending ip, the data')
newdbAdd = input('do you want to add custom dbs  y/N: ')
if newdbAdd =='' or newdbAdd.lower() == 'y' or newdbAdd == 'yes':
    while True:
        newdb = input('enter the name of the new databses (type exit or 0 to exit)): ')

        newdbSplit = newdb.split('.')

        if newdb == '0' or newdb == 'exit' or newdb =='':
            break 
        elif len(newdbSplit) == 2 and newdbSplit[1] == 'csv':
            dbs +="}"+newdb
        elif len(newdbSplit) == 1 :
            newdb= newdb+".csv"
            dbs +="}"+newdb



# asking for default output file name 

while True:
    inputFile = input('enter the new default input file name (press enter to leave it at default): ')
    inputFileSplit = inputFile.split('.')
    if inputFile =='':
        inputFile = 'importips.csv'
        break
    elif len(inputFileSplit) == 2 and inputFileSplit[1] == 'csv':
        break
    elif len(inputFileSplit) == 1 :
        inputFile = inputFile+".csv"
        break    
    else:
        print('it should be a csv file, try again!')

config['SETTINGS']={
    'outPutFileName' : outFile,
    'dbs' : dbs,
    'inputFileName':inputFile,

}

with open('cofig.ini','w') as conf:
    config.write(conf)