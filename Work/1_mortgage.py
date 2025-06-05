# mortgage.py
#
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 
# with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
# The interest rate is 5% (monthly?) and the monthly payment is $2684.11.

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payments = 1000.0 + payment
total_paid = 0.0
count = 1

while principal > 0:
    if count <= 10:
        payment = extra_payments
    
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    count += 1

print(f"Total paid ${total_paid:,.2f} after {count} years")