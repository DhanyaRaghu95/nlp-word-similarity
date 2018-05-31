dic = {}
out = open("unigram.txt", 'w')
pro = open("probability.txt", 'w')
count = 0
with open("output.txt", 'r') as f:
    for line in f:
        words = line.strip().split()
        uni = words
        count += len(words)
        for i in uni:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
for i in uni:
    out.write(str(i) + "\n")
prob = {}
k = 0
for i, j in dic.items():
    prob[k] = float(j) / count
    pro.write(i + ":" + str(prob[k]) + "\n")
    k += 1

thresh = 1.4469016049e-06
pro.close()
out.close()
