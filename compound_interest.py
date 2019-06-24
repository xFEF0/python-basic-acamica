import sys

if len(sys.argv) < 4:
    raise SystemExit("Usage: compound_interest.py <loan_amount> <rate> <time_in_years>")

loan_amount = float(sys.argv[1])
rate = float(sys.argv[2])
time_in_years = int(sys.argv[3])

interest = 0
loan_at_start = loan_amount
loan_at_end = loan_amount

for year in range(time_in_years):
    loan_at_start = loan_at_end
    interest = loan_at_end * (rate / 100)
    loan_at_end += interest

print("If you borrowed at the bank ${:<10.2f}\nyou'd have to pay ${:10.2f}".format(loan_amount, loan_at_end))