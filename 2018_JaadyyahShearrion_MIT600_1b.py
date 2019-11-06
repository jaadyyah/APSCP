new_balance = float(input('What is your outstanding balance on your credit card? '))
interest = float(input('What is your annual interest rate? '))
monthly_pay = 0
months = 13

while months > 12:  # the while statements are very new to me but it seems like this would help.
    months = 0     # while makes sure that my condition is filled, if it isnt then it keeps going
    monthly_pay += 10
    balance = new_balance
    while balance > 0:
        balance = round(balance * (1 + (interest / 12)), 2)
        balance = round(balance - monthly_pay, 2)  # the code here and ^ makes sure that I do these
        months += 1                                                 # things to the existing balance
        print(balance)
        if months > 12:
            break
# this is new to me, luckily I remember the words of a very wise man named Eli.
# 'Um... this is wrong' Thanks wise man. But in all seriousness I half remember what he said about some builtin
# functions so, yeah. Break, I googled what could make the code stop after 12 months and that is what I found

print('Monthly payment to pay off debt after 1 year is, ', monthly_pay)
print('Number of months needed is: ', months)

# hi this is claire and i checked jaadyyah's code. it works and does everything it needs to.
# for a while it wasn't working because she forgot to cast something as a float, but now it works
