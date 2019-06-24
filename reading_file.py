import sys

if len(sys.argv) < 2:
    raise SystemExit("Usage: reading_file.py <filename>")

filename = sys.argv[1]

account = None
total_amount = 0.0
total_items = 0

with open(filename) as f:
    header = next(f)
    for i, line in enumerate(f):
        line = line.strip()
        fields = line.split(',')
        fields[1] = fields[1].strip('"')
        items_quantity = int(fields[2])
        item_value = float(fields[6])

        if account is None:
            account = fields[1]
        
        total_items += items_quantity
        total_amount += items_quantity * item_value

print("Account name: {}".format(account))
print("Total Items: {}".format(total_items))
print("Total: {:<10.2f}".format(total_amount))
print("Number of lines processed: {:<5}".format(i+1))