#!/usr/bin/env python

import sys
import csv
import json


def lookup(f, sci_name):
    sci_name = sci_name.lower()
    data = []
    with open(f) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['ScientificName'].lower() == sci_name:
                return row


if __name__ == '__main__':
    csv_f = sys.argv[1]
    sci_name = sys.argv[2]
    result = lookup(csv_f, sci_name)
    print json.dumps(result, indent=4, sort_keys=True)
