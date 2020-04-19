import json

with open('joblinks.json') as infile:
    links = json.load(infile)


for job in links:
    print(links[job])
