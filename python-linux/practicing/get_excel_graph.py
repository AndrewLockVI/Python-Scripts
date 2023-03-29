import requests
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt



req = requests.get('https://dornsife.usc.edu/assets/sites/298/docs/ir211wk12sample.xls')
open(str(Path(__file__).parent) + '/output.xlsx', 'wb').write(req.content)

excel_content = pd.read_excel(req.content)


xaxis = excel_content['OrderDate']

yaxis = excel_content['Rel. Freq']



#This was a round about way to drop a row only if these two columns contained NaN values. I will in the future use .dropna(subset=[row_val])
new_dataframe = pd.DataFrame({ 'X' : xaxis , 'Y' : yaxis})
new_dataframe = new_dataframe.dropna()






fig, ax = plt.subplots()
ax.bar (range(0, len(yaxis)) , yaxis)
plt.show()
