import os, sys
import os.path
from itertools import repeat
from operator import itemgetter
import hashlib
import time

#compare second indexes from nested list and create potential list of duplicates
def compare(some_list, chunk_hash: bool):
    nlist=[]
    nlist.append([])
    for a in range(len(some_list)-1):
        if some_list[::1][a][1] == some_list[::1][a+1][1]: 
            nlist[0].append(some_list[::1][a][0])
            nlist[0].append(some_list[::1][a+1][0])
    rem_dupas = [list(set(lst)) for lst in nlist] #remove duplicate paths
    #print(nlist)    #[['E:\\photos\\IMG 1860 - Copy.jpg', 'E:\\photos\\IMG 1860.jpg', 'E:\\photos\\IMG 1873 - Copy.jpg', 'E:\\photos\\IMG 1873(2).jpg', 'E:\\photos\\IMG 1873(2).jpg', 'E:\\photos\\IMG 1873.jpg', 'E:\\photos\\IMG 1826 - Copy.jpg', 'E:\\photos\\IMG 1826.jpg']]
    rem_dupas.append([])
    for b in range(len(rem_dupas[0])):
        with open (rem_dupas[0][b], "rb") as data:
            #print(rem_dupas[0][b])
            if chunk_hash:
                output=data.read(1024)
            else:
                data1=data.read()
                output=hashlib.sha1(data1).hexdigest()
        rem_dupas[1].append(output)

    return rem_dupas

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

sys.argv.append('M:\\docs\\')
flist=[]
start=time.time()
temp=os.walk(sys.argv[1], topdown=False)

for root, dirs, files in temp:
    for i in files:
        fsize = []
        fsize.append(os.path.join(root,i))
        fsize.append(os.stat(os.path.join(root,i)).st_size)
        flist.append(fsize)
flist.sort(key=itemgetter(1))


print('\nTotal duplicates based on file size - {}'.format(len(compare(flist, True)[0])))
print('Total duplicates based on first 1024 bytes - {}'.format(len(merge(compare(flist, True)))))
print('Total duplicates based on hash - {}'.format(len(merge(compare(flist, False)))))
print('Found in {} seconds'.format(round(time.time()-start, 2)))