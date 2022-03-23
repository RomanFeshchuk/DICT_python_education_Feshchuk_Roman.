#1 (The First Stage)
def main ():
   print('The Loan principal: 1000')
   print('The First month: repaid 250')
   print('The Secon month: repaid 250')
   print('The Thirg month: repaid 500')
   print('The Final output: The loan has been repaid!')
   if __name__ == '__main__':
    main()
#2 (The Second Stage)
from math import ceil

def main():
    print('The Loan principal: 1000')
    print('The First month: repaid 250')
    print('The Secon month: repaid 250')
    print('The Thirg month: repaid 500')
    print('The Final output: The loan has been repaid!')
    print('Please Enter the Loan principal')
    principal = int(input())

    print('What do you want to calculate?')
    print('Type "m" - for number of monthly payments, type "p" - for the monthly payment:')
    action = input()
    if action == 'm':
       print('Enter the monthly payment:')
       payment = int(input())
       print(f'It will take {ceil(principal / payment)} month to repay the loan')
    elif action == 'p':
       print('Enter the number of month:')
    period = int(input())
    payment = ceil(principal / period)
    thefinal_payment = principal - (period - 1) * payment
    if payment == thefinal_payment:
       print(f'Your monthly payment = {payment}')
    else:
       print(f'Your monthly payment = {payment} and the final payment = {thefinal_payment}')



if __name__ == '__main__':
        main()