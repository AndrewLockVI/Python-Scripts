#From indicates you would like a specific command from a library 
#If you just import os then it would be os.popen() instead of simply popen()

from os import popen

hello = popen("echo 'hello'")
dict = {"duck" : "quack" , "pig" : "oink" , "cow" : "moo"}
keyList = dict.keys()
valList = dict.values()
valStr = ' '.join(valList)


print(hello.read())
print(keyList)
print(valStr)
print(dict.get('duck'))