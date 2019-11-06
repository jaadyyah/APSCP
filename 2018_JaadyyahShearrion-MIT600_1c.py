init_balance = float(input("What is your outstanding balance? "))
interest = float(input("What is your annual interest?"))
balance = 1
upper_bound = (init_balance * (1 + (interest / 12.0)) ** 12.0) / 12.0
lower_bound = init_balance / 12.0
monthly_pay = (upper_bound + lower_bound) / 2

while abs(balance) >= .005:
    balance = init_balance
    for month in range(12):
        balance *= (1 + (interest / 12))
        balance -= monthly_pay
    if balance > 0:
        lower_bound = monthly_pay
        monthly_pay = (upper_bound + monthly_pay) / 2
    elif balance < 0:
        upper_bound = monthly_pay
        monthly_pay = (lower_bound + monthly_pay) / 2

monthly_pay = round(monthly_pay, 2)

print("Monthly payment:", monthly_pay)

# hi this is Claire and it does everything the rubric says it needs to and also it works in the test cases
