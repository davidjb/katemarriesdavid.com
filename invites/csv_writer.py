import itertools
import csv

reader = csv.DictReader(open('wedding2.csv', 'rb'))
reader.fieldnames[3] = 'invite-group'
reader.fieldnames[4] = 'printed'
reader.fieldnames[5] = 'mailed'

data = []
# Get past the first few lines
reader.next()
reader.next()
reader.next()
while True:
    try:
        nxt = reader.next()
    except:
        break
    if nxt['invite-group'] and not nxt['printed'] and nxt['mailed'] != 'No':
        data.append(nxt)

results = itertools.izip_longest(
    (d['invite-group'] for d in data[0::2]),
    (d['invite-group'] for d in data[1::2])
)
print('name1,name2')
for i, j in results:
    print('"%s","%s"' % (i, j))
