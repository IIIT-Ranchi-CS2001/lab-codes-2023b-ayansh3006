import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("AQI_Data.csv")

# a) Display the first 8 rows
print("First 8 rows:")
print(df.head(8))

# b) Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail(5))

# c) Show dtype and number of non-null values in each column
print("\nData types and number of non-null values:")
print(df.info())

# d) Use numpy to compute mean AQI, max PM2.5, and min PM10 for each city
city_stats = df.groupby('City').agg(
    mean_aqi=('AQI', 'mean'),
    max_pm25=('PM2.5', 'max'),
    min_pm10=('PM10', 'min')
).reset_index()

# Display the computed statistics
print("\nCity-wise statistics (mean AQI, max PM2.5, min PM10):")
print(city_stats)

# Rename the columns
df.rename(columns={
    'AQI': 'Air Quality Index',
    'PM2.5': 'Particular Matter 2.5',
    'PM10': 'Particular Matter 10',
    'City': 'Location'
}, inplace=True)

# Replace all occurrences of "unknown" in the Location column with "not available"
df['Location'].replace('unknown', 'not available', inplace=True)

# Display the updated dataset
print(df)

# Save the updated dataset to a new file result.csv
df.to_csv('result.csv', index=False)

