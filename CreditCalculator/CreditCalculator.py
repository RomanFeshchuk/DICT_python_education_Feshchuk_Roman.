# 3 (The Third Stage)
from math import ceil, log, trunc


def main():
    print("Enter the loan principal")
    principal = int(input())

    print("What do you want to calculate?")
    print('type "m" for number of monthly payments, type "p" for the monthly payment:')
    print('''type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
    action = input()
    if action == 'm':
        print("Enter the monthly payment")
    if action == 'n':
        print("Enter the loan principal:")
        payment = int(input())
        print(f'It will take {ceil(principal / payment)} months to repay the loan')
    elif action == 'p':
        print("Enter the number of months")
        period = int(input())
        payment = ceil(principal / period)
        final_payment = principal - (period - 1) * payment
        if payment == final_payment:
            print(f'Your monthly payment = {payment}')
        print("Enter the monthly payment:")
        mont_payment = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        num = ceil(log(mont_payment / (mont_payment - i * payment), 1 + i))
        year = trunc(num / 12)

        month = num - year * 12
        if month == 0:
            print(f"It will take {year} years to repay this loan!")
        elif year == 0:
            print(f"It will take {month} months to repay this loan!")
        else:
            print(f"Your monthly payment = {payment} and the last payment = {final_payment}")
            print(f"It will take {year} years and {month} months to repay this loan!")
    elif action == 'p':
        print("Enter the annuity payment:")
        a_payment = float(input())
        print("Enter the number of periods:")
        period = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        loan = trunc(a_payment * ((1 + i) ** period - 1) / (i * (1 + i) ** period))
        print(f"Your loan principal = {loan}!")
    elif action == 'a':
        print("Enter the loan principal:")
        payment = int(input())
        print("Enter the number of periods:")
        period = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        month_pay = ceil((payment * i * ((1 + i) ** period)) / (((1+i) ** period) - 1))
        print(f"Your monthly payment = {month_pay}!")


if __name__ == '__main__':
    main()
