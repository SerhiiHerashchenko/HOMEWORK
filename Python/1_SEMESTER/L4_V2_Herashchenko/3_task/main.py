import pandas as pd

df1 = pd.read_csv('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\3_task\\students1.txt', sep='\t')
df2 = pd.read_csv('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\3_task\\students2.txt', sep='\t')
df3 = pd.read_csv('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\3_task\\students3.txt', sep='\t')

df = pd.merge(df1, df2, on='Name', how='outer')
df = pd.merge(df, df3, on='Name', how='outer')

english_corr_1_2 = df['Іноземна мова1'].corr(df['Іноземна мова2'])
english_corr_1_3 = df['Іноземна мова1'].corr(df['Іноземна мова3'])
english_corr_2_3 = df['Іноземна мова2'].corr(df['Іноземна мова3'])

programming_bzhd_corr = df['Програмування2'].corr(df['Безпека життєдіяльності та охорона праці'])

print(f"Іноземна мова1 and Іноземна мова2: {english_corr_1_2:.2f}")
print(f"Іноземна мова1 and Іноземна мова3: {english_corr_1_3:.2f}")
print(f"Іноземна мова2 and Іноземна мова3: {english_corr_2_3:.2f}")

print(f"Програмування2 and Безпека життєдіяльності та охорона праці: {programming_bzhd_corr:.2f}")