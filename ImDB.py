#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[52]:


df=pd.read_csv("C:/Users/DELL/Desktop/movie.csv")


# In[53]:


df.head()


# In[54]:


df.info()


# In[55]:


df.describe()


# In[56]:


df["Revenue (Millions)"].fillna(df["Revenue (Millions)"].mean(),inplace=True)
df["Revenue (Millions)"].tail()


# In[57]:


df.info()


# In[58]:


df[df["Revenue (Millions)"]<1]


# In[59]:


df.drop((df[df['Revenue (Millions)']<1]).index,inplace =True)


# In[60]:


df.shape


# In[61]:


print("Number of movies released in particulat year ")
df["Year"].value_counts()


# In[62]:


import seaborn as sns
sns.countplot(x=df["Year"],data=df)


# In[63]:


plt.subplot(2,2,1)
sns.scatterplot(y=df["Revenue (Millions)"],x=df["Votes"],color="Orange")
plt.title("Revenue v/s votes")

plt.subplot(2,2,2)
sns.countplot(x=df["Year"],data=df)
plt.xticks(rotation=45)


plt.subplot(2,2,3)
sns.barplot(x=df["Year"],y=df["Revenue (Millions)"],data=df)
plt.xticks(rotation=45)

plt.subplot(2,2,4)
sns.histplot(x='Runtime (Minutes)',data=df);
plt.title('No.of movies as per their runtime');

plt.tight_layout(pad=1.08)





# In[64]:


#rating greater than 8
df[df["Rating"]>8.0]


# In[65]:


#sorting by rating and finding top rating
df.sort_values(by=["Rating"],ascending=False).head(1)


# In[69]:


#max rating
df[df["Rating"].max()==df["Rating"]]


# In[70]:


#least rating movie
df[df["Rating"].min()==df["Rating"]]


# In[71]:


#least revenue collected
df[df["Revenue (Millions)"].min()==df["Revenue (Millions)"]]


# In[72]:


#highest revenue collected movie
df[df["Revenue (Millions)"].max()==df["Revenue (Millions)"]]


# In[73]:


#movies with metascore greater than 95
df[['Rank','Title','Votes','Genre']].loc[df['Metascore']>95


# In[79]:


df[["Rank","Title","Votes","Genre","Rating"]].loc[df["Rating"]>8.5]


# In[94]:


#top 5 movies 
df.head()
top_movie=df.sort_values(by=["Revenue (Millions)"],ascending=False).head(5)
top_movie


# In[93]:


sns.barplot(y="Revenue (Millions)",x="Director",data=top_movie)
plt.xticks(rotation=45)


# In[96]:


df.head()
df.groupby("Director")["Revenue (Millions)"].sum()


# In[100]:


df1=pd.read_csv("C:/Users/DELL/Desktop/movie.csv")


# In[101]:


print("Number of movies released in particulat year ")
df1["Year"].value_counts()


# In[ ]:




