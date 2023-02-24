import pandas as pd
import requests

params = {"offset": 1, "limit": 100}
results = []

# Make an HTTP GET request to the API and parse the response as JSON
while params.get("offset") <= 500:
    response = requests.get(
        "https://globalmart-api.onrender.com/mentorskool/v1/sales",
        headers={"access_token": "fe66583bfe5185048c66571293e0d358"},
        params=params,
    ).json()
    results += response["data"]
    params["offset"] = int(response.get("next").split("=")[1][:3])

# Normalize the JSON data into a DataFrame
df = pd.json_normalize(results)

# Print the column labels
print(df.columns)

resultDataFrame = df[
    [
        "id",
        "sales_amt",
        "qty",
        "discount",
        "profit_amt",
        "order.order_id",
        "order.order_purchase_date",
        "order.order_status",
        "order.order_delivered_customer_date",
        "order.order_estimated_delivery_date",
        "product.product_id",
        "product.colors",
        "product.category",
        "order.customer.customer_id",
        "order.customer.customer_name",
        "order.vendor.VendorID",
    ]
]

# Save the DataFrame to a CSV file
resultDataFrame.to_csv("Task1.csv", index=False)
