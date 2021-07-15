#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data)
df.to_csv('Df.csv')
d=pd.read_csv('Df.csv')
d.head(3)
df.drop(['name', 'qualify'], axis=1)
df.iloc[:, 0:2]
k = {'name' : "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}
df = df.append(k, ignore_index=True)
df.drop("attempts", axis=1)
df.insert(-1, "Success", [1, 0, 1, np.nan,0,1,1,np.nan,0,1], True)
df
  


# In[16]:


import pandas as pd
name=['Anastasia', 'Dima', 'Katherine', 'James']
age = [20,15,6,19]
S=pd.Series(age, index=name)
S


# In[17]:


import pandas as pd
color=["pink", "white", "black", "blue"]
S1=pd.Series([20, 15, 6, 43], index=color)
S2=pd.Series([3, 22, 9, 10], index=color)
print(S1+S2)


# In[18]:


import pandas as pd
list = [['Jack', 34, 'Paris'], ['Thomas', 30, 'Roma'], 
       ['Alexandre', 16, 'New York']] 
df = pd.DataFrame(list, columns =['name', 'age', 'city'])
df


# In[20]:


dictionary  = { 'name' : ['Jack', 'Thomas', 'Alexandre'],
    'age' : [34, 30, 16],
    'city' : ['Paris', 'Roma', 'New York']}

df = pd.DataFrame(dictionary)
df


# In[39]:


import numpy as np
import pandas as pd
list=['Jack', 34, 'Paris']
my_numpy_array=np.random.randn(3,4)
df=pd.DataFrame(my_numpy_array, columns=["a","b","c","d"])
df.drop("b", axis=1)


# In[ ]:




