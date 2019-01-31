words = list()
count = 0
for line in open(input("Enter file name: ")):
    if line.startswith("From "):
        words = line.rstrip().split()
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
