import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')
diamonds = pd.read_csv('diamonds.csv', index_col=0)
#print diamonds['carat']>2
#filterframe=[diamonds.iloc[x] for x in diamonds.index if diamonds[x,'carat'x>2]# if x.loc['carat']>2]
#print filterframe
diamonds[diamonds['carat'] >2]['price'].plot(kind='hist')
