
import csv

# read CSV files


# `open`: he with keyword is used to ensure that the file is properly opened and closed 
#         automatically, even if an error occurs while processing the file.

# open a file called `people` in read mode (`r`)
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)



# csv.DictReader()
# he `csv.DictReader()` class can be used to read the CSV file into a dictionary
# offering a more user-friendly and accessible method.

with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)