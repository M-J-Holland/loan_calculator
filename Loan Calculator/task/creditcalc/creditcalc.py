# write your code here
import math
loan_principal = float(input("Enter loan principal: "))
user_selection = input('What do you want to calculate?\ntype "m" - for number of monthly payments,\ntype "p" - for '
                       'the monthly payment:\n')
if user_selection.lower() == 'm':
    monthly_payment = float(input("Enter monthly payment: "))
    total_time_to_pay = math.ceil(loan_principal / monthly_payment)
    if total_time_to_pay > 1:
        unit = 'months'
    else:
        unit = 'month'

    print(f"It will take {total_time_to_pay} {unit} to replay the loan")
elif user_selection.lower() == 'p':
    total_months = int(input("Enter total number of months: "))
    monthly_payment = math.ceil(loan_principal / total_months)
    if loan_principal % total_months == 0:
        print(f"The monthly payment is {monthly_payment}")
    else:
        last_payment = int(loan_principal - (total_months - 1) * monthly_payment)
        print(f"Your monthly payment = {math.ceil(monthly_payment)}, and the last payment = {last_payment}")