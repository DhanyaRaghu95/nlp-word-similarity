import pickle
f = open("output.txt","r")
pairs = [("narendra","modi"),("controversial","minister"),("temple","mosque"),("speech","commentary"),("chanting","crowd"),("indian","foreign"),("cricket","stadium"),("government","participation"),("politics","border"),("investment","opposition"),("congress","india")]

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
    prob[i] = float(j)# / count
    pro.write(i + ":" + str(prob[i]) + "\n")
    k += 1
print sorted(prob.values())[5000]

thresh = 2
pro.close()
out.close()
vocab = {}
for i in prob.keys():
    if prob[i] > thresh:
        vocab[i] = prob[i]

f = open("output.txt","r")
fo = open("new_corpus.txt","w")
for i in f.readlines():
    tok = i.split()
    for j in i.split():
        if j not in vocab.keys():
            tok.remove(j)
            tok.append("?")
    fo.write(" ".join(tok))
    fo.write("\n")

fo.close()
f.close()

## write a new corpus
f = open("new_corpus.txt")
for i in f.readlines():
    token = i.split()
    new_trigrams = []
    c = 0
    while c < len(token) - 2:
        new_trigrams.append((token[c], token[c+1], token[c+2]))
        c += 1
print new_trigrams[:5]

pickle.dump(new_trigrams,open("trigrams.p","w"))

