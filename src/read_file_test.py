moby = []

with open('../data/text/moby_dick.txt', newline='') as text:
        for line in text:
            moby.append(line.rstrip())  # strip double newlines

# for line in moby:
#     print(line)

# Print only even lines
# Demo that text file read as array of strings
# for line in range(0, len(moby), 2):
#     print(moby[line])

# extract chapter names
for line in moby:
    if line.upper().startswith('CHAPTER'):
        print(line)