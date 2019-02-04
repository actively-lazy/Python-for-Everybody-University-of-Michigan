import re

sum = 0
for line in open(input("Enter file name: ")):
    numbers = re.findall('([0-9]+)', line)
    if len(numbers) < 1: continue
    for num in numbers:
        sum += int(num)
print(sum)
