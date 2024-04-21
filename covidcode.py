'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('covidcases.csv')
print(df.isnull().sum())
print(df.dtypes)
df['Date'] = df['Date'].str.strip('"')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)

total_cases = df['Cases'].sum()
total_deaths = df['Deaths'].sum()

print(f"Total Cases: {total_cases}")
print(f"Total Deaths: {total_deaths}")

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Cases'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.title('Total Cases Over Time')
plt.grid(True)
plt.show()'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Creating the dataset
# Let's create some random data for the example
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
confirmed_cases = np.random.randint(100, 1000, size=len(dates))
deaths = np.random.randint(5, 50, size=len(dates))
recovered = np.random.randint(50, 800, size=len(dates))

# Create a DataFrame
covid_data = pd.DataFrame({
    'Date': dates,
    'Confirmed Cases': confirmed_cases,
    'Deaths': deaths,
    'Recovered': recovered
})

# Step 2: Data Visualization
# Plotting confirmed cases, deaths, and recovered over time
plt.figure(figsize=(10, 6))
plt.plot(covid_data['Date'], covid_data['Confirmed Cases'], label='Confirmed Cases', color='blue')
plt.plot(covid_data['Date'], covid_data['Deaths'], label='Deaths', color='red')
plt.plot(covid_data['Date'], covid_data['Recovered'], label='Recovered', color='green')
plt.title('COVID-19 Stats Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()