import os, sys
import os.path
from itertools import repeat
from operator import itemgetter
import hashlib
import time

sys.argv.append('M:\\photos\\')
flist=[]
start=time.time()
temp=os.walk(sys.argv[1], topdown=False)

#compare second indexes from nested list and create potential list of duplicates
def compare(some_list):
    nlist=[]
    nlist.append([])
    count=0
    for a in range(len(some_list)-1):
        if some_list[::1][a][1] == some_list[::1][a+1][1]:
            count+=1
            nlist[0].append(some_list[::1][a][0])
            nlist[0].append(some_list[::1][a+1][0])
    #nlist.sort()
    removed = [list(set(lst)) for lst in nlist]
    #print(nlist)    #[['E:\\photos\\IMG 1860 - Copy.jpg', 'E:\\photos\\IMG 1860.jpg', 'E:\\photos\\IMG 1873 - Copy.jpg', 'E:\\photos\\IMG 1873(2).jpg', 'E:\\photos\\IMG 1873(2).jpg', 'E:\\photos\\IMG 1873.jpg', 'E:\\photos\\IMG 1826 - Copy.jpg', 'E:\\photos\\IMG 1826.jpg']]
    return removed,count

#merge file path with file header/hash(TODO)
def merge(another_list):
    merge = []
    for t in range(len(another_list[0])):
        merge_row = []
        for row in another_list:
            merge_row.append(row[t])
        merge.append(merge_row)
    merge.sort(key=itemgetter(1))
    return merge

for root, dirs, files in temp:
    for i in files:
        fsize = []
        fsize.append(os.path.join(root,i))
        fsize.append(os.stat(os.path.join(root,i)).st_size)
        flist.append(fsize)
flist.sort(key=itemgetter(1))

tsts = compare(flist)[0]
tsts.append([])
for c in range(len(tsts[0])):
    with open (tsts[0][c], "rb") as chunk:
        header=chunk.read(1024)
    tsts[1].append(header)

print('\nTotal duplicates based on file size - {}'.format(compare(flist)[1]))
print('Total duplicates based on first 1024 bytes - {}'.format(compare(merge(tsts))[1]))
print('Found in {} seconds'.format(round(time.time()-start, 2)))
