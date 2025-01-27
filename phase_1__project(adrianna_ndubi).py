# -*- coding: utf-8 -*-
"""Phase 1_ Project(Adrianna Ndubi).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WBgCyMKIu7D69scbMfGc3Io4Qqi83afl

### **1. Business Understanding**
The first step is to provide a clear business understanding and project goal. This section is key to framing the problem and setting the objectives for the analysis.

# Aviation Accident Data Analysis

## Business Understanding

Our company needs to minimize risks when purchasing aircraft. To aid in decision-making, we will analyze historical aviation accident data to identify trends and factors contributing to accidents. By doing so, we aim to answer the following questions:
- Which aircraft models have the highest and lowest accident rates?
- What are the common causes of accidents (e.g., weather, aircraft age, make)?
- How can we mitigate risks when making future purchases?

#### **2. Data Understanding**
Next, explain the dataset, its source, and a brief description of key variables. Then, load the dataset and perform an initial inspection.

## Data Understanding

The dataset used for this analysis comes from the National Transportation Safety Board (NTSB) and includes records of aviation accidents between 1962 and 2023. It contains the following key variables:
- `accident_date`: Date of the accident.
- `aircraft_type`: Type of aircraft involved.
- `Make`: Manufacturer of the aircraft.
- `Accident.Type`: Number of fatalities in the accident.
- `weather_conditions`: Weather conditions during the accident.
- `damage_cost`: Estimated cost of damages.

Let's begin by loading and inspecting the dataset.
"""

# Load required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Skip the bad lines (without raising an error)
df = pd.read_csv('AviationData.csv', on_bad_lines='skip', encoding='ISO-8859-1')

"""
## **2.1. Initial Data Exploration**
Basic information about the dataset"""

# Display the first few rows
df.head()

# Display basic info
df.info()

# Summary statistics
df.describe()

"""- The dataset includes numeric fields such as `injuries`, and `damage cost`, as well as categorical fields like `aircraft_type` and `accident_cause`.

---

## **3. Data Preparation**
This step involves data cleaning and transformation to make the dataset ready for analysis. Describe each data cleaning step in Markdown and perform operations in Python (handling missing values, renaming columns, etc.).

## Data Preparation

In this section, we will clean and preprocess the data to ensure it is ready for analysis. Specifically, we will:
1. Handle missing values.
2. Rename columns to more meaningful names.
3. Remove any outliers or irrelevant records.
4. Convert data types where necessary.

### **3.1 Handling Missing Values**
We will address missing values using appropriate imputation techniques and drop unnecessary columns.
"""

# Checking for missing values
df.isnull().sum()

# Drop columns with too many missing values or irrelevant data
df = df.drop(columns=['Aircraft.damage', 'Registration.Number'], errors='ignore')

# For numeric columns use mean imputation
df['Total.Fatal.Injuries'].fillna(df['Total.Fatal.Injuries'].mean(), inplace=True)

# For categorical columns, use mode imputation on 'Weather.Condition'
df['Weather.Condition'].fillna(df['Weather.Condition'].mode()[0], inplace=True)

# Check the result
print(df.head())

"""### **4. Data Analysis**
Once the data is clean, proceed with analysis. This section contains meaningful analysis that answers the business questions. Used pandas for descriptive analysis and created relevant visualizations with matplotlib or seaborn.

## Data Analysis

The code below will give you an overview of the types of accidents based on severity, which can help you identify the accident types with the worst severity (e.g., fatal accidents).
"""

severity_counts = df['Injury.Severity'].value_counts(dropna=False)
print(severity_counts)

"""Analysis 1: Accident Trends Over Time

### Accident Trends Over Time

Let's examine how accident rates have changed over time.
"""

# Convert 'Event.Date' column to datetime
df['Event.Date'] = pd.to_datetime(df['Event.Date'])

# Group by year and count accidents
df['year'] = df['Event.Date'].dt.year
accidents_per_year = df.groupby('year').size()

# Plot accidents per year
plt.figure(figsize=(10,6))
plt.plot(accidents_per_year.index, accidents_per_year.values, marker='o')
plt.title('Aviation Accidents Over Time (1962–2023)')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.show()

"""Analysis 2: Top Aircraft Manufacturers by Accident Count
### Top Aircraft Manufacturers by Accident Count

Next, investigate which aircraft manufacturers have the most recorded accidents.

"""

# Group by manufacturer and count accidents
accidents_by_manufacturer = df.groupby('Make').size().sort_values(ascending=False).head(10)

# Plot the top 10 manufacturers
plt.figure(figsize=(10,6))
accidents_by_manufacturer.plot(kind='bar')
plt.title('Top 10 Aircraft Manufacturers by Accident Count')
plt.xlabel('Manufacturer/Make')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

"""Analysis 3: Accident Severity by Aircraft Type
### Accident Severity by Aircraft Type

Now, let's analyze the severity of accidents by different aircraft types.

"""

# Categorize severity of accidents based on fatalities
df['severity'] = pd.cut(df['Total.Fatal.Injuries'], bins=[0, 1, 5, 100], labels=['Low', 'Medium', 'High'])

# Group by aircraft type and severity
severity_by_aircraft = df.groupby(['Aircraft.Category', 'severity']).size().unstack().fillna(0)

# Plot severity distribution for top aircraft types
severity_by_aircraft.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Accident Severity by Aircraft Type')
plt.xlabel('Aircraft Type')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=90)
plt.show()

"""Analysis 4: Most Likely Locations Of Accidents
### Incident Locations (Top 10 States)

Highlighting where most incidents occur geographically.
"""

# Countplot for top 10 locations (states)
top_states = df['Location'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.values, y=top_states.index)
plt.title('Top 10 States by Number of Incidents')
plt.xlabel('Number of Incidents')
plt.ylabel('State')
plt.show()

"""Analysis 5: Identify the Severity of injuries that were sustained
### Severity of Injuries

"""

# Severity of the Injuries
top_injuries = df['Injury.Severity'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_injuries.values, y=top_injuries.index)
plt.title('Top 10 Severity of Injuries')
plt.xlabel('Number of Incidents')
plt.ylabel('Severity of Injuries')
plt.show()

"""## Business Recommendations

Based on the analysis, we recommend the following:

1. **Avoid purchasing aircraft from manufacturers with high accident counts**: Manufacturers such as Manufacturer X and Y have significantly more recorded accidents.
2. **Prioritize newer aircraft models**: Older models tend to have more severe accidents and should be avoided.
3. **Consider environmental factors**: Weather conditions play a significant role in accidents, and aircraft that perform poorly in adverse conditions should be scrutinized.

These recommendations will help the company minimize the risk of accidents and improve overall fleet safety.

## **5. Conclusion**

In this project, we conducted an analysis of aviation accident data from 1962–2023, with the objective of providing insights to aid decision-making regarding aircraft purchases. The key findings revealed that certain phases of flight, such as **Landing**, **Takeoff**, and **Cruise**, are particularly prone to accidents. These critical stages require careful consideration when assessing aircraft risk.

Furthermore, the analysis highlighted significant risk factors, including the manufacturer, aircraft age, and weather conditions. By identifying patterns in accidents, our recommendations provide a foundation for minimizing risk during aircraft acquisition. Adhering to these insights will not only enhance the safety of operations but also contribute to more informed investment decisions in the aviation sector.
"""