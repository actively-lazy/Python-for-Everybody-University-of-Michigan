# Use the file name mbox-short.txt as the file name
total = 0
count = 0
for line in open(input("Enter file name: ")):
    if not line.startswith("X-DSPAM-Confidence:"): continue
    total += float(line[line.find(":") + 1::].strip())
    count += 1
print("Average spam confidence:", total / count)
