
# coding: utf-8

# Drop the other column region except 

# In[78]:


#Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read data/
df = pd.read_excel('C:/Users/Andy/Desktop/Project/Worldbank data/World_bank_data_region_edited.xlsx')


# # Data Exploration
# Let's do some basic inspection here

# In[79]:


df.shape


# It seems like a extremely little dataset

# In[80]:


df.head()


# The coulmns show different aspect on country. Like economy, environment, education or even women right. I would divde them by each category to do analysis. Because some of them don't have strong connection and it's hard to analyze if I put them together.

# In[81]:


df.dtypes


# In[82]:


df.info()


# In[83]:


df.describe()


# # Missing value

# In[84]:


df.isnull().sum()


# I would want to drop the column "adult_literacy_pct" cuz they are 14 missing value out of 22 country. Even we did analysis on it, it cannot reflect most of country's situation.

# In[85]:


df.drop(columns = 'adult_literacy_pct')


# ### Category analysis
# Let us group each column into different category first

# ### Economic(income_group,access_to_electricity_pop,urban,rural)

# In[86]:


df.income_group.value_counts()


# Let us see who has lower middle income

# In[87]:


df['income_group'].str.contains("Lower middle income")


# In[88]:


df.iloc[15]


# In[89]:


df.iloc[20]


# El Salvador & Bolivia has lower income than the other country

# In[90]:


df[df["access_to_electricity_pop"]<90]


# In[91]:


df[df["access_to_electricity_rural"]<90]


# Even they have lower income, both countries have pretty high electricity access to pop!!

# In[92]:


df[df["access_to_electricity_urban"]<90]


# There is my logic and assumption:High income=>High GDP=>High electricity rate.
# High income country, St.Martin has the lowest elevtricity percentage!?? Which is not make any sense

# Now we can assume income and electricity accessible do not have positive correlation, let us see the line chart

# In[93]:


plt.title('Ecnomic elemets correlation')
plt.ylabel('access to electricity%')
plt.scatter(df['income_group'], df["access_to_electricity_pop"])
plt.show()


# In[94]:


df.groupby('income_group')['access_to_electricity_pop'].mean()


# Lower middle class average electricity% achieve 92%. Upper middle income even over than High income electricity percentage. In sum, there are no clear correlations between income_group V.S access_to_electricity_pop

# In[95]:


df.fillna(0)


# # CO2_emissions_per_capita)

# In[108]:


import warnings
warnings.filterwarnings("ignore")


# In[131]:


plt.title('CO2_emissions_per_capita)')
plt.hist(df['CO2_emissions_per_capita)'],bins=20,range=(1,35),color='blue')
plt.show()


# There are two countries having higher CO2 emissions per capita

# In[113]:


df[df['CO2_emissions_per_capita)']>10]


# They are Sint Maarten (Dutch part) & Trinidad and Tobago	

# # compulsory_edu_yrs

# In[120]:


plt.title('compulsory_edu_yrs')
plt.hist(df['compulsory_edu_yrs'],bins=20,range=(1,20),color='blue')
plt.show()


# It's clear to say most compulsory education years are range from 10-15 years. But there are three outliers less than 7.5

# In[121]:


df[df['compulsory_edu_yrs']<10]


# Suriname,Trinidad and Tobago and Guyana have lower compulsory_edu_yrs.

# ### Internet_usage_pct	

# In[123]:


plt.title('internet_usage_pct')
plt.hist(df['internet_usage_pct'],bins=20,range=(1,100),color='blue')
plt.show()


# In[125]:


df[df['internet_usage_pct']<40]


# Those 4 countries:St. Lucia, El Salvador, Guyana and Bolivia internet usage pct are pretty low

# ### Homicides_per_100k	

# In[130]:


plt.title('homicides_per_100k')
plt.hist(df['homicides_per_100k'],bins=10,range=(1,80),color='blue')
plt.show()


# In[129]:


df[df['homicides_per_100k']>60]


# Two countries have extremly high homicides rate out of 100 who died, Venezuela and El Salvador 

# ### Adult_literacy_pct	

# In[136]:


plt.title('Adult_literacy_pct')
plt.hist(df['adult_literacy_pct'],bins=10,range=(50,100),color='blue')
plt.show()


# In[138]:


df[df['adult_literacy_pct']<90]


# Guyana	has the least adult_literacy_pct but they are not far away from the majority

# ### Child_mortality_per_1k	

# In[141]:


plt.title('Child_mortality_per_1k')
plt.hist(df['child_mortality_per_1k'],bins=20,range=(1,50),color='blue')
plt.show()


# In[142]:


df[df['child_mortality_per_1k']>30]


# Dominica,Guyana and Bolivia	 "child_mortality_per_1k" more than 3%

# # Avg_air_pollution

# In[144]:


plt.title('Avg_air_pollution')
plt.hist(df['avg_air_pollution'],bins=20,range=(1,50),color='blue')
plt.show()


# In[145]:


df[df['avg_air_pollution']>30]


# El Salvador has high air pollution

# ### Women_in_parliament	

# In[146]:


plt.title('Women_in_parliament')
plt.hist(df['women_in_parliament'],bins=20,range=(1,100),color='blue')
plt.show()


# In[147]:


df[df['women_in_parliament']>50]


# Bolivia	has the most percentage women in parliament rate

# ### Tax_revenue_pct_gdp	

# In[148]:


plt.title('Tax_revenue_pct_gdp')
plt.hist(df['tax_revenue_pct_gdp'],bins=20,range=(1,100),color='blue')
plt.show()


# In[151]:


df[df['tax_revenue_pct_gdp']>20]


# Trinidad and Tobago has the highest 'tax_revenue_pct_gdp'

# # Unemployment_pct

# In[153]:


plt.title('Unemployment_pct')
plt.hist(df['unemployment_pct'],bins=20,range=(1,50),color='blue')
plt.show()


# In[154]:


df[df['unemployment_pct']>20]


# St. Lucia has the highest unemployment rate

# # Urban_population_pct & urban_population_growth_pct

# In[162]:


plt.title('Urban_population_pct')
plt.hist(df['urban_population_pct'],bins=20,range=(1,100),color='blue')
plt.show()

plt.title('urban_population_growth_pct')
plt.hist(df['urban_population_growth_pct'],bins=20,range=(1,5),color='blue')
plt.show()


# In[164]:


df[df['urban_population_pct']<40]


# In[165]:


df[df['urban_population_pct']>80]


# In[163]:


df[df['urban_population_growth_pct']>2.5]


# Sint Maarten (Dutch part) have 100% "urban_population_pct" 
# 

# "urban_population_growth_pct" is also the largest. 
