#Seeing how python handles paths and refrencing files

import os
from pathlib import Path
#__file__ is the refrence to where this file is at.
dir_name = os.path.dirname(__file__)

print(dir_name)


#This is the where the person executing is located right now.
print(Path.cwd())