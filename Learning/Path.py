#Seeing how python handles paths and refrencing files

import os
from pathlib import Path
#__file__ is the refrence to where this file is at.
dir_name = os.path.dirname(__file__)

#Changes the current working directory to that of the parent of the current file
os.chdir(dir_name)

#Prints the current working path
print(Path.cwd())
i = 0
#Adds in some blank lines
while i < 5:
    print('')
    i += 1

#Print out directory listing
print(os.popen('dir').read())