import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
data = pd.read_csv("E:\Downloads\George Mason\\Employee_Payroll.csv")

# Descriptive statistics of dataset
numerical_columns = ['Fiscal_Year', 'Fiscal_Quarter', 'Fiscal_Period', 'First_Name', 'Last_Name', 'Middle_Init', 'Bureau', 'Office', 'Office_Name', 'Job_Code', 'Job_Title', 'Base_Pay', 'Position_ID', 'Employee_Identifier', 'Original_Hire_Date']

descriptive_stats = data[numerical_columns].describe().transpose()
print(descriptive_stats)

# Excluding rows with missing 'Base Pay'
data_clean = data.dropna(subset=['Base_Pay'])

# Analysis for question (i): Average Base Pay Change Over Fiscal Years by Job Title
# We'll group by 'Fiscal Year' and 'Job Title', and calculate the mean 'Base Pay'
average_base_pay = data_clean.groupby(['Fiscal_Year', 'Job_Title'])['Base_Pay'].mean().reset_index()

# For visualization, we'll select a few job titles to keep the plot readable
selected_job_titles = average_base_pay['Job_Title'].value_counts().nlargest(5).index
average_base_pay_selected = average_base_pay[average_base_pay['Job_Title'].isin(selected_job_titles)]

# Plotting the data
plt.figure(figsize=(12, 6))
sns.lineplot(data=average_base_pay_selected, x='Fiscal_Year', y='Base_Pay', hue='Job_Title', marker='o')
plt.title('Average Base Pay Change Over Fiscal Years by Job Title')
plt.xlabel('Fiscal Year')
plt.ylabel('Average Base Pay')
plt.xticks(rotation=45)
plt.legend(title='Job Title')
plt.tight_layout()
plt.show()

# Analysis for question (ii): Bureaus with Highest and Lowest Average Base Pays Across Fiscal Quarters
# Grouping by 'Fiscal Quarter' and 'Bureau', and calculating the mean 'Base Pay'
average_base_pay_bureau = data_clean.groupby(['Fiscal_Quarter', 'Bureau'])['Base_Pay'].mean().reset_index()

# Selecting the top 5 and bottom 5 bureaus based on overall average base pay
top_bureaus = average_base_pay_bureau.groupby('Bureau')['Base_Pay'].mean().nlargest(5).index
bottom_bureaus = average_base_pay_bureau.groupby('Bureau')['Base_Pay'].mean().nsmallest(5).index

# Filtering data for selected bureaus
average_base_pay_selected_bureaus = average_base_pay_bureau[average_base_pay_bureau['Bureau'].isin(top_bureaus.union(bottom_bureaus))]

# Plotting the data
plt.figure(figsize=(15, 8))
sns.lineplot(data=average_base_pay_selected_bureaus, x='Fiscal_Quarter', y='Base_Pay', hue='Bureau', marker='o', style='Bureau')
plt.title('Average Base Pay Across Fiscal Quarters for Selected Bureaus')
plt.xlabel('Fiscal Quarter')
plt.ylabel('Average Base Pay')
plt.xticks(rotation=45)
plt.legend(title='Bureau', loc='upper left')
plt.tight_layout()
plt.show()

# Analysis for question (iii): Trend in Hiring Over the Years
# Extracting the year from the 'Original Hire Date'
data_clean['Original_Hire_Date'] = pd.to_datetime(data['Original_Hire_Date'], errors = 'coerce')
data_clean['Hire Year'] = data_clean['Original_Hire_Date'].dt.year

# Counting the number of hires per year
hiring_trend = data_clean.groupby('Hire Year')['Employee_Identifier'].nunique().reset_index()

# Plotting the data
plt.figure(figsize=(12, 6))
sns.barplot(data=hiring_trend, x='Hire Year', y='Employee_Identifier')
plt.title('Trend in Hiring Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Hires')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()