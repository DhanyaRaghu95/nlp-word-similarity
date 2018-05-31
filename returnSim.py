import pickle
pairs = [("narendra","modi"),("controversial","minister"),("temple","mosque"),("speech","commentary"),("chanting","crowd"),("indian","foreign"),("cricket","stadium"),("government","participation"),("politics","border"),("investment","opposition"),("congress","india")]

T = pickle.load(open("trigrams.p"))
mD = pickle.load(open("mD.p"))

Z = 0
D = 0
for p in pairs:
    for t in T.keys():
        #for t check if pairs are middle
        Z += mD[p[0]][t]
        Z += mD[p[1]][t]
        Z = abs(mD[p[0]][t] - mD[p[1]][t])

    print "pair : ",p," : ", (1 - float(Z/D))
