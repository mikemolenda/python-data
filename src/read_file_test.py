moby = []

with open('../data/text/moby_dick_01.txt', newline='') as text:
        for line in text:
            moby.append(line.rstrip())  # strip double newlines

for line in moby:
    print(line)