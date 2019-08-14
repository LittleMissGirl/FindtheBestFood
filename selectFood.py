lines = 0
f = open("finefoods.txt")
fout = open("getSelectFood.txt","w")
while f.readline():
    lines = lines +1
f.seek(0)
for i in range(1,lines):
    line = f.readline()
    stringstack = line.split(':')
    if stringstack[0] == 'product/productId':
        if stringstack[1] == ' B001GVISJM\n' :
            fout.write(line)  
            for i in range(0,8):
                fout.write(f.readline())
fout.close()
            
print 'done!'                
            
            
