import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Step 1: Load / create the dataset
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Temperature': [30, 32, 31, 29, 33, 35, 34],
    'Sales': [200, 220, 210, 190, 250, 300, 280],
    'Rainfall': [5, 2, 0, 8, 1, 0, 3]
}
df = pd.DataFrame(data)
 
# Step 2: Explore the dataset
print(df.head())
print(df.describe())
 
# Step 3: Line plot - trend of Temperature over Days
plt.figure(figsize=(6, 4))
plt.plot(df['Day'], df['Temperature'], marker='o', color='blue')
plt.title('Temperature Trend Over the Week')
plt.xlabel('Day')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.show()
 
# Step 4: Bar plot - Sales comparison across Days
plt.figure(figsize=(6, 4))
plt.bar(df['Day'], df['Sales'], color='orange')
plt.title('Sales Comparison Across Days')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.show()
 
# Step 5: Scatter plot - relationship between Temperature and Sales
plt.figure(figsize=(6, 4))
plt.scatter(df['Temperature'], df['Sales'], color='green')
plt.title('Temperature vs Sales')
plt.xlabel('Temperature (C)')
plt.ylabel('Sales')
plt.show()
 
# Step 6: Correlation matrix
corr_matrix = df[['Temperature', 'Sales', 'Rainfall']].corr()
print("\nCorrelation Matrix:\n", corr_matrix)
 
# Step 7: Heatmap using Seaborn
plt.figure(figsize=(5, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
