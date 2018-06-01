
# coding: utf-8

# In[37]:

import pandas as pd
import numpy as np
import re
import os
os.chdir('/home/ankushraut/Downloads/Thirio')


# In[38]:

data = pd.read_csv('Dataset.csv')


# In[39]:

dish = pd.read_csv('Dishes.csv')


# In[40]:

data.describe()


# In[41]:

positives = ['yes', 'yep', 'yeah', 'sure', 'yo', 'ordered before', 'ya']
negatives = ['nah', 'no', 'nope', 'never']
tracking = ['track', 'where', 'waiting', 'late', 'why']
cancellation = ["cancel", "don't deliver", "don't wanna eat"]
new_order = ['new', 'place', 'order']
def contains_word(text, corpus):
    for word in corpus:
        pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
        pattern = re.compile(pattern, re.IGNORECASE)
        matches = re.search(pattern, text)
        if bool(matches):
            break
    return bool(matches)


# In[42]:

from sklearn.cluster import KMeans


# In[43]:

from sklearn.preprocessing import LabelEncoder
lbl_sex = LabelEncoder()
lbl_day = LabelEncoder()
lbl_slab = LabelEncoder()
data.Sex = lbl_sex.fit_transform(data.Sex)
data.Day = lbl_day.fit_transform(data.Day)
data.Slab = lbl_slab.fit_transform(data.Slab)


# In[44]:

#kmeans recommendation
kmeans_spice = KMeans(n_clusters = len(data.Spice.unique()), random_state = 0).fit(data.drop(labels = ['Date', 'Ticket Size',
                                                                                                      'CustomerID',
                                                                                                      'Cancel','Curry', 'ETA',
                                                                                                      'State Cuisine', 'Order Status',
                                                                                                      'Revenue', 'Discount'], axis = 1))
data['spice_cluster'] = pd.DataFrame({'spice_cluster':kmeans_spice.labels_})
unique_spice = []

for i in range(len(data.spice_cluster.unique())):
    unique_spice.append(np.sort(data.spice_cluster.unique())[i])

mode_spice = []
for i in unique_spice:
    spice_centered = data[(data.spice_cluster == i)]
    mode_spice.append(spice_centered.Spice.mode()[0])
    
recommended_spice = []
for i in range(len(data)):
    recommended_spice.append(mode_spice[data.spice_cluster[i]])


# In[45]:

#kmeans recommendation
lbl_state = LabelEncoder()
data['State Cuisine'] = lbl_state.fit_transform(data['State Cuisine'])
kmeans_state = KMeans(n_clusters = len(data['State Cuisine'].unique()), random_state = 0).fit(data.drop(labels = ['Date', 'Ticket Size',
                                                                                                      'CustomerID',
                                                                                                      'Cancel','Spice', 'ETA',
                                                                                                      'Curry', 'Order Status',
                                                                                                      'Revenue', 'Discount'], axis = 1))
data['State Cuisine'] = lbl_state.inverse_transform(data['State Cuisine'])
data['state_cluster'] = pd.DataFrame({'state_cluster':kmeans_state.labels_})
unique_state = []

for i in range(len(data.state_cluster.unique())):
    unique_state.append(np.sort(data.state_cluster.unique())[i])

mode_state = []
for i in unique_state:
    state_centered = data[(data.state_cluster == i)]
    mode_state.append(state_centered['State Cuisine'].mode()[0])
    
recommended_state = []
for i in range(len(data)):
    recommended_state.append(mode_state[data.state_cluster[i]])


# In[46]:

#kmeans recommendation
kmeans_curry = KMeans(n_clusters = len(data.Curry.unique()), random_state = 0).fit(data.drop(labels = ['Date', 'Ticket Size',
                                                                                                      'CustomerID',
                                                                                                      'Cancel','Spice', 'ETA',
                                                                                                      'State Cuisine', 'Order Status',
                                                                                                      'Revenue', 'Discount'], axis = 1))
data['curry_cluster'] = pd.DataFrame({'curry_cluster':kmeans_curry.labels_})
unique_curry = []

for i in range(len(data.curry_cluster.unique())):
    unique_curry.append(np.sort(data.curry_cluster.unique())[i])

mode_curry = []
for i in unique_curry:
    curry_centered = data[(data.curry_cluster == i)]
    mode_curry.append(curry_centered.Curry.mode()[0])
    
recommended_curry = []
for i in range(len(data)):
    recommended_curry.append(mode_curry[data.curry_cluster[i]])


# In[47]:

