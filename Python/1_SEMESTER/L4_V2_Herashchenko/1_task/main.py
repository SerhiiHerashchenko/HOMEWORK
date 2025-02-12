import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\1_task\\vaccination_process_2021_regions.xlsx')

x = data[['Назва території','Дата (період) данних', 'Pfizer-BioNTech, осіб']]

people_september = x[pd.to_datetime(data["Дата (період) данних"], dayfirst=True).dt.month==9].groupby('Назва території', as_index = False)["Pfizer-BioNTech, осіб"].sum()

people_september.plot(kind='bar', x = "Назва території", figsize = (8,2))
plt.show()
