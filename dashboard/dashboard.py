import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data peminjaman berdasarkan musim
day_df = pd.read_csv('../data/day.csv')
hour_df = pd.read_csv('../data/hour.csv')

# Rata-rata peminjaman sepeda berdasarkan musim
season_avg = day_df.groupby('season')['cnt'].mean()
season_labels = ['Winter', 'Spring', 'Summer', 'Fall']
season_avg.index = [season_labels[i-1] for i in season_avg.index]
season_avg_df = pd.DataFrame(season_avg).reset_index()
season_avg_df.columns = ['Season', 'Average Bike Rentals']

# Rata-rata peminjaman sepeda per jam pada hari Sabtu
hour_avg_saturday = hour_df[hour_df['weekday'] == 6].groupby('hr')['cnt'].mean()
hour_avg_saturday_df = pd.DataFrame(hour_avg_saturday).reset_index()
hour_avg_saturday_df.columns = ['Hour', 'Average Bike Rentals']

# Rata-rata peminjaman sepeda per jam pada hari Minggu
hour_avg_sunday = hour_df[hour_df['weekday'] == 0].groupby('hr')['cnt'].mean()
hour_avg_sunday_df = pd.DataFrame(hour_avg_sunday).reset_index()
hour_avg_sunday_df.columns = ['Hour', 'Average Bike Rentals']

# Title
st.title('Bike Rentals Dashboard')

# Visualisasi 1: Bar chart untuk peminjaman sepeda berdasarkan musim
st.subheader('Average Bike Rentals by Season')
st.write("### Data Table: Average Bike Rentals by Season")
st.table(season_avg_df)  # Menampilkan tabel rata-rata peminjaman berdasarkan musim

fig, ax = plt.subplots(figsize=(6, 5))
ax.bar(season_avg_df['Season'], season_avg_df['Average Bike Rentals'], color='#967259')
ax.set_title('Average Bike Rentals by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Average Bike Rentals')
st.pyplot(fig)

# Visualisasi 2: Line chart untuk peminjaman sepeda per jam pada hari Sabtu
st.subheader('Average Bike Rentals per Hour on Saturday')
st.write("### Data Table: Average Bike Rentals per Hour on Saturday")
st.table(hour_avg_saturday_df)  # Menampilkan tabel rata-rata peminjaman berdasarkan jam pada hari Sabtu

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hour_avg_saturday_df['Hour'], hour_avg_saturday_df['Average Bike Rentals'], marker='o', color='#967259', linestyle='-', linewidth=2, markersize=5)
ax.set_title('Average Bike Rentals per Hour on Saturday')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Bike Rentals')
ax.grid(True)
ax.set_xticks(np.arange(0, 24, 1))  # Set xticks menggunakan np.arange untuk menampilkan seluruh nilai jam
st.pyplot(fig)

# Visualisasi 3: Line chart untuk peminjaman sepeda per jam pada hari Minggu
st.subheader('Average Bike Rentals per Hour on Sunday')
st.write("### Data Table: Average Bike Rentals per Hour on Sunday")
st.table(hour_avg_sunday_df)  # Menampilkan tabel rata-rata peminjaman berdasarkan jam pada hari Minggu

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hour_avg_sunday_df['Hour'], hour_avg_sunday_df['Average Bike Rentals'], marker='o', color='#967259', linestyle='-', linewidth=2, markersize=5)
ax.set_title('Average Bike Rentals per Hour on Sunday')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Bike Rentals')
ax.grid(True)
ax.set_xticks(np.arange(0, 24, 1))  # Set xticks menggunakan np.arange untuk menampilkan seluruh nilai jam
st.pyplot(fig)
