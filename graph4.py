import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_excel_file.xlsx' with the actual path to your Excel file
excel_file_path = 'F DATA SET.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Assuming your Excel file has a column named 'Category' that contains categorical data
# Replace 'Category' with the actual column name in your Excel file
category_counts = df['Limit usage'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('People Limited their time usage')
plt.show()
