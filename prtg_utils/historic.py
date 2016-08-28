#!/usr/bin/env python


from __future__ import print_function
import csv
import sys
import argparse
from utils import Prtg


raw = True
parser = argparse.ArgumentParser(description='Query prtg historic data')
parser.add_argument("--ids", required=True )
parser.add_argument("--starttime", required=True)
parser.add_argument("--endtime", required=True)
parser.add_argument("--average", type=int, default=3600)
parser.add_argument("--host")
parser.add_argument("--user")
parser.add_argument("--password")
parser.add_argument("--output", required=True)
parser.add_argument("--locale",  default='us', help='[us|euro]')
parser.add_argument('--raw', dest='raw', action='store_true')
args = parser.parse_args()
ids = args.ids.split(",")   
if not (args.locale == 'us' or args.locale == 'euro'):
    print("ERROR: Invalid locale: "+ args.locale + "\n", file=sys.stderr)
    sys.exit(-1)




def generate_csv(ids, data, raw, average, locale, output): 

    if locale == 'us': 
        csv.register_dialect('csv_output', delimiter=',')
    elif locale == 'euro':
        csv.register_dialect('csv_output', delimiter=';')

    def format_locale(value): 
        if locale == 'us': 
            return  value.replace(",",".")
        elif locale == 'euro': 
            return  value.replace(".",",")

    
    with open(output, 'wb') as f:
        writer = csv.writer(f, dialect='csv_output')
        row1 = [ "Name" ]
        row2 = [ "Parent Group" ]
        row3 = [ "Parent Device" ]
        row4 = [ "Start of Period " ]
        for id in ids:
            for i in range(2): 
                details = prtg.get_sendor_detail(id)
                row1.append(details['sensordata']['name'])
                row2.append(details['sensordata']['parentgroupname'])
                row3.append(details['sensordata']['parentdevicename'])
            row4.append(id)
            if raw:
                row4.append(str(id) + "(raw)")

        writer.writerow(row1)
        writer.writerow(row2)
        writer.writerow(row3)
        writer.writerow(row4)

        for dateTime in sorted(data):
            row = [ float(dateTime)-float(average)/86400 ]
            #row = [ dateTime ]
            for id in ids:
                v = data[dateTime].get(id)
                if v != None:
                    formatted_value = v.formatted_value
                    formatted_value = formatted_value.rpartition(' ')[0]
                    formatted_value = format_locale(formatted_value)
                    row.append(formatted_value)
                    if raw:
                        value = v.value
                        value = format_locale(value)
                        row.append(value)
                else:
                    row.append("")
            writer.writerow(row)


prtg = Prtg(args.host, args.user, args.password)
data = prtg.get_history_data(ids, args.starttime, args.endtime, args.average)
generate_csv(ids, data, args.raw, args.average, args.locale, args.output)

