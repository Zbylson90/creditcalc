import math
import argparse


def number_of_payments():
    i = (float(args.interest)) / (12 * 100)
    n = math.log((int(args.payment) / (int(args.payment) - i * int(args.principal))), 1 + i)
    n = math.ceil(n)
    n = int(n)
    if n < 12:
        if n == 1:
            print(f"It will take 1 month to repay this loan!")
        else:
            print(f"It will take {n} months to repay this loan!")
    elif n == 12:
        print(f"It will take 1 year to repay this loan!")
    elif 12 < n < 24:
        print(f"It will take 1 year and {n % 12} months to repay this loan!")
    else:
        if n % 12 == 0:
            print(f"It will take {n // 12} years to repay this loan!")
        else:
            print(f"It will take {n // 12} years and {n % 12} months to repay this loan!")
    print(f"Overpayment is {int(args.payment) * n - int(args.principal)}")


def monthly_payment():
    i = (float(args.interest)) / (12 * 100)
    payment_amount = int(args.principal) * ((i * math.pow((1 + i), int(args.periods))) /
                                      (math.pow(1 + i, int(args.periods)) - 1))
    print(f"Your monthly payment = {math.ceil(payment_amount)}!")
    print(f"Overpayment = {math.ceil(payment_amount) * int(args.periods) - int(args.principal)}")


def loan_principle():
    i = (float(args.interest)) / (12 * 100)
    loan = int(args.payment) / ((i * math.pow(1 + i, int(args.periods))) /
                                    (math.pow(1 + i, int(args.periods)) - 1))
    print(f"Your loan principal = {round(loan)}!")
    print(f"Overpayment = {int(args.payment) * int(args.periods) - loan}")


def differ_payments():
    total = 0
    i = (float(args.interest)) / (12 * 100)
    for x in range(1, int(args.periods) + 1):
        monthly_amount = int(args.principal) / int(args.periods) + i * (int(args.principal) - (int(args.principal)
                            * (x - 1)) / int(args.periods))
        monthly_amount = math.ceil(monthly_amount)
        total += monthly_amount
        print(f"Month {x}: payment is {monthly_amount}")
    print(f"Overpayment = {total - int(args.principal)}")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()


if args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
    else:
        differ_payments()
elif args.type == "annuity":
    if args.payment is None:
        monthly_payment()
    elif args.periods is None:
        number_of_payments()
    elif args.principal is None:
        loan_principle()
else:
    print("Incorrect parameters")
