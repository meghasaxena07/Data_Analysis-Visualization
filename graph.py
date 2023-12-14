import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
df = pd.read_excel('F DATA SET.xlsx')

# Convert platform names to lowercase or uppercase and remove leading and trailing spaces
df['Platform'] = df['Platform'].str.upper().str.strip()

# Split values in the 'platform' column
df['Platform'] = df['Platform'].str.split(',')

# Explode the lists to create separate rows for each platform
df = df.explode('Platform')

# Count the occurrences of each platform
platform_counts = df['Platform'].value_counts()

# Plotting the bar graph
fig, ax = plt.subplots()
platform_counts.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)

# Adding labels and title
plt.xlabel('Platform')
plt.ylabel('No. of Users')
plt.title('Platform Distribution')

# Add percentage annotations
total_count = len(df['Platform'])
for i, count in enumerate(platform_counts):
    percentage = (count / total_count) * 100
    ax.text(i, count + 1, f'{percentage:.2f}%', ha='center', va='bottom', fontsize=8)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.show()