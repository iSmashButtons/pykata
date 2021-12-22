# **Change Return Program** - The user enters a cost and then the amount of
# money given. The program will figure out the change and the number of
# quarters, dimes, nickels, pennies needed for the change.

from sys import exit

PROMPT = '$ '

def get_total_amt_due():
    while True:
        print("Enter the total amount due (or q to quit): ")
        try:
            amt_due = input(PROMPT)
            if 'q' in amt_due:
                exit(0)
            amt_due = float(amt_due)
            return amt_due
        except Exception as e:
            print('%s: input must be numeric.' %(e))

def get_cash_received():
    while True:
        print("Enter the cash amount received (or q to quit): ")
        try:
            amt_rec = input(PROMPT)
            if 'q' in amt_rec:
                exit(0)
            amt_rec = float(amt_rec)
            return amt_rec
        except Exception as e:
            print('%s: input must be numeric.' %(e))

def calculate_change_due(total_due, cash_rec):
    return "{:.2f}".format(cash_rec - total_due)

while True:
    amt_due = get_total_amt_due()
    cash = get_cash_received()
    change = calculate_change_due(amt_due, cash)
    print(f"Your change is: ${change}", end='\n\n')