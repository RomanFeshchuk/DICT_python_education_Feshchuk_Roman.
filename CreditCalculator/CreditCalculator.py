# 4 (The Fourth Stage)
import argparse
from math import ceil, log, trunc


def main():
    print("What do you want to calculate?")
    print("""type 'n' for number of monthly payments,
type 'p' for annuity monthly payment amount,
type 'a' for loan principal:""")
    action = input()
    if action == 'n':
        print("Enter the loan principal:")
        payment = int(input())
        print("Enter the monthly payment:")
        month_payment = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        num = ceil(log(month_payment / (month_payment - i * payment), 1 + i))
        year = trunc(num / 12)

        month = num - year * 12
        if month == 0:
            print(f"It will take {year} years to repay this loan!")
        elif year == 0:
            print(f"It will take {month} to repay this loan!")
        else:
            print(f"it will take {year} years and {month} months to repay this loan!")
    elif action == 'p':
        print("Enter the annuity payment:")
        a_payment = float(input())
        print("Enter the number of period:")
        period = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        loan = trunc(a_payment * ((1 + i) ** period - 1) / (i * (1 + i) ** period))
        print(f"Your loan principal = {loan}!")
    elif action == 'a':
        print("Enter the loan principal:")
        payment = int(input())
        print("Enter the number of period:")
        period = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        month_pay = ceil((payment * i * ((1 + i) ** period) / (((1 + i) ** period) - 1)))
        print(f"Your monthly payment = {month_pay}!")

    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--period", type=int)
    parser.add_argument("--interest", type=float)
    args = parser.parse_args()

    t = args.type
    principal = args.principal
    period = args.period
    interest = args.interest

    if t == "diff":
        inter = interest / (12 * 100)
        s = 0
        for n in range(period):
            month_pay = ceil(principal / period + inter * (principal - (principal * ((n + 1) - 1)) / period))
            print(f"Month{n+1}: payment is {month_pay}")
            s += month_pay
        overpayment = s - principal
        print(f"Overpayment = {overpayment}")
    else:
        print("Invalid Key")


if __name__ == '__main__':
    main()
