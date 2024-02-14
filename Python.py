import pandas as pd

df = pd.read_csv('input_data.csv')

df.drop_duplicates(inplace=True)

df['Age'] = df['Age'].apply(lambda x: int(x))

df['Salary_EGP'] = df['Salary_USD'] * 30.80

avg_age = df['Age'].mean()
median_salaries = df['Salary_EGP'].median()
ratio_males_females = df['Gender'].value_counts(normalize=True)

print(f'Average age: {avg_age}')
print(f'Median salaries: {median_salaries}')
print(f'Ratio between males and female employees: {ratio_males_females}')

df.to_csv('output_data.csv', index=False)