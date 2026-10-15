import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'Patient_ID': ['P01', 'P02', 'P03', 'P04', 'P05',
                   'P06', 'P07', 'P08', 'P09', 'P10',
                   'P11', 'P12', 'P13', 'P14', 'P15',
                   'P16', 'P17', 'P18', 'P19', 'P20'],

    'Age': [45, 32, 55, 28, 60, 40, 52, 35, 48, 30,
            62, 38, 50, 27, 58, 42, 46, 34, 53, 29],

    'Sugar_Level': [145, 98, 180, 90, 200, 120, 165, 105, 155, 95,
                    210, 115, 170, 88, 190, 130, 150, 100, 175, 92],

    'BP': [130, 118, 145, 110, 150, 125, 140, 120, 135, 115,
           155, 122, 142, 108, 148, 128, 132, 116, 144, 112],

    'BMI': [28, 23, 31, 22, 34, 26, 30, 24, 29, 23,
            35, 25, 30, 21, 33, 27, 28, 24, 31, 22],

    'Disease_Status': ['Yes', 'No', 'Yes', 'No', 'Yes',
                       'No', 'Yes', 'No', 'Yes', 'No',
                       'Yes', 'No', 'Yes', 'No', 'Yes',
                       'No', 'Yes', 'No', 'Yes', 'No']
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
print(df[['Age', 'Sugar_Level', 'BP', 'BMI']].mean())

# Step 4: Count disease status
print("\nDisease Status Count:")
print(df['Disease_Status'].value_counts())

total = len(df)
disease = (df['Disease_Status'] == 'Yes').sum()
no_disease = (df['Disease_Status'] == 'No').sum()

print("\nTotal Patients:", total)
print("Patients with Disease:", disease)
print("Patients without Disease:", no_disease)
print("Disease Percentage:", (disease / total) * 100)

# Step 5: Compare health parameters by disease status
analysis = df.groupby('Disease_Status')[
    ['Age', 'Sugar_Level', 'BP', 'BMI']
].mean()

print("\nAverage Health Parameters by Disease Status:")
print(analysis)

# Step 6: Visualize disease status count
df['Disease_Status'].value_counts().plot(kind='bar')

plt.title('Disease Status Distribution')
plt.xlabel('Disease Status')
plt.ylabel('Number of Patients')
plt.show()

# Step 7: Visualize average health parameters
analysis.plot(
    kind='bar',
    subplots=True,
    layout=(2, 2),
    figsize=(10, 7),
    legend=False
)

plt.suptitle('Average Health Parameters by Disease Status')
plt.tight_layout()
plt.show()

