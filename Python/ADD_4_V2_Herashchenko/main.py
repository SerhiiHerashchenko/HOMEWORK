import pandas as pd

df = pd.read_csv('C:\\ALL\\GitHub repositories\\HOMEWORK\\Python\\ADD_4_V2_Herashchenko\\diabetes_changed.csv')

df = df.drop_duplicates()

threshold = 0.5
df = df.dropna(axis=1, thresh=int(threshold * len(df)))
df = df.dropna(axis=0, thresh=int(threshold * len(df.columns)))

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
outliers_iqr = ((df < (Q1 - 1.5 * (Q3 - Q1))) | (df > (Q3 + 1.5 * (Q3 - Q1))))

MX = df.mean()
SIGMA = df.std()
outliers_stat = (df - MX).abs() > 3 * SIGMA

outliers_combined = outliers_iqr & outliers_stat

df = df.apply(lambda col: col.fillna(col.mean()))
df[outliers_combined] = df[outliers_combined].apply(lambda col: col.fillna(col.mean()))

print(df)

df.to_csv('diabetes_cleaned.csv', index=False)
