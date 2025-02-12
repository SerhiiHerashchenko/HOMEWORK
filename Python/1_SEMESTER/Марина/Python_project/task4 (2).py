import pandas as pd

df = pd.read_csv('C://ALL//OTHER//GitHub//HOMEWORK//Python//Python_project//diabetes_changed.csv')

# 1. Видалення дублікатів
df = df.drop_duplicates()

# 2. Видалення строк та стовпців з переважно відсутніми данними
threshold = 0.5  # >50%
df = df.dropna(axis=1, thresh=int(threshold * len(df)))  # стовпці
df = df.dropna(axis=0, thresh=int(threshold * len(df.columns)))  # строки

# 3. Визначення викидів з використанням квантилів
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
out_of_range_quantile = (df < (Q1 - 1.5 * (Q3 - Q1))) | (df > (Q3 + 1.5 * (Q3 - Q1)))

# 4. Визначення викидів з використанням статистичних функцій
MX = df.mean()
sigma_X = df.std()
out_of_range_statistics = (df - MX).abs() > 3 * sigma_X

# 5. Заміна викидів (загальних для 2 критеріїв) та відсутніх данних
# середніми значеннями по стовпцям
out_of_range = out_of_range_quantile & out_of_range_statistics
mean = lambda col: col.fillna(col.mean())
df = df.apply(mean)
df[out_of_range] = df[out_of_range].apply(mean)

print(df)
df.to_csv('diabetes_cleaned.csv', index=False)