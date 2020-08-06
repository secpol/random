import os, sys
import os.path

sys.argv.append('M:\\photos\\')

count = 0
temp = os.walk(sys.argv[1], topdown=False)
flist = []
for root, dirs, files in temp:
    for i in files:
        flist.append(i)
        #count+=1
flist.sort()
for a in range(len(flist)-1): 
    if flist[a] == flist[a+1]:
        count+=1
        print (flist[a]) 
#print(flist)
print('\nDups: {}'.format(count))