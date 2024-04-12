#!/usr/bin/env python
# coding: utf-8

# ## Function plotter
# 

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
fx = input("Enter Function: ")
x_lower = int(input("Lower x bound: "))
x_upper = int(input("Upper x bound: "))
class Plot:
    def __init__(self, fx, x_lower, x_upper):
        self.fx = fx
        self.x_lower = x_lower
        self.x_upper = x_upper
    def plotter(self):
        x_values = (range(self.x_lower, self.x_upper + 1))
        y_values = list(map(lambda x: eval(fx), x_values))
       
        return x_values,        y_values,        plt.style.use('seaborn'),        plt.plot(x_values, y_values),        #plt.axis([min(x_values),max(x_values)*1.1,min(y_values),max(y_values)*1.1]),\
        plt.axis([self.x_lower,self.x_upper,min(y_values),max(y_values)*1.1]),        plt.show()

    plot_1 = Plot(fx,x_lower, x_upper) 
plot_1.plotter()


# In[ ]:




