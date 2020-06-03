# lightweight and ultra-fast script to rename large collection of music stored on your HDD
# sample directory tree:
# Y:.
#├───Best Band vol 24 cd1
#├───Best Band vol 24 cd2
#├───Best Band vol 25 cd1
#├───Best Band vol 25 cd2
# Output:
# Y:.
#├───Best Band Vol. 24
#│   ├───Cd 1
#│   └───Cd 2
#├───Best Band Vol. 25
#│   ├───Cd 1
#│   └───Cd 2

import re
import sys, os
from os import listdir
import os.path

cdname = 'Best Band Vol. '
cdnumber = 'Cd '
sys.argv.append(r'Y:/new/new/')

for i in os.listdir(sys.argv[1]):
    if os.path.isdir(sys.argv[1]+i) and re.search('\d\d', i):
        volume = re.findall('\d\d*', i)
        try:
            os.mkdir(sys.argv[1]+cdname+volume[0])
        except FileExistsError:
            pass
        os.rename(sys.argv[1]+i, sys.argv[1]+cdname+volume[0]+'/'+cdnumber+volume[1][0])