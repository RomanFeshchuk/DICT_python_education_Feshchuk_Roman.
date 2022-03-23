#2 (The Second Stage)

from math import ceil


def main():
    print('Loan principal: 1000')
    print('The First month: repaid 250')
    print('The Second month repaid 250')
    print('The Third month repaid 500')
    print('The Final payment: The loan has been repaid!')
    principal = int(input())
    print('What do you want to calculate?')
    print('Type "m" - for number of monthly payments, type "p" - for the monthly payment:')
    action = input()
    if action == 'm':
        print('Enter the monthly payment:')
        payment = int(input())
        print(f'It will take {ceil(principal / payment)} month to repay the loan')
    elif action == 'P':
        print('Enter the nomber of month:')
        period = int(input())
        payment = ceil(principal / period)
        final_payment = principal - (period - 1) * payment
        if payment != final_payment:
            print(f'Your monthly payment = {payment} and the last payment = {final_payment}')
        else:
            print(f'Your monthly payment = {payment}')

if __name__ == '__main__':
        main()