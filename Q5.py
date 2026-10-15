import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'Farm_ID': ['F01', 'F02', 'F03', 'F04', 'F05',
                'F06', 'F07', 'F08', 'F09', 'F10',
                'F11', 'F12', 'F13', 'F14', 'F15',
                'F16', 'F17', 'F18', 'F19', 'F20'],

    'Rainfall_mm': [850, 600, 900, 500, 780, 650, 920, 720, 550, 800,
                    880, 620, 760, 940, 580, 820, 700, 960, 540, 790],

    'Temperature': [28, 32, 27, 34, 29, 31, 26, 30, 33, 28,
                    27, 32, 29, 26, 33, 28, 30, 25, 34, 29],

    'Fertilizer_kg': [60, 45, 65, 40, 55, 48, 70, 52, 42, 58,
                      62, 46, 54, 72, 44, 60, 50, 75, 41, 56],

    'Soil_Type': ['Loamy', 'Sandy', 'Loamy', 'Sandy', 'Clay',
                  'Sandy', 'Loamy', 'Clay', 'Sandy', 'Loamy',
                  'Loamy', 'Sandy', 'Clay', 'Loamy', 'Sandy',
                  'Clay', 'Clay', 'Loamy', 'Sandy', 'Clay'],

    'Crop_Yield_kg': [3200, 2100, 3500, 1800, 3000, 2300, 3700, 2800,
                      1900, 3100, 3400, 2200, 2950, 3800, 2000, 3150,
                      2700, 3900, 1850, 3050]
}

df = pd.DataFrame(data)

# Step 2: Display and inspect the dataset
print("First Five Rows:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Calculate overall averages
print("\nOverall Averages:")
print(df[['Rainfall_mm', 'Temperature',
          'Fertilizer_kg', 'Crop_Yield_kg']].mean())

# Step 4: Analyze soil type distribution
print("\nSoil Type Count:")
print(df['Soil_Type'].value_counts())

# Step 5: Analyze average crop yield by soil type
print("\nAverage Crop Yield by Soil Type:")
soil_analysis = df.groupby('Soil_Type')['Crop_Yield_kg'].mean()
print(soil_analysis)

# Step 6: Analyze average crop yield by rainfall and fertilizer usage
print("\nAverage Rainfall, Fertilizer and Yield by Soil Type:")
print(df.groupby('Soil_Type')[
    ['Rainfall_mm', 'Fertilizer_kg', 'Crop_Yield_kg']
].mean())

# Step 7: Identify farms with the highest crop yield
print("\nTop 5 Farms by Crop Yield:")
top_yield = df.nlargest(5, 'Crop_Yield_kg')
print(top_yield[['Farm_ID', 'Soil_Type', 'Crop_Yield_kg']])

# Step 8: Calculate correlation between numerical variables
print("\nCorrelation Matrix:")
print(df[['Rainfall_mm', 'Temperature',
          'Fertilizer_kg', 'Crop_Yield_kg']].corr())

# Step 9: Visualize average crop yield by soil type
soil_analysis.plot(kind='bar')

plt.title('Average Crop Yield by Soil Type')
plt.xlabel('Soil Type')
plt.ylabel('Average Crop Yield (kg)')
plt.show()

# Step 10: Visualize rainfall vs crop yield
plt.scatter(df['Rainfall_mm'], df['Crop_Yield_kg'])

plt.title('Rainfall vs Crop Yield')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Crop Yield (kg)')
plt.show()

# Step 11: Visualize fertilizer usage vs crop yield
plt.scatter(df['Fertilizer_kg'], df['Crop_Yield_kg'])

plt.title('Fertilizer Usage vs Crop Yield')
plt.xlabel('Fertilizer (kg)')
plt.ylabel('Crop Yield (kg)')
plt.show()

# Step 12: Visualize temperature vs crop yield
plt.scatter(df['Temperature'], df['Crop_Yield_kg'])

plt.title('Temperature vs Crop Yield')
plt.xlabel('Temperature')
plt.ylabel('Crop Yield (kg)')
plt.show()