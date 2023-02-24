import pandas as pd

df = pd.read_csv('Task1.csv')
# print(df.columns)
null_counts = df.isnull().sum() # print(null_counts)

num_duplicates = df.duplicated().sum()

print(num_duplicates)

df["order_purchase_date"] = pd.to_datetime(df["order.order_purchase_date"])
df2 = df[(df["order_purchase_date"].dt.day_of_week == 5) | (df["order_purchase_date"].dt.day_of_week == 6)]
print(df2.shape)
print(df2["order.order_id"].drop_duplicates().shape[0])


category = df.groupby('product.category')['sales_amt'].sum()
highest_sales = category.idxmax()
print("THE CATEGORY WITH THE HIGHEST SALES IS:", highest_sales)


df['order_purchase_date'] = pd.to_datetime(df['order.order_purchase_date'])
df['day_of_order'] = df['order_purchase_date'].dt.strftime('%A') # Weekday name
df['day_label'] = df['day_of_order'].apply(lambda x: 'weekend' if x in ['Saturday', 'Sunday'] else 'weekday')

weekend = df.groupby('day_label')['order.order_id'].nunique()
print(weekend)



# Count number of customers with first name like "Alan"
count = df[df['order.customer.customer_name'].str.startswith('Alan')]['order.customer.customer_id'].nunique()

print(count)


