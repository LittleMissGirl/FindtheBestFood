import nltk
lines = 0
i = 0
f = open("getSelectFood.txt")
fout = open("getReview.txt","w")
raw = f.read()
print type(raw)
print len(raw)

f.seek(0)
while f.readline():
    lines = lines + 1
print lines

f.seek(0)
for i in range(1,lines):
    stringstack = f.readline()
    medium = stringstack.split(":")    
    if medium[0] == 'review/text':
        for i in stringstack[13:]:
            fout.write(i)
fout.close()

