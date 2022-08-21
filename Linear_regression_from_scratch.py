#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


def coeff(x, y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    
    n=np.size(x)
    
    #cross deviation and deviation about x
    s_xy=np.sum(x*y)-n*x_mean*y_mean
    s_xx=np.sum(x*x)-n*x_mean*x_mean
    
    b1=s_xy / s_xx
    b2=y_mean - b1*x_mean
     
    return (b1, b2)


# In[21]:


def plot_reg_line(x,y,b):
    plt.scatter(x,y)
    
    y_pred=b[0]+b[1]*x
    
    #plotting regression line
    plt.plot(x,y_pred)
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()
    


# In[22]:


def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    
    b=coeff(x, y)
    
    plot_reg_line(x,y,b)
    
    


# In[23]:


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




