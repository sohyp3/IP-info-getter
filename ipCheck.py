import csv

ipCountry = "ipCountry.csv"
ipCity = "ipCity.csv"
ipAns = "ipAsn.csv"

def ip_check(ip_p,ip,csvExport):
    data = []
    data.append(str(ip))
    print(f"\n{ip}")
    with open(ipCountry, 'r') as db:
        reader = csv.reader(db)

        for read in reader:
            fip = read[0].split(".")
            sip = read[1].split(".")

            if int(ip_p[0]) == int(fip[0]):

                if int(ip_p[1]) >= int(fip[1]) and int(ip_p[1]) <= int(sip[1]):

                    if int(ip_p[2]) >= int(fip[2]) and int(ip_p[2]) <= int(sip[2]):

                        if int(ip_p[3]) >= int(fip[3]) and int(ip_p[3]) <= int(sip[3]):
                            print(f" country = {read[2]}")
                            data.append(read[2])
                            continue


    with open(ipCity, 'r') as db:
        reader = csv.reader(db)

        for read in reader:
            fip = read[0].split(".")
            sip = read[1].split(".")

            if int(ip_p[0]) == int(fip[0]):

                if int(ip_p[1]) >= int(fip[1]) and int(ip_p[1]) <= int(sip[1]):

                    if int(ip_p[2]) >= int(fip[2]) and int(ip_p[2]) <= int(sip[2]):

                        if int(ip_p[3]) >= int(fip[3]) and int(ip_p[3]) <= int(sip[3]):
                            print(f" city = {read[2]} {read[3]} {read[4]} {read[5]} {read[6]}")
                            cData = f"{read[2]} {read[3]} {read[4]} {read[5]} {read[6]}"
                            data.append(str(cData))
                            continue


    with open(ipAns, 'r') as db:
        reader = csv.reader(db)

        for read in reader:
            fip = read[0].split(".")
            sip = read[1].split(".")

            if int(ip_p[0]) == int(fip[0]):

                if int(ip_p[1]) >= int(fip[1]) and int(ip_p[1]) <= int(sip[1]):

                    if int(ip_p[2]) >= int(fip[2]) and int(ip_p[2]) <= int(sip[2]):

                        if int(ip_p[3]) >= int(fip[3]) and int(ip_p[3]) <= int(sip[3]):
                            print(f" asn = {read[2]} {read[3]}")
                            cData = f"{read[2]} {read[3]}"
                            data.append(cData)
                            continue

    with open(csvExport,'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)