words = list()
for line in open(input("Enter file name: ")):
    for word in line.rstrip().split():
        if word not in words: words.append(word)
words.sort()
print(words)
