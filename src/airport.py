from collections import defaultdict

lhr = []

with open('../data/text/heathrowdata.txt', newline='') as text:
    for line in text:
        lhr.append(line.rstrip())

# Extract weather values for each month and year
weather = defaultdict(dict)

for line in lhr[7:]:
    year = line[:7].strip()

    month = line[8:11].strip()

    tmax = line[12:18].strip()

    tmin = line[19:26].strip()

    af = line[27:34].strip()
    af = af if af != '---' else None

    rain = line[35:42].strip()

    sun = line[43:50].strip()
    sun = sun if sun != '---' else None

    weather[year][month] = {'tmax': tmax, 'tmin': tmin, 'af': af, 'rain': rain, 'sun': sun}

# Print weather data for March 2017
weather_data = weather['1984']['6']

print('Heathrow Airport Weather Data for June 1984')
print()
print('{0:10} {1:>5} °C'.format('High Temp:', weather_data['tmax']))
print('{0:10} {1:>5} °C'.format('Low Temp:', weather_data['tmin']))
print('{0:10} {1:>5} mm'.format('Rainfall:', weather_data['rain']))
print('{0:10} {1:>5} days'.format('Air Frost:', weather_data['af']))
print('{0:10} {1:>5} hours'.format('Sunlight:', weather_data['sun']))

