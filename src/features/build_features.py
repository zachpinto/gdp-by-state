# Adding overall growth rate from 1997-2021 for each sector-state pairing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the growth rate for each sector and state
df['GDP_1997'] = df['1997']
df['GDP_2021'] = df['2021']
df['Growth Rate'] = (df['GDP_2021'] - df['GDP_1997']) / df['GDP_1997']

# Pivot the data to have one row per state and one column per sector
pivoted_data = df.pivot(index='STATE', columns='SECTOR', values='Growth Rate')

# Create a heatmap using seaborn
fig, ax = plt.subplots(figsize=(12, 12))
sns.heatmap(pivoted_data, cmap='YlGnBu', annot=True, fmt='.2f', ax=ax)

# Set plot title and axis labels
ax.set_title('GDP Growth Rates by Sector and State')
ax.set_xlabel('Sector')
ax.set_ylabel('State')

# Show the plot
plt.show()
#%%
df
#%%
# Create Nominal GDP change and weighted growth rate
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the absolute change in GDP for each sector and state
df['GDP_1997'] = df['1997']
df['GDP_2021'] = df['2021']
df['GDP_Change'] = df['GDP_2021'] - df['GDP_1997']

# Calculate the weighted growth rate for each sector and state
df['Growth Rate'] = (df['GDP_2021'] - df['GDP_1997']) / df['GDP_1997']
df['Weighted Growth Rate'] = df['Growth Rate'] * df['GDP_Change'].abs()

# Pivot the data to have one row per state and one column per sector
pivoted_data = df.pivot(index='STATE', columns='SECTOR', values='Weighted Growth Rate')

# Create a heatmap using seaborn
fig, ax = plt.subplots(figsize=(12, 12))
sns.heatmap(pivoted_data, cmap='YlGnBu', annot=False, cbar=True, ax=ax)

# Set plot title and axis labels
ax.set_title('Weighted GDP Growth Rates by Sector and State')
ax.set_xlabel('Sector')
ax.set_ylabel('State')

# Show the plot
plt.show()
#%%
df
#%%
# create STATE_CODE and SECTOR_CODE categorical encodings for cluster analysis
from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder object for the STATE variable
state_encoder = LabelEncoder()

# Encode the STATE variable
df['STATE_CODE'] = state_encoder.fit_transform(df['STATE'])

# Create a LabelEncoder object for the SECTOR variable
sector_encoder = LabelEncoder()

# Encode the SECTOR variable
df['SECTOR_CODE'] = sector_encoder.fit_transform(df['SECTOR'])
#%%
df
#%%
# Drop the last 7 columns using iloc
df = df.iloc[:, :-7]
df
#%%
data = df
data
#%%
# Create new df for regression analysis
# Each row is a state's record of overall growth rate by sector from 1997-2021
# Creating total GDP growth as final feature as response variable

# Create a pivot table to calculate the overall growth rate of each sector for each state
pivoted = pd.pivot_table(data, values=["1997", "2021"], index="STATE", columns="SECTOR", aggfunc=sum)

# Calculate the overall growth rate for each sector for each state
sector_growth_rates = (pivoted["2021"] - pivoted["1997"]) / pivoted["1997"] * 100

# Calculate the total GDP growth rate for each state
state_gdp = data.groupby("STATE").sum()
state_growth_rates = ((state_gdp["2021"] - state_gdp["1997"]) / state_gdp["1997"]) * 100

# Add a name to the Series for the total GDP growth rate
state_growth_rates.name = "TOTAL_GDP_GROWTH"

# Join the sectoral growth rates and the total GDP growth rates
new_data = sector_growth_rates.join(state_growth_rates)

# Reset the index to include the "STATE" column
new_data = new_data.reset_index()

# Save the new dataset to a CSV file
new_data.to_csv("/home/pintz/dev/analytics/gdp-by-state/data/processed/new_data.csv", index=False)

new_data