import pandas as pd
import matplotlib.pyplot as plt

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
ages = [21, 22, 20, 23, 21]
scores = [88, 92, 95, 70, 85]

df = pd.DataFrame({'Name': names, 'Age': ages, 'Score': scores})

print("Average Score:", df['Score'].mean())
print("Highest Score:", df['Score'].max())
print("Number of Students:", len(df))

new_student = pd.DataFrame({'Name': ['Frank'], 'Age': [22], 'Score': [90]})
df = pd.concat([df, new_student], ignore_index=True)

print("\nUpdated DataFrame:")
print(df)

plt.bar(df['Name'], df['Score'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores of Students')
plt.show()

plt.hist(df['Age'], bins=[20, 21, 22, 23, 24], edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Students')
plt.title('Distribution of Ages')
plt.show()

