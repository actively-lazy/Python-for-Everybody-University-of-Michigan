try:
    score = float(input("Enter Score: "))
except:
    print("Error")
if 1 >= score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
