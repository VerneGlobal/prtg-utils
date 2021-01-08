#!/bin/bash

set -x

IDS='<comma seperated list of ids>'

#Start time format "yyyy-mm minus 1-dd (eom)-23-00-00 e.g. for April 2017 = 2017-03-31-23-00-00"
START_TIME='2017-03-31-23-00-00'

#End time format "yyyy-mm plus 1-01-00-00-00 e.g. for April 2017 = 2017-05-01-00-00-00"
END_TIME='2017-05-01-00-00-00'

#Daily average
#AVG_SECONDS=86400
#Hourly average
AVG_SECONDS=3600

HOST='<host>'
USERNAME='<username>'
PASSWORD='<password>'
OUTPUT='<output>'

set -e
prtg_history_csv --ids "$IDS" --starttime $START_TIME --endtime $END_TIME --average $AVG_SECONDS  --host $HOST  --user $USERNAME --password $PASSWORD --output $OUTPUT --ilocale euro 
