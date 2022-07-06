import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


plt.figure(figsize=(10,6))
plt.title("title")

# Add plot function here

# Force legend to appear
plt.legend()

plt.xlabel("xlabel")
plt.ylabel("ylabel")


###############################


# plot both together to compare
fig, ax=plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0])
ax[0].set_title("Original Data")
sns.histplot(normalized_data, ax=ax[1])
ax[1].set_title("Normalized data")
plt.show()


###############################
# Axes-level functions
###############################

flights = sns.load_dataset("flights")
may_flights = flights.query("month == 'May'")
sns.lineplot(data=may_flights, x="year", y="passengers")

flights_wide = flights.pivot("year", "month", "passengers")
sns.lineplot(data=flights_wide["May"])

sns.lineplot(data=flights_wide)

sns.lineplot(data=flights, x="year", y="passengers")
sns.lineplot(data=flights, x="year", y="passengers", hue="month", style="month")

###############################

sns.histplot(data=penguins, x="flipper_length_mm")
sns.histplot(data=penguins, x="flipper_length_mm", bins=30)
sns.histplot(data=penguins, x="flipper_length_mm", kde=True)
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", element="step")

###############################

sns.kdeplot(data=tips, x="total_bill")
sns.kdeplot(data=tips, x="total_bill", hue="time")
sns.kdeplot(data=tips, x="total_bill", hue="time", multiple="stack")

# 1 KDE plot for 3 data files containing 3 species
sns.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", fill=True)
sns.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", fill=True)
sns.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", fill=True)

###############################

sns.barplot(x="day", y="total_bill", data=tips)
sns.barplot(x="day", y="total_bill", hue="sex", data=tips)

###############################

flights = sns.load_dataset("flights")
flights_wide = flights.pivot("month", "year", "passengers")
sns.heatmap(flights_wide)
# Annotate each cell with the numeric value using integer formatting
sns.heatmap(flights_wide, annot=True, fmt="d")

###############################

sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time")

###############################

# Create a scatter plot with a regression line that best fits the data
sns.regplot(x="total_bill", y="tip", data=tips)
# A second order
sns.regplot(x="total_bill", y="tip", data=tips, order=2)

###############################

# Create a categorical scatter plot
sns.swarmplot(x=tips["total_bill"])
sns.swarmplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)


###############################
# Figure-level functions
###############################

# sns.relplot (Default kind="scatter")

sns.relplot(data=tips, x="total_bill", y="tip", hue="day")
# Assigning a col variable creates a faceted figure with multiple subplots arranged 
# across the columns of the grid
sns.relplot(data=tips, x="total_bill", y="tip", hue="day", col="time")
# Different variables can be assigned to facet on both the columns and rows
sns.relplot(data=tips, x="total_bill", y="tip", hue="day", col="time", row="sex")

# sns.relplot (kind="line")

sns.relplot(data=flights_wide, kind="line")
sns.relplot(data=fmri, x="timepoint", y="signal", col="region", hue="event", style="event", kind="line")

###############################

# sns.displot (Default kind="hist")

sns.displot(choc_data['rating'])
sns.displot(data=penguins, x="flipper_length_mm")
sns.displot(data=penguins, x="flipper_length_mm", kind="kde")
sns.displot(data=penguins, x="flipper_length_mm", kde=True)
sns.displot(data=penguins, x="flipper_length_mm", hue="species", kind="kde")
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="sex", kind="kde")

###############################

# sns.catplot (Default kind="strip")

sns.catplot(x="time", y="pulse", hue="kind", data=exercise)
sns.catplot(x="time", y="pulse", hue="kind", data=exercise, kind="boxen")
sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=exercise)

###############################

# Create a scatter plot with a regression line that best fits the data
sns.lmplot(x="total_bill", y="tip", data=tips)
# Create a scatter plot with two regression lines, correspoding to smokers and nonsmokers
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)
