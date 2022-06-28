#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as  pd
import matplotlib.pyplot as plt


# In[58]:


df = pd.read_csv('F:\menu.csv')


# In[59]:


df.head(5)


# In[60]:


df.describe()


# In[61]:


df.dtypes


# In[62]:


df.shape


# In[63]:


df.tail()


# In[64]:


df.notnull().head(10)


# In[65]:


df['Category'].unique()


# In[66]:


df['Category'].value_counts().plot(kind='bar')


# # Coffee and Tea category contains higest numbers of items

# In[67]:


df['Item'].unique()


# In[68]:


df.iloc[130:135]


# In[69]:


## GOAL: Show the most healthy menu items at McDonald's by identifying:

Menu items that have the least saturated fat.
Menu items that have the least sodium.
Menu items that have the least sugar.
Menu items that have the most dietary fiber.
Menu items that have the least saturated fats, sodium, and sugar overall.


# # 1. Which menu items have the least saturated fat?

# ## A. Saturated fat by category

# In[70]:


df.columns


# In[71]:


categories_by_saturated_fat = df[['Category','Saturated Fat']].groupby('Category').sum().sort_values('Saturated Fat', ascending = True)

categories_by_saturated_fat.plot(kind = 'barh', figsize = (12,8))

plt.title('Saturated Fat [grams] by Category')
plt.xlabel('Saturated Fat [grams]')


# ## B. Top 10 Menu Items With The Least Saturated Fat

# In[72]:


items_by_saturated_fat = df[['Item','Saturated Fat']].groupby('Item').sum().sort_values(['Saturated Fat','Item'], ascending=True).head(70)
items_by_saturated_fat
items_by_saturated_fat.plot(kind='bar',figsize=(21,8))

plt.ylabel('Saturated Fat [in grams]')
plt.title('Saturated Fat [in grams] by Item')


# # 2. Which menu items have the least sodium?

# ## A. Sodium by Category 

# In[85]:


categories_by_sodium = df[['Category','Sodium']].groupby('Category').sum().sort_values('Sodium', ascending=True).head(70)
categories_by_sodium

categories_by_sodium.plot(kind='barh', figsize=(11,6))

plt.xlabel('Sodium [mg]')
plt.title('Sodium [mg] by category')


# ## B. Top 10 Menu Items With The Least Sodium

# In[88]:


items_by_Sodium = df[['Item','Sodium']].groupby('Item').sum().sort_values('Sodium', ascending=True).head(10)
items_by_Sodium


# In[97]:


items_by_Sodium = df[['Item','Sodium']].groupby('Item').sum().sort_values('Sodium', ascending=True).head(20)
items_by_Sodium
items_by_Sodium.plot(kind='bar', figsize=(21,8))
plt.xlabel('Items',size=20)
plt.ylabel('Sodium [mg]',size=20)
plt.title('Sodium [mg] by Item',size=30)


# # 3. Which menu items have the least sugars?

# ## A. Sugars By Category

# In[99]:


categories_by_sugar = df[['Category','Sugars']].groupby('Category').sum().sort_values('Sugars', ascending=True).head(70)
categories_by_sugar

categories_by_sugar.plot(kind='barh', figsize=(11,6))
plt.xlabel('Sugar[gram]')
plt.title('Sugars [gram] by Category')


# ## B. Top 10 Menu Items With The Least Sugars

# In[101]:


items_by_sugars = df[ ['Item', 'Sugars'] ]                            .groupby('Item')                            .sum()                            .sort_values(['Sugars', 'Item'], ascending=True)                            .head(10)

items_by_sugars


# In[102]:


items_by_sugars = df[ ['Item', 'Sugars'] ]                            .groupby('Item')                            .sum()                            .sort_values(['Sugars', 'Item'], ascending=True)                            .head(80)

items_by_sugars

items_by_sugars.plot(kind='bar', figsize=(21,7))

plt.ylabel('Sugars [in grams]')
plt.title('Sugars [in grams] by Item');


# # 4. Which menu items have the most dietary fiber?

# ## A. Dietary Fiber By Category

# In[105]:


categories_by_dietary_fiber = df[ ['Category', 'Dietary Fiber'] ]                            .groupby('Category')                            .sum()                            .sort_values('Dietary Fiber', ascending=True)                            .head(70)

categories_by_dietary_fiber

categories_by_dietary_fiber.plot(kind='barh', figsize=(11,6))

plt.xlabel('Dietary Fiber [[in grams]')
plt.title('Dietary Fiber [[in grams] by Category');


# ## B. Top 10 Menu Items With The Most Dietary Fiber

# In[107]:


items_by_dietary_fiber = df[ ['Item', 'Dietary Fiber'] ]                            .groupby('Item')                            .sum()                            .sort_values(['Dietary Fiber', 'Item'], ascending=False)                            .head(10)

items_by_dietary_fiber


# In[108]:


items_by_dietary_fiber = df[ ['Item', 'Dietary Fiber'] ]                            .groupby('Item')                            .sum()                            .sort_values(['Dietary Fiber', 'Item'], ascending=False)                            .head(80)

items_by_dietary_fiber

items_by_dietary_fiber.plot(kind='bar', figsize=(21,7))

plt.ylabel('Dietary Fiber [[in grams]')
plt.title('Dietary Fiber [[in grams] by Item');


# # 5. Which menu items have the least saturated fats, sodium, and sugar overall?

# In[109]:


items_by_satfat_sod_sugar_dietf = df[ ['Item','Saturated Fat', 'Sodium', 'Sugars', 'Dietary Fiber'] ]                            .groupby('Item')                            .sum()                            .sort_values(['Sodium', 'Sugars','Saturated Fat', 'Item'], ascending=True)                            .head(30)

items_by_satfat_sod_sugar_dietf


# ## Beverages have the least saturated fat. Apple slices is the only food item without sodium.
