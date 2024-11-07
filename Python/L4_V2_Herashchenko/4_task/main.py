import pandas as pd

flights_df = pd.read_csv('C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L4_V2_Herashchenko\\4_task\\2008_rand.csv')
airports_df = pd.read_csv('C:\\ALL\\OTHER\\GitHub\HOMEWORK\\Python\\L4_V2_Herashchenko\\4_task\\airports.csv')

mean_distance = flights_df['Distance'].mean()
min_distance = flights_df['Distance'].min()
max_distance = flights_df['Distance'].max()

print("1:")
print(f"Mean: {mean_distance:.2f}")
print(f"Min: {min_distance}")
print(f"Max: {max_distance}")

max_distance_flights = flights_df[flights_df['Distance'] == max_distance]
print("\n2.1:")
print(max_distance_flights[['Year', 'Month', 'DayofMonth', 'FlightNum', 'Origin', 'Dest', 'Distance']])

flight_nums = max_distance_flights['FlightNum'].unique()

other_days_same_flights = flights_df[(flights_df['FlightNum'].isin(flight_nums)) & (flights_df['Distance'] != max_distance)]

print("\n2.2:")
print(other_days_same_flights[['Year', 'Month', 'DayofMonth', 'FlightNum', 'Origin', 'Dest', 'Distance']])

flights_per_day = flights_df['DayOfWeek'].value_counts().idxmax()
print(f"\n3: {flights_per_day}")

december_flights = flights_df[flights_df['Month'] == 12]
top_origins_december = december_flights['Origin'].value_counts().head(5).index

popular_origins_info = airports_df[airports_df['iata'].isin(top_origins_december)][['iata', 'city']]
print("\n4:")
print(popular_origins_info)

max_arrival_delay = flights_df['ArrDelay'].max()
max_delay_flight = flights_df[flights_df['ArrDelay'] == max_arrival_delay]

print("\n5:")
print("\nFlight:")
print(max_delay_flight[['Year', 'Month', 'DayofMonth', 'Origin', 'Dest', 'ArrDelay']])

max_delay_airport = max_delay_flight.iloc[0]['Dest']
max_delay_airport_info = airports_df[airports_df['iata'] == max_delay_airport][['airport', 'city', 'state']]
print("\nAirport:")
print(max_delay_airport_info)