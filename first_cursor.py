import pandas as pd

# Create an example dataframe for a tutorial on data analysis
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'San Francisco', 'London', 'Paris', 'Tokyo'],
    'Salary': [50000, 75000, 80000, 65000, 45000],
    'Experience': [2, 5, 8, 3, 1]
})

# Display the first few rows of the dataframe
print(df.head())

# Basic information about the dataframe
print(df.info())

# Summary statistics of numerical columns
print(df.describe())

