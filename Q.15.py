import csv

def read_csv():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv()