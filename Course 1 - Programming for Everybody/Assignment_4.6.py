def computepay(hours, rate):
    pay = rate * hours
    if hours > 40:
        pay += rate * (hours - 40) * 0.5
    return pay


hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
print(computepay(hours, rate))
