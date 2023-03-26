import pandas as pd
print('testing')


to_write = pd.DataFrame({ 'WIDTH' : [22 , 12 , 12], 'HEIGHT' : [22 , 45 , 43]})
to_write.to_excel('test.xlsx', sheet_name='test_sheet')
print('Data Frame Information: \n' + str(to_write))


out_excel = pd.read_excel('test.xlsx')
print(out_excel)




