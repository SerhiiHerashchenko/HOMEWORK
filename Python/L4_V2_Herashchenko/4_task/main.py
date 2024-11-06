import pandas as pd

# Загрузка данных
flights_df = pd.read_csv('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\4_task\\2008_rand.csv')
airports_df = pd.read_csv('C:\\ALL\\OTHER\\GitHub\HOMEWORK\\Python\\L4_V2_Herashchenko\\4_task\\airports.csv')

# 1. Среднее, минимальное и максимальное расстояние
mean_distance = flights_df['Distance'].mean()
min_distance = flights_df['Distance'].min()
max_distance = flights_df['Distance'].max()

print(f"Среднее расстояние: {mean_distance:.2f}")
print(f"Минимальное расстояние: {min_distance}")
print(f"Максимальное расстояние: {max_distance}")

# 2. Проверка максимального расстояния
# Найдём рейсы с максимальным расстоянием
max_distance_flights = flights_df[flights_df['Distance'] == max_distance]
print("\nРейсы с максимальным расстоянием:")
print(max_distance_flights[['Year', 'Month', 'DayofMonth', 'FlightNum', 'Origin', 'Dest', 'Distance']])

# Получаем номера рейсов с максимальным расстоянием
flight_nums = max_distance_flights['FlightNum'].unique()

# Фильтруем те же рейсы в другие дни, исключая записи с максимальным расстоянием
other_days_same_flights = flights_df[(flights_df['FlightNum'].isin(flight_nums)) & (flights_df['Distance'] != max_distance)]

print("\nРасстояния, пройденные этими же рейсами в другие дни:")
print(other_days_same_flights[['Year', 'Month', 'DayofMonth', 'FlightNum', 'Origin', 'Dest', 'Distance']])

# 3. День недели с наибольшим количеством полётов
flights_per_day = flights_df['DayOfWeek'].value_counts().idxmax()
print(f"\nДень недели с наибольшим количеством полётов: {flights_per_day}")

# 4. Наиболее популярные места отправления в декабре
december_flights = flights_df[flights_df['Month'] == 12]
top_origins_december = december_flights['Origin'].value_counts().head(5).index

# Добавление информации о городах
popular_origins_info = airports_df[airports_df['iata'].isin(top_origins_december)][['iata', 'city']]
print("\n5 наиболее популярных мест отправления в декабре и их города:")
print(popular_origins_info)

# 5. Аэропорт с наибольшей задержкой при посадке
max_arrival_delay = flights_df['ArrDelay'].max()
max_delay_flight = flights_df[flights_df['ArrDelay'] == max_arrival_delay]

print("\nАэропорт с наибольшей задержкой при посадке:")
print(max_delay_flight[['Year', 'Month', 'DayofMonth', 'Origin', 'Dest', 'ArrDelay']])

# Вывод аэропорта с наибольшей задержкой и его город из airports_df
max_delay_airport = max_delay_flight.iloc[0]['Dest']
max_delay_airport_info = airports_df[airports_df['iata'] == max_delay_airport][['airport', 'city', 'state']]

print("\nИнформация об аэропорте с наибольшей задержкой:")
print(max_delay_airport_info)
