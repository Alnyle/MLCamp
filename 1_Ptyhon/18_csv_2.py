
import csv

# open: try to open the file if not exist create one and open it in write (`w`) mode
with open('progtagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["SN", "Movies", "Progagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])
    
    
# using DictWriter in csv

with open('Student.csv', 'w', newline='') as file:
    filednames = ['SSN', 'Name']
    writer = csv.DictWriter(file, fieldnames=filednames)
    
    writer.writeheader()
    writer.writerow({'SSN': 1, 'Name': 'Osman Ali'})
    writer.writerow({'SSN': 2, 'Name': 'Kim mong'})