def recommended(new_token):
    most_recommended = []
    moderately_recommended = []
    recommended = []
    for i in range(len(dish)):
        if dish.Curry[i] == recommended_curry[new_token] and dish.Spice[i] == recommended_spice[new_token] and dish['State Cuisine'][i] == recommended_state[new_token]:
            most_recommended.append(dish.Dish[i])
        elif dish.Curry[i] == recommended_curry[new_token] and dish.Spice[i] == recommended_spice[new_token]:
            moderately_recommended.append(dish.Dish[i])
        elif dish['State Cuisine'][i] == recommended_state[new_token] and dish.Spice[i] == recommended_spice[new_token]:
            moderately_recommended.append(dish.Dish[i])
        elif dish.Curry[i] == recommended_curry[new_token] and dish['State Cuisine'][i] == recommended_state[new_token]:
            moderately_recommended.append(dish.Dish[i])
        elif dish.Curry[i] == recommended_curry[new_token] and dish.Spice[i] != recommended_spice[new_token] and dish['State Cuisine'][i] != recommended_state[new_token]:
            recommended.append(dish.Dish[i])
        elif dish.Curry[i] != recommended_curry[new_token] and dish.Spice[i] == recommended_spice[new_token] and dish['State Cuisine'][i] != recommended_state[new_token]:
            recommended.append(dish.Dish[i])
        elif dish.Curry[i] != recommended_curry[new_token] and dish.Spice[i] != recommended_spice[new_token] and dish['State Cuisine'][i] == recommended_state[new_token]:
            recommended.append(dish.Dish[i])
    return most_recommended, moderately_recommended, recommended


# In[48]:

new_customer = input("Hi, I'm Thirio, your nutritional companion. Have you ordered from us before?")
if contains_word(new_customer, positives):
    customer_number = int(input('Welcome back! Please enter your unique ID. '))
else:
    print('Welcome to Thirio!')
    customer_number = len(data.CustomerID.unique())


# In[49]:

feedback_food = []
customer_id = []
feedback_delivery = []

flow1 = input('Do you want to place a new order or track your order?')
flow1_1 = input('Please enter the token number of your last order, if you have one.')

if contains_word(flow1, tracking):
    print('Your order ', data['Order Status'][int(flow1_1)])
    print('ETA ', data['ETA'][int(flow1_1)])

elif contains_word(flow1, cancellation):
    flow1_2 = input('Do you wanna cancel your order? ')
    if contains_word(flow1_2, positives):
        flow1_2_1 = input('Please enter your token number. ')
        if flow1_2_1.isdigit() == False or int(flow1_2_1) not in data.index:
            flow1_2_1 = input('Please enter a valid token number. ')
        print(data.Cancel[int(flow1_2_1)])

elif contains_word(flow1, new_order):
    new_token = len(data)-1
    rec = recommended(new_token)
    if len(rec[0]) != 0:
        print('We highly recommend you the following dishes:', rec[0])
    elif len(rec[1]) != 0:
        print('You could try these dishes:', rec[1])
    else:
        print('Wanna try one of these:', rec[2])
    flow1_3 = input('What would you like to order?')
    print('Thank you for ordering from Thirio! Your nutritious delicacy is en route!')

    
else:
    flow2 = input('Would you like to leave a feedback and help us improve?')
    if contains_word(flow2, positives):
        flow2_1 = int(input('Please rate the food quality and taste on a scale of 1-5. '))
        if flow2_1 == 5:
            print('We are privileged to have served you such tasty food.')
        elif flow2_1 == 4:
            flow2_1_1 = input('Please let us know how we can give you the best eating experience. ')
            feedback_food.append(flow2_1_1)
            customer_id.append(int(flow1_1))
        elif flow2_1 == 3:
            flow2_1_2 = input('Please let us know how we can go above average next time! ')
            feedback_food.append(flow2_1_2)
            customer_id.append(int(flow1_1))
        else:
            flow2_1_3 = input('Please help us know what went so wrong with the food. ')
            feedback_food.append(flow2_1_3)
            customer_id.append(int(flow1_1))
            print('We are really sorry you had to experience that. We would surely improve next time. ')
        
        flow2_2 = int(input('Please rate the delivery service on a scale of 1-5. '))
        if flow2_2 == 5:
            print('We are privileged to have served you so well!')
        elif flow2_2 == 4:
            flow2_2_1 = input('Please let us know how we can give you the best delivery service. ')
            feedback_delivery.append(flow2_2_1)
            customer_id.append(int(flow1_1))
        elif flow2_2 == 3:
            flow2_2_2 = input('Please let us know how we can improve our delivery service next time. ')
            feedback_delivery.append(flow2_2_2)
            customer_id.append(int(flow1_1))
        else:
            flow2_2_3 = input('Please help us know what went so wrong with the delivery. ')
            feedback_delivery.append(flow2_2_3)
            customer_id.append(int(flow1_1))
            print('We are really sorry you had to experience that. We would surely improve next time. ')
        print('Thanks for your valuable feedback!')
flow3 = input('Please let us know in case of any other grievances. ')
print("Thanks. We'll get back to you shortly.")


# In[50]:

data.head()


# In[51]:

#baseline recommendation
customer_data = data[(data.CustomerID == customer_number)].reset_index(drop = True)

state_preference = customer_data['State Cuisine'].value_counts().index
curry_preference = customer_data['Curry'].value_counts().index
spice_preference = customer_data['Spice'].value_counts().index

for i in range(len(state_preference)):
    if state_preference[i] not in data['State Cuisine'].tail(4):
        state_recommendation = state_preference[i]
    break

for i in range(len(curry_preference)):
    if curry_preference[i] not in data['Curry'].tail(4):
        curry_recommendation = curry_preference[i]
    break
    
for i in range(len(spice_preference)):
    if spice_preference[i] not in data['Spice'].tail(4):
        spice_recommendation = spice_preference[i]
    break

print('Based on your likes, we recommend', curry_recommendation, 'curry and', spice_recommendation, 'spices from', state_recommendation, '.')

