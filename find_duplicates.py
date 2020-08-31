import os, sys, io
import os.path
from itertools import repeat
import hashlib
import time

#compare second indexes from nested list and create potential list of duplicates
#then remove duplicate paths
def compare(some_list):
    nlist=[]
    nlist.append([])
    for a in range(len(some_list)-1):
        if some_list[a][1] == some_list[a+1][1]: 
            nlist[0].append(some_list[a][0])
            nlist[0].append(some_list[a+1][0])
    nlist = [list(set(lst)) for lst in nlist]

    return nlist

#get 1024/8192 bytes chunk of file, hash it and/or append it to the list
def chunk_hash(get_list, sel: bool):  
    get_list.append([])
    for b in range(len(get_list[0])):
        with open (get_list[0][b], "rb") as data:
            if sel:
                if b == 0:
                    print('\rProccessing 1024 bytes chunk...')
                output=data.read(1024)
            else:
                if b == 0:
                    print('\rProccessing 8196 bytes hash...')
                data=data.read(8192)
                output=hashlib.sha1(data).hexdigest()
        get_list[1].append(output)

    return get_list

#merge file path with file byte chunk/hash
def merge(another_list):
    merge = []
    for t in range(len(another_list[0])):
        merge_row = []
        for row in another_list:
            merge_row.append(row[t])
        merge.append(merge_row)
    merge.sort(key=lambda elem: elem[1])

    return merge

def wrapper(hashed):
    for duplicate in range(len(hashed)):
        if duplicate % 2 == 0:
            try:
                x1 = hashed[duplicate][0]
                x2 = hashed[duplicate+1][0]
            except IndexError:
                pass
            #print('Duplicate file found: {} ---> {}'.format(x1, x2))
            #with io.open('duplicates.txt', "a", encoding="utf-8") as f:
            #    f.write('Duplicate file found: {} ---> {}'.format(x1, x2)+'\n')

sys.argv.append('M:\\photos\\')

flist=[]
count=0
start=time.time()
temp=os.walk(sys.argv[1], topdown=False)

for root, dirs, files in temp:
    for i in files:
        count+=1
        fsize = []
        fsize.append(os.path.join(root,i))
        fsize.append(os.stat(os.path.join(root,i)).st_size)
        flist.append(fsize)
        print('\r' + 'File progress: {}'.format(count), end='')
flist.sort(key=lambda elem: elem[1])

size_list = compare(flist)
size_list = merge(chunk_hash(size_list, True))
hash_list = compare(size_list)
hash_list = merge(chunk_hash(hash_list, False))
wrapper(hash_list) 

print('\nTotal duplicates based on file size - {}'.format(len(compare(flist)[0])))
print('Total duplicates based on first 1024 bytes - {}'.format(len(size_list)))
print('Total duplicates based on hash - {}'.format(len(hash_list)))
print('Total files scanned - {}'.format(count))
print('Found in {} seconds'.format(round(time.time()-start, 2)))