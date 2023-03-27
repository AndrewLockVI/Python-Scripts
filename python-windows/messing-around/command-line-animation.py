import time
from termcolor import colored
from pathlib import Path
options = ('=     ' , ' =', '  =' , '   =' , '    =')


text_art = open(str(Path(__file__).parent) + '\\AsciiArt.txt').read()
print(text_art)


count = 0
# while True:
#     if count > 4:
#         count = 0
    


#     #print( options[count], end='\r')
#     #print(colored('testing' , 'red'))



#     time.sleep(.2)
#     count += 1