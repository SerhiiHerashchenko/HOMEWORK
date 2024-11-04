import pandas as pd
import datetime as dt

data = pd.read_excel("C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\2_task\\filter2.xlsx")


t=dt.datetime.today()
# x=data[t<=pd.to_datetime(data["Shelf_life"], dayfirst=True).dt.]


data = open("C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\2_task\\text.txt")
file = data.read()
print(file)
