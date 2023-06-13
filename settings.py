from configparser import ConfigParser

def get_valid_filename(message, default_filename):
    while True:
        filename = input(message)
        if not filename:
            filename = default_filename
        if filename.endswith('.csv'):
            return filename
        else:
            print("\033[91mInvalid filename! It should end with '.csv'. Please try again.\033[0m")

def add_custom_dbs(dbs):
    print("\033[93mFor custom databases, the file structure should be: starting IP, ending IP, data\033[0m")
    while True:
        new_db = input("\033[96mEnter the name of the new database (type '\033[1mexit\033[0m\033[96m' or '\033[1m0\033[0m\033[96m' to exit): \033[0m")
        if not new_db or new_db.lower() in ['exit', '0']:
            break
        if new_db.endswith('.csv'):
            dbs.append(new_db)
        else:
            new_db += ".csv"
            dbs.append(new_db)
        print("\033[92mAlready chosen databases:\033[0m", ", ".join(dbs))

def mainConfig():
    print("\033[95m==================== Welcome to Configuration Menu ====================\033[0m")
    config = ConfigParser()
    config_file = 'config.ini'

    # Asking for the default output file name
    default_out_file = 'exported.csv'
    outFile = get_valid_filename("\033[96mEnter the new default output file name \033[30m(press Enter to leave it at default): \033[0m",default_out_file)

    # Asking whether to add the default databases
    add_default_dbs = input("\033[96mDo you want to add the existing databases? \033[30m(\033[1mY\033[0m/n): \033[0m").lower() in ['', 'y', 'yes']
    dbs = []
    if add_default_dbs:
        dbs.append('ipCountry.csv')

    # Asking whether to add custom databases
    add_custom = input("\033[96mDo you want to add custom databases? \033[30m(y/\033[1mN\033[0m): \033[0m").lower() in ['y', 'yes']
    if add_custom:
        add_custom_dbs(dbs)

    # Asking for the default input file name
    default_in_file = 'imports.csv'
    inputFile = get_valid_filename("\033[96mEnter the new default input file name \033[30m(press Enter to leave it at default): \033[0m",default_in_file)

    config['SETTINGS'] = {
        'outPutFileName': outFile,
        'dbs': ','.join(dbs),
        'inputFileName': inputFile,
        'hideWarning' : False,
    }

    with open(config_file, 'w') as conf:
        config.write(conf)

    print("\033[92mConfiguration saved successfully! \U0001F4BE\033[0m")

