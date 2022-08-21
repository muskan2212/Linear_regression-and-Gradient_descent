#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


def grad_des(x,y):
    m_curr=b_curr=0
    iteration=1000
    l_r=0.0001
    n=len(x)
    for i in range(iteration):
        y_pred=m_curr*l_r + b_curr
        cost = 1/n*sum([val**2 for val in (y-y_pred)])
        
        m_der = -1/n*sum(x*(y-y_pred))
        b_der = -1/n*sum(y-y_pred)
        
        m_curr= m_curr-m_der*l_r
        b_curr= b_curr-b_der*l_r
        
        print ("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost, i))
        
        
    


# In[7]:


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

grad_des(x,y)


# In[10]:


plt.scatter(x,y)


# In[ ]:




