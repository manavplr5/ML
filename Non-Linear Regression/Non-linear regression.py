import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit


url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/china_gdp.csv"
df = pd.read_csv(url)
df.head(10)

#plotting the dataset
plt.figure(figsize = (8,5))
x_data, y_data = (df['Year'].values, df["Value"].values)
plt.plot(x_data, y_data, 'ro')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()

#Choosing a model
x = np.arange(-5.0, 5.0)
y =1.0/(1.0 + np.exp(-x))
plt.plot(x,y)
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

#Building the model
def sigmoid( x, Beta_1, Beta_2):
	y = 1/(1 + np.exp(-Beta_1*(x - Beta_2)))
	return y

beta_1 = 0.10
beta_2 = 1990.0
y_pred = sigmoid(x_data, beta_1, beta_2)
plt.plot(x_data, y_pred*15000000000000.)
plt.plot(x_data, y_data, 'ro')
plt.show()

#We have to find best parameters foor our model, first normalize x and y
xdata = x_data/max(x_data)
ydata = y_data/max(y_data)

#How we find the best parameters for our fit line?
#we can use curve_fit which uses non-linear least squares to fit 
#our sigmoid function, to data. Optimal values for the parameters so 
#that the sum of the squared residuals of sigmoid(xdata, *popt) - ydata 
#is minimized.
#popt are our optimized parameters.
popt, pcov = curve_fit(sigmoid, xdata, ydata)
print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))

#plotting the resulting regression model
x = np.linspace( 1960, 2015, 55 )
x = x/max(x)
plt.figure(figsize = (8,5))
y = sigmoid(x, *popt)
plt.plot(xdata, ydata, 'ro', label = 'data')
plt.plot(x,y, linewidth=3.0, label='fit')
plt.legend(loc="best")
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()









