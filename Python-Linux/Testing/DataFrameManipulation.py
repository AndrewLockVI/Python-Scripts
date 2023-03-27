import requests
import pandas as pd
from pathlib import Path


#This is to simulate 
df = pd.DataFrame(
	{'NAME' : 
		('ANDREW', "SALLY" , "LISA", None), 
	'WEIGHT' : 
		(150, 132, 129 , 142), 
	'ISMALE' :
		 (True, False, False, True), 
	 'MED EXCEPTION' : 
	 	(None, 'Cancer' , None, None), 
	'PRIMARY PHONE' : 
	(6023020320, 3902390239, 932939394, None)})

#This prints out ahe list where WHEIGHT <> NaN
print(df.dropna(subset=['WEIGHT']))

#This prints out the list where NAME <> NaN
print(df.dropna(subset=['NAME']))

#This prints out the original data frame to show that the variable is not being manipulated by using the .dropna() function.
print(df)


"""
Output:
     NAME  WEIGHT  ISMALE MED EXCEPTION  PRIMARY PHONE
0  ANDREW     150    True          None   6.023020e+09
1   SALLY     132   False        Cancer   3.902390e+09
2    LISA     129   False          None   9.329394e+08
3    None     142    True          None            NaN
     NAME  WEIGHT  ISMALE MED EXCEPTION  PRIMARY PHONE
0  ANDREW     150    True          None   6.023020e+09
1   SALLY     132   False        Cancer   3.902390e+09
2    LISA     129   False          None   9.329394e+08
     NAME  WEIGHT  ISMALE MED EXCEPTION  PRIMARY PHONE
0  ANDREW     150    True          None   6.023020e+09
1   SALLY     132   False        Cancer   3.902390e+09
2    LISA     129   False          None   9.329394e+08
3    None     142    True          None            NaN
[Finished in 318ms]

"""