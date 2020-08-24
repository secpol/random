import os, sys
import os.path
from itertools import repeat
from operator import itemgetter
import hashlib
import time


sys.argv.append('E:\\photos\\')

count2 = 0
flist = []
start = time.time()

temp = os.walk(sys.argv[1], topdown=False)

for root, dirs, files in temp:
    for i in files:
        fsize = []
        fsize.append(os.path.join(root,i))
        fsize.append(os.stat(os.path.join(root,i)).st_size)
        flist.append(fsize)
flist.sort(key=itemgetter(1))
#print (flist)   #[['E:\\photos\\IMG 1826.jpg', 49818], ['E:\\photos\\IMG 1833.jpg', 49353]...]

#compare second indexes from nested list and create potential list of duplicates
def compare(some_list):
    nlist = []
    nlist.append([])
    index_num = -1
    for a in range(len(some_list)-1):
        if some_list[::1][a][1] == some_list[::1][a+1][1]:
            index_num+=1
            nlist[0].append(some_list[::1][a][0])
            nlist[0].append(some_list[::1][a+1][0])
    #print(nlist)    #[['E:\\photos\\IMG 1860 - Copy.jpg', 'E:\\photos\\IMG 1860.jpg', 'E:\\photos\\IMG 1873 - Copy.jpg', 'E:\\photos\\IMG 1873(2).jpg', 'E:\\photos\\IMG 1873(2).jpg', 'E:\\photos\\IMG 1873.jpg', 'E:\\photos\\IMG 1826 - Copy.jpg', 'E:\\photos\\IMG 1826.jpg']]
    return nlist

lister = compare(flist)

lister.append([])
for c in range(len(lister[0])):
    with open (lister[0][c], "rb") as chunk:
        header=chunk.read(10)
    lister[1].append(header)
#print(lister)

tohash = []
for g in range(len(lister[0])):
    tohash_row = []
    for row in lister:
        tohash_row.append(row[g])
    tohash.append(tohash_row)
print(tohash)

print('\nTotal duplicates based on file size - {}'.format('TODO'))
print('Total duplicates based on first 1024 bytes - {}'.format('TODO'))
print('Found in {} seconds'.format(round(time.time()-start, 2)))
