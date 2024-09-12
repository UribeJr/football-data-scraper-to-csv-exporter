#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import modules and packages
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


# In[3]:


#scrape single game shots
base_url = 'https://understat.com/match/'
match = str(input("Enter your match ID: "))
url = base_url + match


# In[16]:


res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')
span = soup.find('span')
script = soup.find_all('script')
script


# In[18]:


string = script[1].string
string


# In[26]:


#strip symbols so we only have json data
index_start = string.index("('") + 2
index_end = string.index("')")

json_data = string[index_start:index_end]
json_data = json_data.encode('utf8').decode('unicode_escape')
data = json.loads(json_data)


# In[35]:


df_h = pd.DataFrame(data['h'])
print("Home Team DataFrame:")
print(df_h.head())


# In[37]:


# Save the home team DataFrame to a CSV file
df_h.to_csv('home_team_shots.csv', index=False)


# In[ ]:




