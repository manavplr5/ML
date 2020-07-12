import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(-5.0 , 5.0, 0.1)

#make changes in slope nd intercept to verify the changes in graph
y = 2*(x) + 3
y_noise = 2 * np.random.normal(size = x.size)
ydata = y + y_noise
plt.plot(x,ydata, 'bo')
plt.plot(x,y, 'r')
plt.ylabel('Dependent Variable')
plt.xlabel("Independent Variable")
plt.show()


#Graph of a cubic function
x = np.arange(-5.0, 5.0, 0.1)
y = 1*(x**3) + 1*(x**2) + 1*x + 3
y_noise = 2 * np.random.normal(size=x.size)
ydata = y + y_noise
plt.plot(x, ydata, 'bo')
plt.plot(x, y, 'r')
plt.ylabel("Dependent Variable")
plt.xlabel("Independent Variable")
plt.shows()

#Graph of a quadratic function
x = np.arange(-5.0, 5.0, 0.1)
y = np.power(x, 2)
y_noise = 2 * np.random.normal(size = x.size)
ydata = y + y_noise
plt.plot(x,y, 'bo')
plt.plot(x, ydata, 'r')
plt.ylabel("Dependent Variable")
plt.xlabel("Independent Variable")
plt.show()

#Exponential Function
x = np.arange(-5.0, 5.0, 0.1)
y = np.exp(x)

plt.plot(x,y)
plt.ylabel('Dependent Variable')
plt.xlabel('Independent Variable')
plt.show()

#Logarithmic
x = np.arange(-5.0, 5.0, 0.1)
y= np.log(x)
plt.plot(x,y)
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()


#Seismoidal/ Logistic
x = np.arange(-5.0, 5.0, 0.1)
y = 1-4/(1+np.power(3, x-2))
plt.plot(x,y)
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()







