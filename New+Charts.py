
# coding: utf-8

# In[18]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
import os
os.chdir('/home/ankushraut/Downloads/Thirio')
plt.style.use('ggplot')
get_ipython().magic('matplotlib inline')

wholesome = int(input("Enter 1 for global analysis or 0 for specific analysis : "))


# In[19]:

data = pd.read_csv('Dataset.csv')


# In[20]:

data.head()


# In[21]:

data.describe()


# In[22]:

unique_dates = data.Date.unique()


# In[23]:

uniqueness = []
for i in range(len(unique_dates)):
    uniqueness.append(unique_dates[i])


# In[24]:

data['Date'] = pd.to_datetime(data['Date'])


# In[25]:

data['month'] = data['Date'].dt.month
data['week'] = data['Date'].dt.week
data['day'] = data['Date'].dt.day
data['year'] = data['Date'].dt.year


# In[26]:

order_distance = []
for i in range(len(data)):
    order_distance.append(abs(data['Arrival Latitude'][i]-data['Departure Latitude'][i])+abs(data['Arrival Longitude'][i]-data['Departure Longitude'][i]))

data['Order Distance'] = pd.DataFrame({'Order Distance':order_distance})


# In[27]:

if wholesome == 0:
    desired_year = input("Enter the desired year to check: ")
    desired_month = input("Enter the desired month to check: ")
    desired_week = input("Enter the desired week to check: ")
    desired_day = input("Enter the desired day of the month to check: ")
    desired_date = input("Or enter the exact date in standard format: ")


# In[28]:

if wholesome == 0:
    if desired_year == '' and desired_date != '':
        desired_year = desired_date[:4]
    if desired_month == '' and desired_date != '':
        desired_month = desired_date[5:7]
    if desired_day == '' and desired_date != '':
        desired_day = desired_date[8:]
    if desired_week == '' and desired_date != '':
        if int(desired_day)<=7:
            desired_week = '1'
        elif int(desired_day)>=8 and int(desired_day)<=14:
            desired_week = '2'
        elif int(desired_day)>=15 and int(desired_day)<=21:
            desired_week = '3'
        elif int(desired_day)>=22 and int(desired_day)<=28:
            desired_week = '4'
        else:
            desired_week = '5'


# In[29]:

if wholesome == 0:
    yearly_data = data[(data.year == int(desired_year))]
    monthly_data = yearly_data[(yearly_data.month == int(desired_month))]
    weekly_data = monthly_data[(monthly_data.day>=((int(desired_week)-1)*7 + 1))&(monthly_data.day<=((int(desired_week)-1)*7 + 8))]
    daily_data = monthly_data[(monthly_data.day == int(desired_day))]


# In[30]:

#Sex based pointplot of tickt size vs order distance
if wholesome == 1:
    sns.set(style="whitegrid", color_codes=True)
    plt.figure(figsize = (12,8))
    sns.pointplot(x=data['Ticket Size'], y=data['Order Distance'], hue = data['Sex'], palette={"M": "r", "F": "g"},
                  markers=["^", "o"], linestyles=["-", "--"])
    plt.title('Pointplot of Order distance vs Ticket Size (with confidence interval)')
    plt.show()
else:
    plt.figure(figsize = (12,8))
    sns.pointplot(x=yearly_data['Ticket Size'], y=yearly_data['Order Distance'], hue = yearly_data['Sex'], palette={"M": "r", "F": "g"},
                  markers=["^", "o"], linestyles=["-", "--"])
    plt.title('Pointplot of Order distance vs Ticket Size (yearly)')
    plt.show()
    
    plt.figure(figsize = (12,8))
    sns.pointplot(x=monthly_data['Ticket Size'], y=monthly_data['Order Distance'], hue = monthly_data['Sex'], palette={"M": "r", "F": "g"},
                  markers=["^", "o"], linestyles=["-", "--"])
    plt.title('Pointplot of Order distance vs Ticket Size (monthly)')
    plt.show()
    
    plt.figure(figsize = (12,8))
    sns.pointplot(x=weekly_data['Ticket Size'], y=weekly_data['Order Distance'], hue = weekly_data['Sex'], palette={"M": "r", "F": "g"},
                  markers=["^", "o"], linestyles=["-", "--"])
    plt.title('Pointplot of Order distance vs Ticket Size (weekly)')
    plt.show()
    
    plt.figure(figsize = (12,8))
    sns.pointplot(x=daily_data['Ticket Size'], y=daily_data['Order Distance'], hue = daily_data['Sex'], palette={"M": "r", "F": "g"},
                  markers=["^", "o"], linestyles=["-", "--"])
    plt.title('Pointplot of Order distance vs Ticket Size (daily)')
    plt.show()


