import pandas as pd
import numpy as np

print("<---------------- Table 1 ---------------------------------------->")
print("")
df = pd.read_csv(r'C:\Users\anubh\OneDrive\Documents\Datasets\MiltonData.csv')

pd.options.display.float_format = "{:,.0f}".format

df = df.drop(columns=['Week','ItemGroup', 'Market', 'TimeOfActivity', 'TotPeople' ])

df = df.groupby(["Item","State"], as_index=True)["TotMins"].sum()


df = df.unstack()

df['Grand Total'] = df.sum(axis=1)

df = df.sort_values(by='Grand Total', ascending=False)

df.loc['Grand Total']= df.sum()

print(df)

print("<----------------------Table 2---------------------------------------->")

df_2 = pd.read_csv(r'C:\Users\anubh\OneDrive\Documents\Datasets\MiltonData.csv')
df_2 = df_2.drop(columns=['Week', 'Market', 'TimeOfActivity', 'TotPeople' ])


df_2 = df_2.groupby([ 'ItemGroup', 'Item', 'State'], as_index=True)["TotMins"].sum()
df_2 = df_2.unstack()

itemGroup2 = (df.loc[['Item04', 'Item07', 'Item10']])

itemGroup2.loc['ItemGroup2'] = itemGroup2.sum()
itemGroup2 = itemGroup2.reset_index()


print(" ")
itemGroup1 = (df.loc[['Item01', 'Item02', 'Item03', 'Item05', 'Item06', 'Item08', 'Item09', 'Item11', 'Item12']])

itemGroup1.loc['ItemGroup1'] = itemGroup1.sum()
itemGroup1 = itemGroup1.reset_index()

print("")
df = pd.DataFrame(np.concatenate([itemGroup1, itemGroup2]), columns=itemGroup1.columns)




df = df.reindex([9,0,1,2,3,4,5,6,7,8,13,10,11,12])

sum = df.iloc[0] + df.iloc[10]




df.loc[len(df)+1] = ['Grand Total'] + df.iloc[[0,10], 1:].sum(axis=0).tolist()
print(df)

print("<----------------- Table 3 -----------------------------------------------------> ")
print("")

df_3 = pd.read_csv(r'C:\Users\anubh\OneDrive\Documents\Datasets\MiltonData.csv')
df_3 = df_3[df_3.Item == 'Item04']

df_3 = df_3.drop(columns=['Item','ItemGroup', 'Market', 'TimeOfActivity', 'TotPeople' ])


df_orginal = df_3.groupby(["Week","State"], as_index=True)["TotMins"].sum()
df_orginal = df_orginal.unstack()

df_orginal['Grand Total'] = df_orginal.sum(axis=1)
df_orginal.loc['Total TotMIns']= df_orginal.sum()

df_orginal = df_orginal.reset_index()


print("")
df_3 = df_3.groupby(["Week","State"], as_index=True)["TotMins"].sum()
df_3 = df_3.unstack()


df_3['Grand Total'] = df_3.sum(axis=1)


df_3['State1'] = df_3.iloc[:, 0]/df_3.iloc[:, 4] *100
df_3['State2'] = df_3.iloc[:, 1]/df_3.iloc[:, 4] *100
df_3['State3'] = df_3.iloc[:, 2]/df_3.iloc[:, 4] *100
df_3['State4'] = df_3.iloc[:, 3]/df_3.iloc[:, 4] *100
df_3['Grand Total'] = df_3.iloc[:, 4]/df_3.iloc[:, 4] *100
df_3.loc['Total % of Mins By State'] = df_3.mean(axis=0)

df_3 = df_3.reset_index()

print("")
df_3 = pd.DataFrame(np.concatenate([df_orginal, df_3]), columns=df_orginal.columns)

df_3= df_3.reindex([0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,13,27])
df_3.round(decimals=0)
print(df_3)




print("")

print("<----------------------- Table 4 ---------------------------->")
df_4 = pd.read_csv(r'C:\Users\anubh\OneDrive\Documents\Datasets\MiltonData.csv')

df_4 = df_4[df_4.Item == 'Item07'] 
df_4 = df_4[df_4.State == 'State4']

df_4['AvgMins/Psn'] = df_4['TotMins']/df_4['TotPeople']

print(df_4)
df_4 = df_4.drop(columns=['Item','ItemGroup', 'State', 'TimeOfActivity', 'TotPeople', 'TotMins'])

df_4 = df_4.groupby(["Week", 'Market'], as_index=True)['AvgMins/Psn'].mean()

df_4 = df_4.unstack()

df_4.loc['Grand Total'] = df_4.mean(axis=0)
df_4['Grand Total'] = df_4.mean(axis=1)

print(df_4)

print("<----------------------- Table 5 ---------------------------->")

df_5 = pd.read_csv(r'C:\Users\anubh\OneDrive\Documents\Datasets\MiltonData.csv')

df_5 =  df_5[df_5.Market == 'Market09']
df_5 = df_5[df_5.ItemGroup == 'ItemGroup2']

df_5 = df_5.drop(columns=['Item','ItemGroup', 'State', 'Market','TotMins'])

df_5 = df_5.groupby(["Week", 'TimeOfActivity'], as_index=True)["TotPeople"].sum()

df_5 = df_5.unstack()


df_5['Grand Total'] = df_5.sum(axis=1)
df_5.loc['Grand Total'] = df_5.sum(axis=0)
print(df_5)

print("<--------------------------Table 6 -------------------------------->")

df_5['M-F'] = df_5['M-F Afternoon'] + df_5['M-F Morning']
df_5['S&S'] = df_5['S&S Afternoon'] + df_5['S&S Morning']

df_5 = df_5.drop(columns=['M-F Afternoon','M-F Morning', 'S&S Afternoon', 'S&S Morning'])

df_5 = df_5.reindex(columns=['M-F','S&S','Grand Total'])
print(df_5)

print("<--------------------------Table 7 -------------------------------->")
df_7 = df_5

df_7.loc['4Wk to 2020W13'] = df_7.iloc[[0,1,2,3], 0:].mean()
df_7.loc['4Wk to 2020W14'] = df_7.iloc[[1,2,3,4], 0:].mean()
df_7.loc['4Wk to 2020W15'] = df_7.iloc[[2,3,4,5], 0:].mean()
df_7.loc['4wk to 2020W16'] =  df_7.iloc[[3,4,5,6], 0:].mean()
df_7.loc['4wk to 2020W17'] =  df_7.iloc[[4,5,6,7], 0:].mean()
df_7.loc['4wk to 2020W18'] =  df_7.iloc[[5,6,7,8], 0:].mean()
df_7.loc['4wk to 2020W19'] =  df_7.iloc[[6,7,8,9], 0:].mean()
df_7.loc['4wk to 2020W20'] =  df_7.iloc[[7,8,9,10], 0:].mean()
df_7.loc['4wk to 2020W21'] =  df_7.iloc[[8,9,10,11], 0:].mean()
df_7.loc['4wk to 2020W22'] =  df_7.iloc[[9,10,11,12], 0:].mean()

df_7 = df_7.drop(df_7.index[range(14)])

print(df_7)
print("")