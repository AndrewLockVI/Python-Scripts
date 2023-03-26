import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

fig, ax= plt.subplots()



excel_path = str(Path(__file__).parent) + '/test.xlsx'
to_write = pd.DataFrame({ 'NAME' : ['James', 'Timmy', 'Sally'], 'WIDTH' : [22 , 12 , 12], 'HEIGHT' : [22 , 45 , 43]})
to_write.to_excel(str(Path(__file__).parent) + '/test.xlsx', sheet_name='test_sheet')



out_excel = pd.read_excel(str(Path(__file__).parent) + '/test.xlsx')

update_excel = out_excel.append( {'NAME' : 'Andrew' , 'HEIGHT': 22 , 'WIDTH' : 20}, True)

update_excel.to_excel(str(Path(__file__).parent) + '/test.xlsx', sheet_name='test_sheet')

excel = pd.read_excel(excel_path)
xaxis = excel['NAME']
yaxis = excel['WIDTH']


ax.bar(xaxis , yaxis)
plt.show()