# In[31]:

#daily basis barplot of ticket size vs order distance
if wholesome == 1:
    plt.figure(figsize = (20,15))
    sns.barplot(x=data['Ticket Size'], y=data['Order Distance'], hue = data['Day'])
    plt.title('Barplot of Order distance vs Ticket Size')
    plt.show()
else:
    plt.figure(figsize = (20,15))
    sns.barplot(x=yearly_data['Ticket Size'], y=yearly_data['Order Distance'], hue = yearly_data['Day'])
    plt.title('Barplot of Order distance vs Ticket Size (yearly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=monthly_data['Ticket Size'], y=monthly_data['Order Distance'], hue = monthly_data['Day'])
    plt.title('Barplot of Order distance vs Ticket Size (monthly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=weekly_data['Ticket Size'], y=weekly_data['Order Distance'], hue = weekly_data['Day'])
    plt.title('Barplot of Order distance vs Ticket Size (weekly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=daily_data['Ticket Size'], y=daily_data['Order Distance'], hue = daily_data['Day'])
    plt.title('Barplot of Order distance vs Ticket Size (daily)')
    plt.show()


# In[32]:

#Slab based boxplot of ticket size vs order distance
if wholesome == 1:
    plt.figure(figsize = (14,10))
    sns.pointplot(x=data['Ticket Size'], y=data['Order Distance'], hue = data['Slab'])
    plt.title('Box plot of Order distance vs Ticket Size')
    plt.show()
else:
    plt.figure(figsize = (14,10))
    sns.pointplot(x=yearly_data['Ticket Size'], y=yearly_data['Order Distance'], hue = yearly_data['Slab'])
    plt.title('Box plot of Order distance vs Ticket Size (yearly)')
    plt.show()
    
    plt.figure(figsize = (14,10))
    sns.pointplot(x=monthly_data['Ticket Size'], y=monthly_data['Order Distance'], hue = monthly_data['Slab'])
    plt.title('Box plot of Order distance vs Ticket Size (monthly)')
    plt.show()
    
    plt.figure(figsize = (14,10))
    sns.pointplot(x=weekly_data['Ticket Size'], y=weekly_data['Order Distance'], hue = weekly_data['Slab'])
    plt.title('Box plot of Order distance vs Ticket Size (weekly)')
    plt.show()
    
    plt.figure(figsize = (14,10))
    sns.pointplot(x=daily_data['Ticket Size'], y=daily_data['Order Distance'], hue = daily_data['Slab'])
    plt.title('Box plot of Order distance vs Ticket Size (daily)')
    plt.show()


# In[33]:

#simple countplot of ticket size
if wholesome == 1:
    plt.figure(figsize = (12,8))
    sns.countplot(x=data['Ticket Size'], hue=data['Sex'])
    plt.title('Countplot of ticket size')
    plt.show()
else:
    plt.figure(figsize = (12,8))
    sns.countplot(x=yearly_data['Ticket Size'], hue=yearly_data['Sex'])
    plt.title('Countplot of ticket size (yearly)')
    plt.show()
    
    plt.figure(figsize = (12,8))
    sns.countplot(x=monthly_data['Ticket Size'], hue=monthly_data['Sex'])
    plt.title('Countplot of ticket size (monthly)')
    plt.show()
    
    plt.figure(figsize = (12,8))
    sns.countplot(x=weekly_data['Ticket Size'], hue=weekly_data['Sex'])
    plt.title('Countplot of ticket size (weekly)')
    plt.show()
    
    plt.figure(figsize = (12,8))
    sns.countplot(x=daily_data['Ticket Size'], hue=daily_data['Sex'])
    plt.title('Countplot of ticket size (daily)')
    plt.show()


# In[34]:

#Violinplot of order window vs ticket size
if wholesome == 1:
    plt.figure(figsize = (12,8))
    sns.violinplot(data['Ticket Size'], data['Window'], hue = data['Sex'], split = True)
    plt.title('Violin plot for order window vs ticket size')
    plt.show()
else:
    plt.figure(figsize = (12,8))
    sns.violinplot(yearly_data['Ticket Size'], yearly_data['Window'], hue = yearly_data['Sex'], split = True, palette = 'pastel')
    plt.title('Violin plot for order window vs ticket size (yearly)')
    plt.show()

    plt.figure(figsize = (12,8))
    sns.violinplot(monthly_data['Ticket Size'], monthly_data['Window'], hue = monthly_data['Sex'], split = True, palette = 'pastel')
    plt.title('Violin plot for order window vs ticket size (monthly)')
    plt.show()

    plt.figure(figsize = (12,8))
    sns.violinplot(weekly_data['Ticket Size'], weekly_data['Window'], hue = weekly_data['Sex'], split = True, palette = 'pastel')
    plt.title('Violin plot for order window vs ticket size (weekly)')
    plt.show()

    plt.figure(figsize = (12,8))
    sns.violinplot(daily_data['Ticket Size'], daily_data['Window'], hue = daily_data['Sex'], split=True, palette = 'pastel')
    plt.title('Violin plot for order window vs ticket size (daily)')
    plt.show()


# In[35]:

#boxplot for order window vs ticket size
if wholesome == 1:
    plt.figure(figsize = (12,8))
    sns.boxplot(data['Ticket Size'], data['Window'], hue = data['Slab'])
    plt.title('Boxplot for order window vs ticket size')
    plt.show()
else:
    plt.figure(figsize = (12,8))
    sns.boxplot(daily_data['Ticket Size'], daily_data['Window'], hue = daily_data['Slab'], palette = 'pastel')
    plt.title('Boxplot for order window vs ticket size (daily)')
    plt.show()

    plt.figure(figsize = (12,8))
    sns.boxplot(weekly_data['Ticket Size'], weekly_data['Window'], hue = weekly_data['Slab'], palette = 'pastel')
    plt.title('Boxplot for order window vs ticket size (weekly)')
    plt.show()

    plt.figure(figsize = (12,8))
    sns.boxplot(monthly_data['Ticket Size'], monthly_data['Window'], hue = monthly_data['Slab'], palette = 'pastel')
    plt.title('Boxplot for order window vs ticket size (monthly)')
    plt.show()

    plt.figure(figsize = (12,8))
    sns.boxplot(yearly_data['Ticket Size'], yearly_data['Window'], hue = yearly_data['Slab'], palette = 'pastel')
    plt.title('Boxplot for order window vs ticket size (yearly)')
    plt.show()


# In[36]:

#splitting data on daily basis
order_volume = []

for i in uniqueness:
    daily_data = data[data.Date == i]
    order_volume.append(len(daily_data))


# In[37]:

#plotting order volume and lags
orderVolume = pd.Series(order_volume)
weekLag = orderVolume.shift(-7)

volume_df = pd.DataFrame({'Order Volume':order_volume, 'Week Lag':weekLag})


# In[38]:

plt.figure(figsize = (12,8))
sns.regplot(volume_df['Order Volume'], volume_df['Week Lag'], ci = 99, order=1)
plt.title('Polynomial regression line of week lag vs daily order')
plt.show()


# In[39]:

plt.figure(figsize = (12,8))
sns.regplot(volume_df['Order Volume'], volume_df['Week Lag'], ci = 95, x_estimator = np.mean, order = 2)
plt.title('Regression (unique values) of week lag vs daily order')
plt.show()


# In[40]:

plt.figure(figsize = (12,8))
sns.jointplot(volume_df['Order Volume'], volume_df['Week Lag'], kind = 'kde')
plt.title('Kernel Density plot of daily week lag vs daily order')
plt.show()


# In[41]:

#inference -> Generally if no. of tickets have been less on one day then those have been
# more on the corresponding day of the next week and vice versa


# In[42]:

#Trend line for no. of orders

x = pd.Series(list(range(91)))
plt.figure(figsize = (12,8))
sns.regplot(x, volume_df['Order Volume'], ci = 95, order=3)
plt.title('Polynomial trend line for order volume')
plt.show()


# In[43]:

data.head()


# In[44]:

#monthwise BMI vs ticket_size
sns.factorplot(x="Ticket Size", y="BMI", hue="Slab",
               col="month", data=data, kind="box", size=8, aspect=.5)
plt.show()


# In[45]:

sns.kdeplot(data['Age'], shade = True)
plt.title('Distribution of Age')
plt.show()


# In[46]:

sns.kdeplot(data['BMI'], shade = True)
plt.title('Distribution of BMI')
plt.show()


# In[47]:

sns.kdeplot(data['Revenue'], shade = True)
plt.title('Distribution of Revenue')
plt.show()


# In[48]:

#boxplot for order window vs ticket size
if wholesome == 1:
    plt.figure(figsize = (20,14))
    sns.boxplot(data['Age'], data['BMI'], hue = data['Sex'])
    plt.title('Boxplot for BMI vs Age')
    plt.show()
else:
    plt.figure(figsize = (20,14))
    sns.boxplot(daily_data['Age'], daily_data['BMI'], hue = daily_data['Sex'], palette = 'pastel')
    plt.title('Boxplot for BMI vs Age (daily)')
    plt.show()

    plt.figure(figsize = (20,14))
    sns.boxplot(weekly_data['Age'], weekly_data['BMI'], hue = weekly_data['Sex'], palette = 'pastel')
    plt.title('Boxplot for BMI vs Age (weekly)')
    plt.show()

    plt.figure(figsize = (20,14))
    sns.boxplot(monthly_data['Age'], monthly_data['BMI'], hue = monthly_data['Sex'], palette = 'pastel')
    plt.title('Boxplot for BMI vs Age (monthly)')
    plt.show()

    plt.figure(figsize = (20,14))
    sns.boxplot(yearly_data['Age'], yearly_data['BMI'], hue = yearly_data['Sex'], palette = 'pastel')
    plt.title('Boxplot for BMI vs Age (yearly)')
    plt.show()


# In[49]:

#Revenue
#daily basis barplot of Revenue vs Ticket Size
if wholesome == 1:
    plt.figure(figsize = (20,15))
    sns.barplot(x=data['Ticket Size'], y=data['Revenue'], hue = data['Day'])
    plt.title('Barplot of Revenue vs Ticket Size')
    plt.show()
else:
    plt.figure(figsize = (20,15))
    sns.barplot(x=yearly_data['Ticket Size'], y=yearly_data['Revenue'], hue = yearly_data['Day'])
    plt.title('Barplot of Revenue vs Ticket Size (yearly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=monthly_data['Ticket Size'], y=monthly_data['Revenue'], hue = monthly_data['Day'])
    plt.title('Barplot of Revenue vs Ticket Size (monthly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=weekly_data['Ticket Size'], y=weekly_data['Revenue'], hue = weekly_data['Day'])
    plt.title('Barplot of Revenue vs Ticket Size (weekly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=daily_data['Ticket Size'], y=daily_data['Revenue'], hue = daily_data['Day'])
    plt.title('Barplot of Revenue vs Ticket Size (daily)')
    plt.show()


# In[50]:

#Revenue
#daily basis barplot of Revenue vs Ticket Size
if wholesome == 1:
    plt.figure(figsize = (20,15))
    sns.barplot(x=data['Ticket Size'], y=data['Revenue'], hue = data['Sex'])
    plt.title('Barplot of Revenue vs Ticket Size')
    plt.show()
else:
    plt.figure(figsize = (20,15))
    sns.barplot(x=yearly_data['Ticket Size'], y=yearly_data['Revenue'], hue = yearly_data['Sex'])
    plt.title('Barplot of Revenue vs Ticket Size (yearly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=monthly_data['Ticket Size'], y=monthly_data['Revenue'], hue = monthly_data['Sex'])
    plt.title('Barplot of Revenue vs Ticket Size (monthly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=weekly_data['Ticket Size'], y=weekly_data['Revenue'], hue = weekly_data['Sex'])
    plt.title('Barplot of Revenue vs Ticket Size (weekly)')
    plt.show()
    
    plt.figure(figsize = (20,15))
    sns.barplot(x=daily_data['Ticket Size'], y=daily_data['Revenue'], hue = daily_data['Sex'])
    plt.title('Barplot of Revenue vs Ticket Size (daily)')
    plt.show()

