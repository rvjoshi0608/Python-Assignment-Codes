import pandas as pd
 
# Step 1: Create sample data (or read from file: pd.read_csv('data.csv'))
data = {
    'Name': ['Amit', 'Sneha', 'Rahul', 'Amit', 'Priya', None],
    'Marks': [85, 90, None, 85, 78, 92],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', None, 'Nagpur']
}
df = pd.DataFrame(data)
 
print("Original DataFrame:\n", df)
 
# Step 2: Explore the dataset
print("\nFirst rows:\n", df.head())
print("\nInfo:")
df.info()
print("\nStatistical Summary:\n", df.describe())
 
# Step 3: Check missing values
print("\nMissing values:\n", df.isnull().sum())
 
# Step 4: Handle missing values
df_dropped = df.dropna()                     # remove rows with any missing value
df_filled = df.fillna({'Name': 'Unknown', 'Marks': df['Marks'].mean(), 'City': 'Unknown'})
 
print("\nAfter dropna():\n", df_dropped)
print("\nAfter fillna():\n", df_filled)
 
# Step 5: Check and remove duplicates
print("\nDuplicate rows:\n", df_filled.duplicated())
df_no_duplicates = df_filled.drop_duplicates()
print("\nAfter removing duplicates:\n", df_no_duplicates)
 
# Step 6: Data selection using loc[]
print("\nStudents with Marks > 80:\n", df_no_duplicates.loc[df_no_duplicates['Marks'] > 80])
print("\nOnly Name and Marks columns:\n", df_no_duplicates.loc[:, ['Name', 'Marks']])
