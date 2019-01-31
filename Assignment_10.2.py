dict = dict()
for line in open(input("Enter file name: ")):
    if line.startswith("From "):
        words = line.rstrip().split()
        hour = words[5].split(":")[0]
        dict[hour] = dict.get(hour, 0) + 1

dict = sorted(((k, v) for k, v in dict.items()))

for word in dict:
    print(word[0], word[1])
