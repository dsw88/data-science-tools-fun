import glob
import csv
import re

with open('aggregated.txt', 'a') as outfile:

    for file in glob.glob('./yob*.txt'):
        # For each row (minus first)
        # append to new one
        # add year
        regex = re.compile('.*yob(\d{4}).txt')
        match = regex.match(file)
        year = match.group(1)
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row.append(year)
                outfile.write('{}\n'.format(','.join(row)))