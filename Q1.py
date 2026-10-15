import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'Student_ID': ['S01', 'S02', 'S03', 'S04', 'S05',
                   'S06', 'S07', 'S08', 'S09', 'S10',
                   'S11', 'S12', 'S13', 'S14', 'S15',
                   'S16', 'S17', 'S18', 'S19', 'S20'],

    'Attendance': [92, 55, 78, 60, 88, 47, 95, 72, 50, 83,
                   66, 90, 58, 76, 62, 85, 45, 80, 68, 53],

    'Study_Hours': [5, 2, 4, 3, 5, 1, 6, 3, 2, 4,
                    3, 5, 2, 4, 3, 5, 1, 4, 3, 2],

    'Internal_Marks': [45, 24, 38, 28, 42, 20, 48, 35, 22, 40,
                       30, 44, 25, 36, 29, 41, 18, 39, 32, 23],

    'Result': ['Pass', 'Fail', 'Pass', 'Fail', 'Pass',
               'Fail', 'Pass', 'Pass', 'Fail', 'Pass',
               'Fail', 'Pass', 'Fail', 'Pass', 'Fail',
               'Pass', 'Fail', 'Pass', 'Pass', 'Fail']
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
print(df[['Attendance', 'Study_Hours',
          'Internal_Marks']].mean())

# Step 4: Count Pass and Fail students
print("\nResult Count:")
print(df['Result'].value_counts())

total = len(df)
passed = (df['Result'] == 'Pass').sum()
failed = (df['Result'] == 'Fail').sum()

print("\nTotal Students:", total)
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Pass Percentage:", (passed / total) * 100)

# Step 5: Compare Pass and Fail students
analysis = df.groupby('Result')[
    ['Attendance', 'Study_Hours', 'Internal_Marks']
].mean()

print("\nAverage Performance by Result:")
print(analysis)

# Step 6: Visualize Pass and Fail counts
df['Result'].value_counts().plot(kind='bar')

plt.title('Pass vs Fail Student Count')
plt.xlabel('Result')
plt.ylabel('Number of Students')
plt.show()

# Step 7: Visualize average performance
analysis.plot(kind='bar', subplots=True,
              layout=(1, 3), figsize=(12, 4),
              legend=False)

plt.suptitle('Average Performance by Result')
plt.tight_layout()
plt.show()