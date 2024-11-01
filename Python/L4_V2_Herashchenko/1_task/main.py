import pandas as pd

data = pd.read_excel('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\1_task\\vaccination_process_2021_regions.xlsx')

x = data[['Дата (період) данних', 'Pfizer-BioNTech, осіб']]

people_september = x[pd.to_datetime(data["Дата (період) данних"]).dt.month==9]

print(people_september['Pfizer-BioNTech, осіб'].sum())