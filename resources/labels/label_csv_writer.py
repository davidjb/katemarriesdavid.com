#!/usr/bin/env python3
import csv
import sys

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    reader.fieldnames[2] = 'address'
    reader.fieldnames[3] = 'invite-group'
    reader.fieldnames[5] = 'mailed'

    # Get past the first few lines
    next(reader)
    next(reader)
    next(reader)

    writer = csv.DictWriter(sys.stdout, fieldnames=['name', 'address'])
    writer.writeheader()

    for row in reader:
        if row['address'] and row['mailed'] not in ('No', 'Yes'):
            content = row['address'].split('\n')
            writer.writerow({'name': content[0], 'address': '\n'.join(content[1:]).rstrip() } )
