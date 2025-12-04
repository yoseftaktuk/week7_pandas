import pandas as pd
import numpy as np
df = pd.read_json('data.json')
df = pd.DataFrame(df)
#שאלה 1
convert_dict = { 'shipping_days': int, 'customer_age': int, 'rating': float}
df = df.astype(convert_dict)
df['order_date'] = df['order_date'].apply(pd.to_datetime)
df['total_amount'] = df['total_amount'].str.replace('$', '')
df['total_amount'] = pd.to_numeric(df['total_amount'],  errors = 'coerce')

#שאלה 2
df['items_html'] = df['items_html'].str.replace('<', '', regex=True)
df['items_html'] = df['items_html'].str.replace('>', '', regex=True)
df['items_html'] = df['items_html'].str.replace('/', '', regex=True)

#שאלה 3
df = df.replace(r'^\s*$', 'no coupon', regex=True)

#שאלה 4
df['order_month'] = df['order_date'].dt.month

#שאלה 5
avrege = np.mean(df['total_amount'])

l = []
for price in df['total_amount']:
    if price > avrege:
        l.append(True)
    else:
        l.append(False) 

sorted_df = df.sort_values(by='total_amount',ascending=False)
df['high_value_order'] = l
#שאלה 6
    
# print(df['country'])
group = df.groupby('country')["rating"].transform('mean')
group.mean()

df['rating'] = group
print(df)
# print(df['high_value_order'])
# print(df['rating'])
# print(df.info()) 
# print(df['total_amount'])

#שאלה 7
filtered_values = np.where((df['total_amount'] > 1000) & (df['rating'] > 4.5))


#שאלה 8

l = []
for time in df['shipping_days']:
    if int(time) > 7:
        l.append('delayed')
    else:
        l.append('on_time')    

df['delivery_status'] = l
print(df['delivery_status'])

#שאלה 9
df.to_csv('clean_orders_209265933.csv')