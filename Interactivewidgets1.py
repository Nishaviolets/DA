#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ipywidgets')


# In[2]:


get_ipython().system('jupyter nbextension enable --py widgetsnbextension --sys-prefix')


# In[3]:


import ipywidgets as widgets
w = widgets.IntSlider(value = 10,
                     min=-5,
                     max=20,
                     step=1,
                     description='Range slider:',
                     continuous_update=False,
                     orientation='horizontal')


# In[4]:


w


# In[5]:


w.value


# In[6]:


type(w)


# In[7]:


r = widgets.IntRangeSlider(value =[10,1000],
                     min=0,
                     max=10000,
                     step=1,
                     description='Price range:',
                     orientation='horizontal')


# In[8]:


r


# In[9]:


r.value


# In[10]:


p=widgets.IntProgress(value=70,
                     min=0,
                     max=100,
                     step=1,
                     description='Loading:',
                     bar_style='success',
                     orientation='horizontal')


# In[11]:


p


# In[12]:


import time

for i in range(0,110,10):
    p.value = i
    
    time.sleep(i)


# In[13]:


widgets.BoundedIntText(value=5,
                      min=0,
                      max=100,
                      step=1,
                      description='Text:',
                      disabled=False)


# In[14]:


widgets.Checkbox(value=False,
                description='Check me')


# In[15]:


dd = widgets.Dropdown(options=['None','0','1','2','3'],
                     value='None',
                     description='Number:',
                     disabled=False)


# In[16]:


dd


# In[17]:


dd.value


# In[18]:


rb = widgets.RadioButtons(options=['None','MacBook Pro','MacBook Air',
                                  'Notebook','Lenovo','Dell','HP'],
                         value='None',
                         description='Laptop choice')


# In[19]:


rb


# In[20]:


rb.value


# In[21]:


button= widgets.Button(description='Happiness Button',
                      button_style='success',
                      tooltip='Good things will happen:-)',
                      icon='Check')
                     


# In[22]:


def button_click_event_handler(button):
    print('You clicked! Good things are about to happen!')
    
    print(button.description)


# In[23]:


button.on_click(button_click_event_handler)


# In[24]:


button


# In[25]:


play = widgets.Play(value=50,
                   min=0,
                   max=100,
                   step=1,
                   description="Press Play")
slider=widgets.IntSlider()
widgets.jslink((play,'value'),(slider,'value'))
widgets.HBox([play,slider])


# In[26]:


#adding interactivity to functions


# In[27]:


def f(x):
    return x


# In[28]:


interact(f,x=10);


# In[ ]:


interact(f,x=True);


# In[ ]:


interact(f,x='Hello, widgets');


# In[ ]:


@interact(x=True, y=5.0)
def g(x,y):
    return(x,y)


# In[ ]:


def h(p,q):
    return(p,q)


# In[ ]:


interact(h,p=5,q=fixed(20))


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


def f(m,b):
    plt.figure(2)
    
    x=np.linspace(-10,10,num=1000)
    
    plt.plot(x, m*x+b)
    plt.ylim(-5,5)
    plt.show()
    
interactive_plot = interactive(f,m=(-2.0,2.0),b=(-3,3,0.5))


# In[ ]:


output=interactive_plot.children[-1]
output.layout.height = '350px'
interactive_plot


# In[ ]:


from IPython.display import display
text=widgets.Text()
display(text)
def make_upper_case(input_text):
    text.value=input_text.value.upper()
    print(text.value)
    
text.on_submit(make_upper_case)    


# In[ ]:


import os
from IPython.display import Image
fidr='datasets/Nature/'
@interact
def show_images(file=os.listdir(fdir)):
    display(Image(fdir + file))


# In[ ]:




