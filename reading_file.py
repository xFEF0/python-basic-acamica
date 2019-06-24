import sys
import csv

if len(sys.argv) < 2:
    raise SystemExit("Usage: reading_file.py <filename>")

filename = sys.argv[1]

account = None
total_amount = 0.0
total_items = 0

with open(filename) as f:
    rows = csv.reader(f)
    header = next(f)
    for i, row in enumerate(rows):
        item_quantity = int(row[2])
        item_value = float(row[6])

        if account is None:
            account = row[1]
        
        total_items += item_quantity
        total_amount += item_quantity * item_value

print("Account name: {}".format(account))
print("Total Items: {}".format(total_items))
print("Total: {:<10.2f}".format(total_amount))
print("Number of lines processed: {:<5}".format(i+1))