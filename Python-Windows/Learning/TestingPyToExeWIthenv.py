import dotenv
import os
from pathlib import Path

#When you export to a single file it runs from the temp directory for __file__, but if you run it through a directory with the exe then it should be able 
#To use the .env file if you specify the path using __file__'s parent directory and then append on \.env

# path_env = Path(__file__).parent
# print(path_env)
# dotenv.load_dotenv(str(path_env) + r'\.env')
# print(str(path_env) + r'\.env')

# envVal = os.getenv('testVal')
# print(envVal)


#Moves up two directories for the current working directory from where this file is currently stored.
os.chdir(Path(__file__).parent.parent)
print(Path.cwd())