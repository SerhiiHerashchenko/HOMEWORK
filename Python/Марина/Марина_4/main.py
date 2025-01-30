import pandas as pd 
from datetime import datetime 
 
data = pd.read_excel('C://Users//tiko1//Documents//GitHub//HOMEWORK//Python//Марина_4//filter4.xlsx') 
 
data['Data'] = pd.to_datetime(data['Data'], dayfirst=True) 
current_date = datetime.now() 
 
# Стовпець Recycling 
data['Recycling'] = data.apply(lambda row: 'Yes' if (current_date - row['Data']).days > row['Shelf_life'] else 'No', axis=1) 
print(data[['Product', 'Data', 'Shelf_life', 'Recycling']]) 
 
print("Товари, які потрібно відправити на утилізацію:") 
recycling_needed = data[data['Recycling'] == 'Yes'] 
print(recycling_needed) 
 
print("Товари, виготовлені в Одесі, які потрібно відправити на утилізацію:") 
odessa_recycling = data[(data['Region'] == 'Odessa') & (data['Recycling'] == 'Yes')] 
print(odessa_recycling) 
 
print("Товари Mineral water, які не прострочені:") 
mineral_water_not_expired = data[(data['Product'] == 'Mineral water') & (data['Recycling'] == 'No')] 
print(mineral_water_not_expired) 
 
print("Товари, виготовлені у Львові або Полтаві:") 
lviv_poltava_products = data[data['Region'].isin(['Lviv', 'Poltava'])] 
print(lviv_poltava_products) 
 
print("Товари, що коштують більше 50 грн. і які потрібно відправити на утилізацію:") 
expensive_recycling_products = data[(data['Price'] > 50) & (data['Recycling'] == 'Yes')] 
print(expensive_recycling_products) 
 
print("Вибірка товарів за умовами:") 
odessa_price = data[(data['Region'] == 'Odessa') & (data['Price'] < 30)] 
truskavets_recycling = data[(data['Region'] == 'Truskavets') & (data['Recycling'] == 'Yes')] 
selected_products = pd.concat([odessa_price, truskavets_recycling]) 
print(selected_products) 
 
print("Товари, що відповідають заданим критеріям:") 
odessa_recycling = data[(data['Region'] == 'Odessa') & (data['Recycling'] == 'Yes')] 
expensive_valid = data[(data['Price'] > 40) & (data['Shelf_life'] > 30)] 
selected_products = pd.concat([odessa_recycling, expensive_valid]) 
print(selected_products)
