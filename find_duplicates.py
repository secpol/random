import os, sys, io
import os.path
import hashlib
import time

def compare(some_list):
    list1=[]
    list2=[]
    for a in range(len(some_list)-1):
        if some_list[a][1] == some_list[a+1][1] and some_list[a][0] != some_list[a+1][0]: 
            list1.append(some_list[a][0])
            list2.append(some_list[a+1][0])
    paths = list(zip(list1,list2))

    return paths

def chunk_hash(lista, switch: bool):
    list3=[]
    list4=[]
    for i,j in lista:
        list3.append(i)
        list3.append(j)
        try:
            with open(i, "rb") as data1, open(j, "rb") as data2:
                if switch:
                    if len(list3) == 2:
                        print('\rProccessing 1024 bytes chunk...')
                    out1=data1.read(1024)
                    out2=data2.read(1024)
                else:
                    if len(list3) == 2:
                        print('\rProccessing 8196 bytes hash...')
                    data1=data1.read(8192)
                    data2=data2.read(8192)
                    out1=hashlib.sha1(data1).hexdigest()
                    out2=hashlib.sha1(data2).hexdigest()
        except PermissionError as permission:
            print(permission)
            pass
        except OSError as syserror:
            print(syserror)
            pass
        list4.append(out1)
        list4.append(out2)
    seq=list(zip(list3,list4))
    seq.sort(key=lambda elem: elem[1])

    return seq


val=input('Type path, eg. D:/, /home/user\n')
while not os.path.isdir(val):
    val=input('Wrong input, try again\n')

flist=[]
count=0
start=time.time()
temp=os.walk(val, topdown=False)

for root, dirs, files in temp:
    for i in files:
        count+=1
        fsize = []
        fsize.append(os.path.join(root,i))
        fsize.append(os.stat(os.path.join(root,i)).st_size)
        flist.append(fsize)
        print('\r' + 'File progress: {}'.format(count), end='')
flist.sort(key=lambda elem: elem[1])

#animate = '|/-\\'
#idx = 0
comp1 = compare(flist)            
xc=chunk_hash(comp1, True)
comp2=compare(xc)
xh=chunk_hash(comp2, False)
comp3=compare(xh)
comp3.sort()

print('\nTotal duplicates based on file size - {}'.format(len(comp1)*2))
print('Total duplicates based on first 1024 bytes - {}'.format(len(comp2)))
print('Total duplicates based on hash - {}'.format(len(comp3)))
print('Total files scanned - {}'.format(count))
print('Found in {} seconds'.format(round(time.time()-start, 2)))

c=0
f = io.open('log7.txt', 'a', encoding='utf-8')
for o,p in comp3:
    c+=1
    f.write('{:05n} -- Duplicate file found: {} ---> {}'.format(c,o,p)+'\n')
f.close()
print('\nDone!')