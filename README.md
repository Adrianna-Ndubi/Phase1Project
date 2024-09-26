# Phase1Project
Adrianna Ndubi
Link to the Slide Presentation: https://prezi.com/view/52OdAswJlmhgs19sfKsx/

plt.figure(figsize=(10, 6))
sns.barplot(x=top_injuries.values, y=top_injuries.index) # Changed top_causes to top_injuries
plt.title('Top 10 Severity of Injuries')
plt.xlabel('Number of Incidents')
plt.ylabel('Severity of Injuries')
plt.show()
---

# Aviation Accident Data Analysis

## Overview

This project involves analyzing aviation accident data from the National Transportation Safety Board (NTSB), covering the years 1962 to 2023. The goal is to provide insights to aid the company’s aviation division in making informed decisions regarding aircraft purchases. By identifying trends in accident data and determining high-risk aircraft models, we aim to minimize future risks associated with fleet expansion.

## Business Understanding

### Stakeholders
The primary stakeholders for this project are the decision-makers in the aviation division of the company, particularly those responsible for fleet management and purchasing new aircraft.

### Key Business Questions
The analysis addresses the following key business questions:
1. Which aircraft models have the highest and lowest accident rates, and should they be avoided or prioritized for purchase?
2. What factors contribute most to aviation accidents (e.g., manufacturer, weather conditions, or age of the aircraft)?
3. How can the company mitigate risks and enhance safety when expanding its fleet?

## Data Understanding and Analysis

### Source of Data
The dataset used in this analysis was sourced from the National Transportation Safety Board (NTSB) and contains records of aviation accidents from 1962 to 2023. The dataset includes the following key variables:
- `accident_date`: The date of the aviation accident.
- `aircraft_type`: The type of aircraft involved.
- `manufacturer`: The aircraft manufacturer.
- `fatalities`: Number of fatalities in the accident.
- `weather_conditions`: Weather conditions at the time of the accident.
- `damage_cost`: The estimated cost of damage caused by the accident.

### Data Analysis and Visualizations

1. **Accident Trends Over Time**
   - This visualization shows how the number of accidents has changed over the years. There are spikes in certain periods that could be linked to external factors such as economic conditions or changes in aviation technology.
   
   ![Accidents Over Time](link-to-your-image)

2. **Top 10 Aircraft Manufacturers by Accident Count**
   - The analysis highlights the top aircraft manufacturers by accident count. Manufacturers such as X and Y have a higher number of accidents, suggesting that further investigation into their aircraft's reliability is warranted.
   
   ![Top 10 Manufacturers](link-to-your-image)

3. **Accident Severity by Aircraft Type**
   - This visualization categorizes accidents by severity (low, medium, high) and shows the distribution of severity across different aircraft types. It helps identify which aircraft are more prone to serious accidents.
   
   ![Accident Severity](link-to-your-image)

## Conclusion

### Summary of Findings

1. **Manufacturer Risk**: Certain manufacturers, such as X and Y, are associated with a significantly higher number of accidents. These manufacturers should be carefully evaluated before making purchasing decisions.
   
2. **Aircraft Age**: Older aircraft models are more likely to be involved in severe accidents. Therefore, prioritizing newer models for future purchases will help reduce risk.
   
3. **Weather Conditions**: Adverse weather plays a crucial role in accidents. Aircraft that perform poorly under specific weather conditions should be avoided, and weather-resistant aircraft should be prioritized.

By following these recommendations, the company can make more informed decisions that will reduce risks and improve the overall safety of the fleet.

---

**Note:** The placeholders for visualizations (`![...](link-to-your-image)`) should be replaced with actual image URLs or embedded images from your GitHub repository.

