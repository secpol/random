import os, sys
import os.path
from itertools import repeat
from operator import itemgetter
import time

sys.argv.append('E:\\')
count = 0
count2 = 0
flist = []
tohash = []
start = time.time()

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
        print('\r' + 'Equal size files: {}'.format(str(count)), end='')
        #print('file {} = {}'.format(flist[::1][a][0], flist[::1][a+1][0]))
for b in range(len(tohash)-1): 
    if tohash[::1][b][1] == tohash[::1][b+1][1]:
        count2+=1
        print('\r' + 'Equal chunk size files: {}'.format(str(count2)), end='')
        #print('found chunk {} is equal to this file {}'.format(tohash[::1][b][0], tohash[::1][b+1][0]))
        
#msec = round(1000 / avg, 4)
print('\nTotal duplicates based on file size - {}'.format(count))
print('Total duplicates based on first 1024 bytes - {}'.format(count2))
print('Found in {} seconds'.format(round(time.time()-start, 2)))