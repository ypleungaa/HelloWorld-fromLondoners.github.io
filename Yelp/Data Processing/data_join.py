#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


rest = pd.read_csv("restaurants_br.csv")


# In[4]:


dummy_rest = pd.get_dummies(rest,columns=['general_ca'],prefix='gen_cat')


# In[5]:


dummy_rest.head()


# In[6]:


rest_agg = dummy_rest.drop(columns=['OID','FID_1','Field1','category','id','latitude','longitude','FID_2','label','altname','centroid_x','centroid_y'])
br_cate = rest_agg.groupby(['name','code'],as_index=False).sum()
br_cate.head()


# In[32]:


br_cate_rename = br_cate.drop(columns=['gen_cat_ ']).rename(index=str,columns={'gen_cat_African':'African','gen_cat_American':'American','gen_cat_Italian':'Italian','gen_cat_Chinese':'Chinese','gen_cat_European_Other':'European_Other','gen_cat_French':'French','gen_cat_Indian':'Indian','gen_cat_Japanese_Korean':'Japanese_Korean','gen_cat_Latin_American':'Latin_American','gen_cat_Mediterranean':'Mediterranean','gen_cat_Middle_Eastern':'Middle_Eastern','gen_cat_Other':'Other','gen_cat_Pakistani':'Pakistani','gen_cat_Southeast_Asian':'Southeast_Asian'})
br_cate_rename


# In[33]:


max_num = br_cate_rename.max(axis=1)


# In[36]:


br_cate_rename['max_num'] = br_cate_rename.max(axis=1)
br_cate_rename


# In[37]:


columns = list(br_cate_rename)


# In[41]:


def max_cat(row):
    for cat in columns:
        if row[cat] == row['max_num']:
            return cat
br_cate_rename['prev_cat'] = br_cate_rename.apply(max_cat,axis=1)
br_cate_rename


# In[44]:


def num_cat(row):
    count = 0
    for i in range(2,16):
        if row[i] != 0:
            count += 1
    return count
br_cate_rename['num_cat'] = br_cate_rename.apply(num_cat,axis=1)
br_cate_rename


# In[45]:


br_cate_rename.to_csv("borough_category.csv")

