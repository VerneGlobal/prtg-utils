from __future__ import print_function
import requests
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import csv
import json
from collections import defaultdict


class PrtgValue:
    def __init__(self, formatted_value, value,):
        self.formatted_value = formatted_value
        self.value = value


class Prtg:

    def __init__(self, hostname, username, password):
        requests.packages.urllib3.disable_warnings()
        self.hostname = hostname
        self.username = username
        self.password = password
        self.history_data_url = "https://{0}/api/historicdata.csv".format(hostname)
        self.sensor_detail_url = "https://{0}/api/getsensordetails.json".format(hostname)

    def sensor_url(self, id):
        return "https://{0}/sensor.htm?id={1}".format(self.hostname, id)

    def get_history_data(self, ids, start_time, end_time, average_seconds):
        data = defaultdict(lambda: {})
        for id in ids:
            print("Obtaining history for id:" , id)
            params = {'id': id, 
                       'sdate': start_time, 
                       'edate': end_time, 
                       'avg': average_seconds, 
                       'username': self.username,
                       'passhash': self.password }
            r = requests.get(self.history_data_url, params=params, verify=False)
            f = StringIO(r.text)
            reader = csv.reader(f, delimiter=',')
            next(reader, None)
            for row in reader:
                dateTime = row[1]
                value = PrtgValue(row[2], row[3])
                if dateTime != "":
                    data[dateTime][id] = value
        return data

    def get_sendor_detail(self, id):
        params = {'id': id, 
                   'username': self.username,
                   'passhash': self.password }
        r = requests.get(self.sensor_detail_url, params=params, verify=False)
        return json.loads(r.text)

