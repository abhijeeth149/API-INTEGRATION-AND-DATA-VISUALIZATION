# earthquake_data_visualizer.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Get data from USGS Earthquake API
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch data from API")
    exit()

data = response.json()

# Step 2: Extract relevant fields
earthquakes = []
for quake in data['features']:
    props = quake['properties']
    coords = quake['geometry']['coordinates']
    
    earthquakes.append({
        'Place': props['place'],
        'Magnitude': props['mag'],
        'Time': props['time'],
        'Longitude': coords[0],
        'Latitude': coords[1],
        'Depth': coords[2]
    })

# Step 3: Create DataFrame and clean data
df = pd.DataFrame(earthquakes)
df.dropna(subset=['Magnitude'], inplace=True)
df['Time'] = pd.to_datetime(df['Time'], unit='ms')

# Optional: Save to CSV
df.to_csv("output_sample.csv", index=False)

# Step 4: Set Seaborn style
sns.set(style="whitegrid")

# Step 5: Plot 1 - Histogram of magnitudes
plt.figure(figsize=(10, 5))
sns.histplot(df["Magnitude"], bins=20, kde=True, color='tomato')
plt.title("Distribution of Earthquake Magnitudes (Last 24 Hours)")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("magnitude_distribution.png")
plt.close()

# Step 6: Plot 2 - Scatter plot of earthquakes over time
plt.figure(figsize=(12, 6))
sns.scatterplot(x="Time", y="Magnitude", hue="Depth", size="Magnitude", data=df,
                palette="coolwarm", sizes=(30, 200), alpha=0.7)

plt.title("Earthquake Magnitudes Over Time")
plt.xlabel("Time")
plt.ylabel("Magnitude")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("earthquakes_over_time.png")
plt.close()

print("Project completed. Images and data saved.")
