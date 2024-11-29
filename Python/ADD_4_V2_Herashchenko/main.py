import pandas as pd


# Загрузка данных
df = pd.read_csv('C://Users//tiko1//Documents//GitHub//HOMEWORK//Python//ADD_4//diabetes_changed.csv')

# 1. Удаление дубликатов
df = df.drop_duplicates()

# 2. Удаление строк и столбцов с преимущественно отсутствующими данными
threshold = 0.5  # Если больше 50% значений пропущено в столбце или строке, удаляем
df = df.dropna(axis=1, thresh=int(threshold * len(df)))  # Удаляем столбцы
df = df.dropna(axis=0, thresh=int(threshold * len(df.columns)))  # Удаляем строки

# 3. Определение выбросов с использованием квантилей (IQR-метод)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))

# 4. Определение выбросов с использованием статистических функций (метод на основе среднеквадратичного отклонения)
MX = df.mean()
SIGMA = df.std()
outliers_stat = (df - MX).abs() > 3 * SIGMA

# 5. Объединение выбросов (с учетом обоих методов)
outliers_combined = outliers_iqr & outliers_stat

# 6. Замена выбросов и отсутствующих данных на средние значения по столбцам
df = df.apply(lambda col: col.fillna(col.mean()))  # Заменяем отсутствующие данные средним значением
df[outliers_combined] = df[outliers_combined].apply(lambda col: col.fillna(col.mean()))  # Заменяем выбросы средним значением

# Проверка результатов
print("Предобработанные данные:")
print(df)

# Сохраняем результат в новый файл
df.to_csv('diabetes_cleaned.csv', index=False)
