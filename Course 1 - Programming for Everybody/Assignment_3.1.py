hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate per Hour:"))
pay  = rate*hrs
if hrs>40:
    pay += rate*(hrs-40)*0.5
print(pay)
