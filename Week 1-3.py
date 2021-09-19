
# coding: utf-8

# # DataFrame

# In[6]:


#import the packages "Pandas" and "MatPlotLib" into Jupyter Notebook
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[7]:


fb = pd.DataFrame.from_csv('../data/facebook.csv')
ms = pd.DataFrame.from_csv('../data/microsoft.csv')


# In[8]:


fb['Price1'] = fb['Close'].shift(-1) # 1영업일 이전 종가 리스트


# In[9]:


print(fb.head())


# In[12]:


fb['PriceDiff'] = fb['Price1'] - fb['Close']
fb.head()


# In[14]:


fb['Return'] = fb['PriceDiff'] / fb['Close'] # 증감률 


# In[15]:


fb.head()


# In[16]:


fb['Direction'] = [1 if fb.loc[ei, 'PriceDiff'] > 0 else -1 for ei in fb.index]
fb.head()  ## 주가 방향성 


# In[17]:


fb['Average3'] = (fb['Close'] + fb['Close'].shift(1) + fb['Close'].shift(2))/3
fb.head() 


# In[18]:


fb['MA40'] = fb['Close'].rolling(40).mean()
fb['MA200'] = fb['Close'].rolling(200).mean()
fb.head() 


# In[19]:


fb['Close'].plot()
fb['MA40'].plot()
fb['MA200'].plot()


# In[20]:


print(fb.head())


# In[21]:


fb.shape


# In[22]:


fb.tail()


# In[23]:


fb.loc['2015-01-02', 'Close']


# In[24]:


fb.loc['2015-01-01':'2015-12-31','Close']


# In[25]:


fb.iloc[624: , :]


# In[26]:


fb.loc['2015-01-01':'2015-12-31', 'Close'].plot()


# In[27]:


#It is your turn to import Microsoft's stock data - "microsoft.csv", which is located in the same folder of facebook.csv
#Replace "None" with your code
ms = None


# In[28]:


# print head of ms, 1 line


# ** Expected Output: **

# <tr>
#     <th>Date</th>
#     <th>Open</th>  
#     <th>High</th>
#     <th>Low</th>
#     <th>Close</th>
#     <th>Adj Close</th>
#     <th>Volume</th>
# </tr>
# <tr>
#     <td>2014-12-31</td>
#     <td>46.730000</td>  
#     <td>47.439999</td>
#     <td>46.450001</td>
#     <td>46.450001</td>
#     <td>42.848763</td>
#     <td>21552500</td>
# </tr>
# <tr>
#     <td>2015-01-02</td>
#     <td>46.660000</td>  
#     <td>47.419998</td>
#     <td>46.540001</td>
#     <td>46.759998</td>
#     <td>43.134731</td>
#     <td>27913900</td>
# </tr>
# <tr>
#     <td>2015-01-05</td>
#     <td>46.369999</td>  
#     <td>46.730000</td>
#     <td>46.250000</td>
#     <td>46.330002</td>
#     <td>42.738068</td>
#     <td>39673900</td>
# </tr>
# <tr>
#     <td>2015-01-06</td>
#     <td>46.380001</td>  
#     <td>46.750000</td>
#     <td>45.540001</td>
#     <td>45.650002</td>
#     <td>42.110783</td>
#     <td>36447900</td>
# </tr>
# <tr>
#     <td>2015-01-07</td>
#     <td>45.980000</td>  
#     <td>46.459999</td>
#     <td>45.490002</td>
#     <td>46.230000</td>
#     <td>42.645817</td>
#     <td>29114100</td>
# </tr>
# 

# ## Show the size of a DataFrame using "Shape"

# In[6]:


print(fb.shape)


# In[7]:


# print the shape of ms, 1 line


# ## Show summary statistics of a DataFrame

# In[29]:


# print summary statistics of Facebook
print(fb.describe())


# ## Locate a particular row of data using "Selection by label"

# In[30]:


# select all the price information of Facebook in 2016.
fb_2015 = fb.loc['2015-01-01':'2015-12-31']


# In[31]:


# print the price of Facebook on '2015-03-16'
print(fb_2015.loc['2015-03-16'])


# ## Locate a particular row of data using "Selection by position"

# In[33]:


# print the opening price of the first row
print(fb.iloc[0, 0])


# ## Plot the stock data using plot() method

# In[35]:


plt.figure(figsize=(10, 8))
fb['Close'].plot()
plt.show()

