# write your code here
loan_principal = float(input("Enter loan principal: "))
monthly_payment = float(input("Enter monthly payment: "))

time_to_pay = loan_principal / monthly_payment
print(f"It will take {time_to_pay} months to pay off the loan")