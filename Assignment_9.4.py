dict = dict()
for line in open(input("Enter file name: ")):
    if line.startswith("From "):
        words = line.rstrip().split()
        dict[words[1]] = dict.get(words[1], 0) + 1

wordsHistogram = sorted(((v, k) for k, v in dict.items()), reverse=True)

print(wordsHistogram[0][1], wordsHistogram[0][0])
