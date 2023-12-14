import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
df = pd.read_excel('F DATA SET.xlsx')

# Convert threats to lowercase or uppercase and remove leading and trailing spaces
df['consumption'] = df['consumption'].str.upper().str.strip()

# Split values in the 'threat' column
df['consumption'] = df['consumption'].str.split(';')

# Explode the lists to create separate rows for each threat
df = df.explode('consumption')

# Count the occurrences of each threat
threat_counts = df['consumption'].value_counts()

# Plotting the bar graph
fig, ax = plt.subplots()
threat_counts.plot(kind='bar', color='lightpink', edgecolor='black', ax=ax)

# Adding labels and title
plt.xlabel('Media Consumed')
plt.ylabel('No. of Users')
plt.title('Social Media Trends')

# Add percentage annotations
total_count = len(df['consumption'])
for i, count in enumerate(threat_counts):
    percentage = (count / total_count) * 100
    ax.text(i, count + 1, f'{percentage:.2f}%', ha='center', va='bottom', fontsize=6)

# Rotate x-axis labels for better readability
plt.xticks(rotation=30, ha='right')

# Display the plot
plt.show()