import os, sys
import os.path
from collections import defaultdict
from itertools import repeat
from operator import itemgetter

sys.argv.append('E:\\impra\\')
count = 0
flist = []
tohash = []

temp = os.walk(sys.argv[1], topdown=False)

for root, dirs, files in temp:
    for i in files:
        fsize = []
        fsize.append(os.path.join(root,i))
        fsize.append(os.stat(os.path.join(root,i)).st_size)
        flist.append(fsize)

flist.sort(key=itemgetter(1))
for a in range(len(flist)-1): 
    if flist[::1][a][1] == flist[::1][a+1][1]:
        nlist = []
        nlist.append(flist[::1][a][0])
        with open (flist[::1][a][0], "rb") as chunk:
            header=chunk.read(1024)
        nlist.append(header)
        tohash.append(nlist)

        count+=1
        #tohash = list(zip(flist, fsize))
        print('file {} = {}'.format(flist[::1][a][0], flist[::1][a+1][0]))

print('total dups {}'.format(count))
print(tohash)

#print(str(res)) 
#print('\nDups: {}'.format(count))
#print(flist[::2]) #['M:\\photos\\asiii\\IMG 1826.jpg', 'M:\\photos\\asiii\\IMG 1833.jpg'....]
#print(flist[1::2]) #[49818, 49353, 48516, 50619...]