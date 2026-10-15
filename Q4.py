import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'Customer_ID': ['C01', 'C02', 'C03', 'C04', 'C05',
                    'C06', 'C07', 'C08', 'C09', 'C10',
                    'C11', 'C12', 'C13', 'C14', 'C15',
                    'C16', 'C17', 'C18', 'C19', 'C20'],

    'Income': [45000, 25000, 60000, 22000, 50000,
               30000, 70000, 28000, 55000, 24000,
               65000, 35000, 48000, 26000, 75000,
               32000, 52000, 27000, 68000, 23000],

    'Credit_Score': [720, 580, 750, 560, 710,
                     600, 780, 590, 730, 570,
                     760, 620, 700, 585, 790,
                     610, 725, 575, 770, 555],

    'Loan_Amount': [200000, 150000, 300000, 120000, 250000,
                    180000, 350000, 160000, 270000, 130000,
                    320000, 200000, 240000, 140000, 400000,
                    190000, 260000, 150000, 330000, 125000],

    'Employment_Type': [
        'Salaried', 'Self-employed', 'Salaried', 'Unemployed',
        'Salaried', 'Self-employed', 'Salaried', 'Self-employed',
        'Salaried', 'Unemployed', 'Salaried', 'Self-employed',
        'Salaried', 'Unemployed', 'Salaried', 'Self-employed',
        'Salaried', 'Self-employed', 'Salaried', 'Unemployed'
    ],

    'Loan_Status': [
        'Approved', 'Rejected', 'Approved', 'Rejected',
        'Approved', 'Rejected', 'Approved', 'Rejected',
        'Approved', 'Rejected', 'Approved', 'Rejected',
        'Approved', 'Rejected', 'Approved', 'Rejected',
        'Approved', 'Rejected', 'Approved', 'Rejected'
    ]
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
print(df[['Income', 'Credit_Score', 'Loan_Amount']].mean())

# Step 4: Count loan approval status
print("\nLoan Status Count:")
print(df['Loan_Status'].value_counts())

total = len(df)
approved = (df['Loan_Status'] == 'Approved').sum()
rejected = (df['Loan_Status'] == 'Rejected').sum()

print("\nTotal Customers:", total)
print("Approved Loans:", approved)
print("Rejected Loans:", rejected)
print("Approval Percentage:", (approved / total) * 100)

# Step 5: Compare approved and rejected applications
analysis = df.groupby('Loan_Status')[
    ['Income', 'Credit_Score', 'Loan_Amount']
].mean()

print("\nAverage Financial Details by Loan Status:")
print(analysis)

# Step 6: Analyze employment type and loan status
print("\nEmployment Type vs Loan Status:")
print(pd.crosstab(df['Employment_Type'], df['Loan_Status']))

# Step 7: Visualize loan approval status
df['Loan_Status'].value_counts().plot(kind='bar')

plt.title('Loan Approval Status Distribution')
plt.xlabel('Loan Status')
plt.ylabel('Number of Customers')
plt.show()

# Step 8: Visualize average financial details
analysis.plot(
    kind='bar',
    subplots=True,
    layout=(1, 3),
    figsize=(12, 4),
    legend=False
)

plt.suptitle('Average Financial Details by Loan Status')
plt.tight_layout()
plt.show()

# Step 9: Visualize employment type and loan status
pd.crosstab(
    df['Employment_Type'],
    df['Loan_Status']
).plot(kind='bar')

plt.title('Employment Type vs Loan Status')
plt.xlabel('Employment Type')
plt.ylabel('Number of Customers')
plt.xticks(rotation=0)
plt.show()