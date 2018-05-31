"""token = [1,2,3,3,5,6,7]
new_trigrams = []
c = 0
while c < len(token) - 2:
    new_trigrams.append((token[c], token[c+1], token[c+2]))
    c += 1
print new_trigrams"""
pairs = [("narendra","modi"),("controversial","minister"),("temple","mosque"),("speech","commentary"),("chanting","crowd"),("indian","foreign"),("cricket","stadium"),("government","participation"),("politics","border"),("investment","opposition"),("congress","india")]
##making a unigram model
import pickle
trigrams = pickle.load(open("trigrams.p"))
f = open("output.txt")
new_trigrams = []

for line in f.readlines():
    token = line.split()
    c = 0
    while c < len(token) - 2:
        new_trigrams.append((token[c], token[c+1], token[c+2]))
        c += 1
#print new_trigrams

T = dict()

# ##################### 8
# forming T
for t in new_trigrams:
    if t not in T.keys():
        T[t] = 1
    else:
        T[t] += 1

pickle.dump(T, open("trigrams.p", "w"))
# ####### 9
#count()

print len(set(T)), len(new_trigrams)
#forming inverse dic
#   w : [t]
mD = dict()
for t in T:
    if t[1] not in mD.keys():
        mD[t[1]] = dict()
    if t not in mD[t[1]].keys():
        mD[t[1]][t] = 1
    else:
        mD[t[1]][t]+=1

print mD.keys()
pickle.dump(mD,open("mD.p","w"))
exit()




Z = 0
D = 0
for p in pairs:
    for t in T.keys():
        #for t check if pairs are middle
        Z += mD[p[0]][t]
        Z += mD[p[1]][t]
        Z = abs(mD[p[0]][t] - mD[p[1]][t])

print (1 - float(Z/D))




