import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
df = pd.read_csv('math_scores.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Calculate some basic statistics on the math scores
print(df['math_score'].describe())

# Create a histogram of the math scores
plt.hist(df['math_score'], bins=20)
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.show()

# Create a scatterplot of math scores vs. reading scores
plt.scatter(df['reading_score'], df['math_score'])
plt.xlabel('Reading Score')
plt.ylabel('Math Score')
plt.show()
