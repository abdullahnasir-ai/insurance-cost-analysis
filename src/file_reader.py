import csv

with open('/Users/dully/PycharmProjects/insurance-cost-analysis/data/insurance.csv', 'r') as data:
    data_reader = csv.DictReader(data)

    data_list = []
    for line in data_reader:
        data_list.append(line)




