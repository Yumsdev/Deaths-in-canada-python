import matplotlib.pyplot as plt

# Data for drug overdose deaths in Canadian provinces (fictional dataset for illustration purposes)
provinces = [
    "British Columbia", "Alberta", "Saskatchewan", "Manitoba", "Ontario",
    "Quebec", "New Brunswick", "Nova Scotia", "Prince Edward Island",
    "Newfoundland and Labrador", "Yukon", "Northwest Territories", "Nunavut"
]
deaths = [1600, 1200, 400, 500, 2500, 1500, 200, 300, 100, 150, 80, 50, 20]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(provinces, deaths, color='skyblue')
plt.xlabel('Number of Overdose Deaths (2023) / CODE BY Jordan Jones')
plt.title('Drug Overdose Deaths by Province in Canada (2023)')
plt.gca().invert_yaxis()  # Invert y-axis for better readability

# Display the chart
plt.tight_layout()
plt.show()
