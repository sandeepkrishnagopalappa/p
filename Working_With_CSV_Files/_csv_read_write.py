import csv

# Reading CSV Files
with open('babynames.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)     # Prints each line of csv file.

with open('babynames.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line[0], line[1])     # Prints only first and second column.

with open('babynames.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['year'], line['sex'])


# Writing to CSV Files
with open('new_baby_names.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['name', 'age', 'sex'])
    
with open('babynames.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('test.csv', 'w', newline='') as csv_write:
        csv_writer = csv.DictWriter(csv_write, fieldnames=["year","name","percent","sex"])
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
