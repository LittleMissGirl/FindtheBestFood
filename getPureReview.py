f = open("getReview.txt")
fout = open("pureReview.txt","w")

for line in f:
    fout.write(line.replace("&quot;",'"').replace("&quot",'"').replace("&amp;","&"))
fout.close()
print "done!"
