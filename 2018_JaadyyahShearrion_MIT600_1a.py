balance = float(input('What is your outstanding balance on your credit card? '))
annual_interest = float(input('What is your annual interest rate? '))
month_rate = float(input('What is your minimum monthly payment rate? '))

paid = 0
for month in range(12):
    print('Month; ', month + 1)
    min_payment = (month_rate * balance)
    interest_paid = ((annual_interest / 12) * balance)
    principal = (min_payment - interest_paid)
    balance = (balance - principal)
    paid = (min_payment + paid)
    print('Payment for this month: ', round(min_payment, 2))
    print('Principal payment: ', round(principal, 2))
    print('Remaining balance: ', round(balance, 2))

print('Total payment:', round(paid, 2))
print('Remainder: ', round(balance, 2))

# hi this is claire and I helped her fix a rounding issue bc it was rounding too early but it works now yay
# it gives basically the same number as the test
