# Student No. 202201723 Mahmoud Atta

import pandas as pd
mydataset = pd.read_csv('iris.csv')
x = mydataset.iloc[:,:].values
y = mydataset.iloc[:,:-1].values
m = mydataset.groupby('class').size()
n = mydataset.head(20)

s = mydataset.plot(kind='box',
subplots = True, layout=(2,2),
sharex=False, sharey=False)

g=pd.plotting.scatter_matrix(mydataset)


