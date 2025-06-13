# Real-Time Earthquake Data Visualization using Python

## 🔍 Project Overview
This project fetches real-time global earthquake data using the USGS API and visualizes:
- Distribution of magnitudes
- Earthquakes over time with depth

## 📦 Tools & Technologies
- Python
- Requests (for API)
- Pandas (for data processing)
- Seaborn & Matplotlib (for visualization)

## 📡 API Used
- USGS Earthquake Feed: [All Day GeoJSON](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson)

## 📁 Files
- `earthquake_data_visualizer.py` – Main Python script
- `output_sample.csv` – Earthquake data
- `magnitude_distribution.png` – Histogram plot
- `earthquakes_over_time.png` – Scatter plot
- `README.md` – Project documentation

## 🚀 How to Run
1. Install dependencies:
    ```bash
    pip install requests pandas matplotlib seaborn
    ```
2. Run the script:
    ```bash
    python earthquake_data_visualizer.py
    ```

## 📊 Output
- **Histogram**: Shows how strong the earthquakes were.
- **Scatter Plot**: Shows magnitude over time, colored by depth.

---

✅ Project ready for internship submission.
