import pandas as pd
from datetime import datetime, timedelta

data = pd.read_excel('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\2_task\\filter2.xlsx')

today = datetime.now()

data['Discount'] = ((pd.to_datetime(data['Shelf_life']) - today) <= timedelta(days=3)) | (pd.to_datetime(data['Shelf_life']) < today)

discounted_items = data[data['Discount']]

discounted_polish_items = data[(data['CountryOfOrigin'] == 'Poland') & (data['Discount'])]

milk_good_health_no_discount = data[(data['Product'] == "Milk 'Good health'") & (data['Discount'] == False)]

ukraine_no_discount = data[(data['CountryOfOrigin'] == 'Ukraine') & (~data['Discount'])]

large_discounted_batches = data[(data['Quantity'] > 20) & (data['Discount'])]

polish_large_volume_or_ukraine_discounted = data[((data['CountryOfOrigin'] == 'Poland') & (data['Quantity'] > 30)) | ((data['CountryOfOrigin'] == 'Ukraine') & (data['Discount']))]

polish_low_price_or_small_discounted_volume = data[((data['CountryOfOrigin'] == 'Poland') & (data['Price'] < 20)) | ((data['Quantity'] < 40) & (data['Discount']))]

print("1:\n", discounted_items, "\n____________________________")
print("2:\n", discounted_polish_items, "\n____________________________")
print("3:\n", milk_good_health_no_discount, "\n____________________________")
print("4:\n", ukraine_no_discount, "\n____________________________")
print("5:\n", large_discounted_batches, "\n____________________________")
print("6:\n", polish_large_volume_or_ukraine_discounted, "\n____________________________")
print("7:\n", polish_low_price_or_small_discounted_volume, "\n____________________________")
