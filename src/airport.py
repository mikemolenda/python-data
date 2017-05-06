lhr =[]

with open('../data/text/heathrowdata.txt', newline='') as lhr_input:
    for row in lhr_input:
        lhr.append(row.strip().replace('Provisional', '').strip('#'))

for line in lhr[7:]:
    print(line)

    year = line[:4]
    print(year)

    month = line[5:8].strip()
    print(month)

    tmax = line[9:15].strip()
    print(tmax)

    tmin = line[16:23].strip()
    print(tmin)