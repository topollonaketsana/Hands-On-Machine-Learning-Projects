import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import sklearn as pd 
import sklearn.linear_model

oecd_bli = pd.read_csv ("oecd_bli_2015.csv", thousands= ' , ')
x =np.c_[country_stats["GDP per capita"]]
y =np.c_[country_stats["Life satisfaction"]]

country_stats.plot (kind= 'scatter', x= "GDP per capita", y= "Life satisfaction")
plt.show()

model = sklearn.linear_model.LinearRegression()

model.fit(x, y)


#x_new = [[22587]]
#print(model.predict(x_new))