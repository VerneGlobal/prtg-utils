Prtg Utils
=======================


Tools to work with PRTG.


----

Ths ulilities use the PRTG API to access prtg and provide
utilities which are not available easily on PRTG.

--- 

Usage 

prtg_history_csv [-h] --ids IDS --starttime STARTTIME --endtime ENDTIME [--average AVERAGE] [--host HOST] [--user USER] [--password PASSWORD] --output OUTPUT [--locale LOCALE] [--ilocale LOCALE] [--raw]

Query prtg historic data

optional arguments:
  -h, --help              show this help message and exit
  --ids IDS               List of PRTG ids
  --starttime STARTTIME   Start time
  --endtime ENDTIME       End Time
  --average AVERAGE       Average
  --host HOST             PRTG host
  --user USER             PRTG user
  --password PASSWORD     PRTG password
  --output OUTPUT         Output file
  --locale LOCALE         [us|euro]
  --ilocale LOCALE         [us|euro]
  --raw                   Only output raw data

