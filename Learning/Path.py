#Seeing how python handles paths and refrencing files
#This is important because direct file refrences i.e. open('rndfile.txt')
#will not work unless the python file is executed from the directory that
#also has rndfile.txt in it unless you change to the proper directory using
#os.chdir() where the input is the correct path.

import os
from pathlib import Path
#__file__ is the refrence to where this file is at.
dir_name = os.path.dirname(__file__)


#Changes the current working directory to that of the parent of the current file
os.chdir(dir_name)
print(dir_name)

# #Prints the current working path
# print(Path.cwd())
# i = 0
# #Adds in some blank lines
# while i < 5:
#     print('')
#     i += 1


# #Print out directory listing
# print(os.popen('dir').read())