import csv

def generate_csv(prtg, ids, data, raw, average, ilocale, locale, output):

    if locale == 'us': 
        csv.register_dialect('csv_output', delimiter=',')
    elif locale == 'euro':
        csv.register_dialect('csv_output', delimiter=';')

    def format_locale(value): 
        ## thousand seperator
        if ilocale == 'euro':
            value = value.replace(".","")
        ## decimal seperator
        if locale == 'us': 
            return  value.replace(",",".")
        elif locale == 'euro': 
            return  value.replace(".",",")

    
    with open(output, 'w') as f:
        writer = csv.writer(f, dialect='csv_output')
        row1 = [ "Name" ]
        row2 = [ "Parent Group" ]
        row3 = [ "Parent Device" ]
        row4 = [ "Start of Period " ]
        for id in ids:
            details = prtg.get_sendor_detail(id)
            row1.append(details['sensordata']['name'])
            row2.append(details['sensordata']['parentgroupname'])
            row3.append(details['sensordata']['parentdevicename'])
            row4.append(id)
            if raw:
                row1.append(details['sensordata']['name'])
                row2.append(details['sensordata']['parentgroupname'])
                row3.append(details['sensordata']['parentdevicename'])
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
