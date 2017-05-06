import json

infile = open('../data/json/chicago.json')

crimes = json.load(infile)

# Find crimes on Belmont Ave
for row in crimes:
    if row['block'].endswith('BELMONT AVE'):
        print(row['description'])


