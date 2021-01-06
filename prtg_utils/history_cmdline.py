from __future__ import print_function

import sys
import argparse
from prtg_utils.utils import Prtg
from prtg_utils.history import generate_csv


def main(): 
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
    parser.add_argument("--ilocale",  default='us', help='[us|euro]')
    parser.add_argument("--locale",  default='us', help='[us|euro]')
    parser.add_argument('--raw', dest='raw', action='store_true', help='output raw data')
    args = parser.parse_args()
    ids = args.ids.split(",")   
    if not (args.locale == 'us' or args.locale == 'euro'):
        print("ERROR: Invalid locale: "+ args.locale + "\n", file=sys.stderr)
        sys.exit(-1)
    if not (args.ilocale == 'us' or args.ilocale == 'euro'):
        print("ERROR: Invalid ilocale: "+ args.ilocale + "\n", file=sys.stderr)
        sys.exit(-1)


    prtg = Prtg(args.host, args.user, args.password)
    data = prtg.get_history_data(ids, args.starttime, args.endtime, args.average)
    generate_csv(prtg, ids, data, args.raw, args.average, args.ilocale, args.locale, args.output)

