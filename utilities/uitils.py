import pandas as pd
import numpy as np

firstProductSet = {'Product1': ['Computer','Phone','Printer','Desk'],
                   'Price1': [1200,800,200,350]
                   }
df1 = pd.DataFrame(firstProductSet,columns= ['Product1', 'Price1'])


secondProductSet = {'Product2': ['Computer','Phone','Printer','Desk'],
                    'Price2': [1200,810,200,360]
                    }
df2 = pd.DataFrame(secondProductSet,columns= ['Product2', 'Price2'])


def compareTwoDF(df1,df2):
    dfc=df1.copy()
    dfc['Price2'] = df2['Price2'] #add the Price2 column from df2 to df1
    dfc['pricesMatch'] = np.where(dfc['Price1'] == df2['Price2'], 'True', 'False')  #create new column in df1 to check if prices match
    print (dfc)
compareTwoDF(df1,df2)
