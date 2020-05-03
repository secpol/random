import sys, os
from os import listdir
import os.path
import shutil

sys.argv.append(r'V:/working_dir/')
callendar = ['May','June','July','August','September']
year = '_2020'
my_name = 'John'
spreadsheets = {'ext':('.xls', '.xlsx')}

for item in callendar:
    dest = sys.argv[1]+item+year+'/'
    os.makedirs(dest)
    for i in os.listdir(sys.argv[1]):
        if os.path.isfile(sys.argv[1]+i):
            name_split = os.path.splitext(i)[0]
            s_sheets = os.path.splitext(i)[1]
            if my_name in name_split and s_sheets in spreadsheets['ext']:
                al = i.split('.')
                al.insert(1, '_'+item+'.')
                nfile = ''.join(al)
                shutil.copy(sys.argv[1]+i, dest+nfile) 
                print(dest+nfile)
