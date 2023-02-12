#!/usr/bin/env python
# coding: utf-8

# # A/B TESTING

# A/B Testing means analyzing two marketing strategies to choose the best marketing strategy that can convert more traffic into sales (or more traffic into your desired goal) effectively and efficiently

# In[1]:


#IMPORT LIBRARIES
import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"


# In[3]:


#LOAD DATASETS
control_data = pd.read_csv("/home/arya/Desktop/PYTHON DATASCIENCE PROJECTS/A|B Testing/control_group.csv", sep = ";")
test_data = pd.read_csv("/home/arya/Desktop/PYTHON DATASCIENCE PROJECTS/A|B Testing/test_group.csv", sep = ";")


# In[4]:


print(control_data.head())


# In[5]:


print(test_data.head())


# ### DATA PREPARATION

# The datasets have some errors in column names. Let’s give new column names

# In[6]:


control_data.columns = ["Campaign Name", "Date", "Amount Spent", 
                        "Number of Impressions", "Reach", "Website Clicks", 
                        "Searches Received", "Content Viewed", "Added to Cart",
                        "Purchases"]


# In[7]:


test_data.columns = ["Campaign Name", "Date", "Amount Spent", 
                        "Number of Impressions", "Reach", "Website Clicks", 
                        "Searches Received", "Content Viewed", "Added to Cart",
                        "Purchases"]


# In[8]:


#TO CHECK NULL VALUES
print(control_data.isnull().sum())


# In[9]:


print(test_data.isnull().sum())


# The dataset of the control campaign has missing values in a row. Let’s fill in these missing values by the mean value of each column:

# In[10]:


control_data["Number of Impressions"].fillna(value=control_data["Number of Impressions"].mean(), 
                                             inplace=True)
control_data["Reach"].fillna(value=control_data["Reach"].mean(), 
                             inplace=True)
control_data["Website Clicks"].fillna(value=control_data["Website Clicks"].mean(), 
                                      inplace=True)
control_data["Searches Received"].fillna(value=control_data["Searches Received"].mean(), 
                                         inplace=True)
control_data["Content Viewed"].fillna(value=control_data["Content Viewed"].mean(), 
                                      inplace=True)
control_data["Added to Cart"].fillna(value=control_data["Added to Cart"].mean(), 
                                     inplace=True)
control_data["Purchases"].fillna(value=control_data["Purchases"].mean(), 
                                 inplace=True)


# In[11]:


#To create a new dataset by merging both datasets:
ab_data = control_data.merge(test_data, 
                             how="outer").sort_values(["Date"])
ab_data = ab_data.reset_index(drop=True)
print(ab_data.head())


# In[12]:


#To check if the dataset has an equal number of samples about both campaigns
print(ab_data["Campaign Name"].value_counts())


# ## A/B Testing to Find the Best Marketing Strategy
#   

# Analyze the relationship between the number of impressions we got from both campaigns and the amount spent on both campaigns:

# In[13]:


figure = px.scatter(data_frame = ab_data, 
                    x="Number of Impressions",
                    y="Amount Spent", 
                    size="Amount Spent", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# The control campaign resulted in more impressions according to the amount spent on both campaigns. 

# The number of searches performed on the website from both campaigns:

# In[15]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(control_data["Searches Received"]), 
          sum(test_data["Searches Received"])]
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Searches')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# The test campaign resulted in more searches on the website

# The number of website clicks from both campaigns:

# In[16]:


label = ["Website Clicks from Control Campaign", 
         "Website Clicks from Test Campaign"]
counts = [sum(control_data["Website Clicks"]), 
          sum(test_data["Website Clicks"])]
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Website Clicks')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# The test campaign wins in the number of website clicks

# The amount of content viewed after reaching the website from both campaigns:

# In[17]:


label = ["Content Viewed from Control Campaign", 
         "Content Viewed from Test Campaign"]
counts = [sum(control_data["Content Viewed"]), 
          sum(test_data["Content Viewed"])]
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Content Viewed')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# The audience of the control campaign viewed more content than the test campaign. Although there is not much difference, as the website clicks of the control campaign were low, its engagement on the website is higher than the test campaign.
# 
# 

# The number of products added to the cart from both campaigns:

# In[18]:


label = ["Products Added to Cart from Control Campaign", 
         "Products Added to Cart from Test Campaign"]
counts = [sum(control_data["Added to Cart"]), 
          sum(test_data["Added to Cart"])]
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Added to Cart')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# Despite low website clicks more products were added to the cart from the control campaign.

# The amount spent on both campaigns:

# In[20]:


label = ["Amount Spent in Control Campaign", 
         "Amount Spent in Test Campaign"]
counts = [sum(control_data["Amount Spent"]), 
          sum(test_data["Amount Spent"])]
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Amount Spent')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# The amount spent on the test campaign is higher than the control campaign. But as we can see that the control campaign resulted in more content views and more products in the cart, the control campaign is more efficient than the test campaign.

# The purchases made by both campaigns:

# In[22]:


label = ["Purchases Made by Control Campaign", 
         "Purchases Made by Test Campaign"]
counts = [sum(control_data["Purchases"]), 
          sum(test_data["Purchases"])]
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Purchases')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# There’s only a difference of around 1% in the purchases made from both ad campaigns. As the Control campaign resulted in more sales in less amount spent on marketing, the control campaign wins here!

# ### Metrics to find which ad campaign converts more

#  The relationship between the number of website clicks and content viewed from both campaigns:

# In[23]:


figure = px.scatter(data_frame = ab_data, 
                    x="Content Viewed",
                    y="Website Clicks", 
                    size="Website Clicks", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# The website clicks are higher in the test campaign, but the engagement from website clicks is higher in the control campaign. So the control campaign wins!
# 
# 

# The relationship between the amount of content viewed and the number of products added to the cart from both campaigns:

# In[24]:


figure = px.scatter(data_frame = ab_data, 
                    x="Added to Cart",
                    y="Content Viewed", 
                    size="Added to Cart", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# Again, the control campaign wins! 

# The relationship between the number of products added to the cart and the number of sales from both campaigns:

# In[25]:


figure = px.scatter(data_frame = ab_data, 
                    x="Purchases",
                    y="Added to Cart", 
                    size="Purchases", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# Although the control campaign resulted in more sales and more products in the cart, the conversation rate of the test campaign is higher.

# ## CONCLUSION 

# From the above A/B tests, we found that:
# 1. The control campaign resulted in more sales and engagement from the visitors. More products were viewed from the control campaign, resulting in more products in the cart and more sales. 
# 2. The conversation rate of products in the cart is higher in the test campaign. 
# 3. The test campaign resulted in more sales according to the products viewed and added to the cart.
# 4. The control campaign results in more sales overall. 
# 
# So, the Test campaign can be used to market a specific product to a specific audience, and the Control campaign can be used to market multiple products to a wider audience.
# 
# 

# In[ ]:




