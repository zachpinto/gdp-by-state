import pandas as pd
import statsmodels.api as sm

# Define the predictor variables (20 sectors) and the response variable (total GDP growth)
X = data.iloc[:, 1:-1]
y = data.iloc[:, -1]

# Fit a linear regression model using statsmodels
model = sm.OLS(y, sm.add_constant(X)).fit()

# Extract the estimated coefficients for each sector
coefs = model.params[1:-1]

# Sort the coefficients in descending order
sorted_coefs = coefs.sort_values(ascending=False)

# Print the top 5 sectors associated with high levels of growth in the total GDP
print("Top 5 sectors:")
print(sorted_coefs.head())

# Print the bottom 5 sectors associated with low levels of growth in the total GDP
print("\nBottom 5 sectors:")
print(sorted_coefs.tail())

X = data.iloc[:, 1:-1]
y = data.iloc[:, -1]

# Fit a linear regression model using statsmodels
model = sm.OLS(y, sm.add_constant(X)).fit()

# Extract the p-values for each sector
p_values = model.pvalues[1:-1]

# Sort the p-values in ascending order
sorted_p_values = p_values.sort_values()

# Print the p-values for each sector
print("P-values:")
print(sorted_p_values)

import pandas as pd
import statsmodels.api as sm

# Define the predictor variables (3 statistically significant sectors) and any other relevant variables
X = data[["Professional, scientific, and technical services", "Manufacturing", "Retail trade"]]
y = data["TOTAL_GDP_GROWTH"]

# Fit a linear regression model using statsmodels
model = sm.OLS(y, sm.add_constant(X)).fit()

# Print the regression results
print(model.summary())

from statsmodels.stats.outliers_influence import variance_inflation_factor

# Calculate the VIF for each predictor variable
vif = pd.DataFrame()
vif["features"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Print the VIF values
print(vif)

# Calculate the residuals from the regression model
residuals = model.resid

# Plot the residuals against the fitted values
plt.scatter(model.fittedvalues, residuals)
plt.title("Residuals vs Fitted Values")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()

# Perform the Breusch-Pagan test for heteroscedasticity
from statsmodels.stats.diagnostic import het_breuschpagan

lm, lm_pvalue, fvalue, f_pvalue = het_breuschpagan(residuals, X)
print("Breusch-Pagan test:")
print("LM statistic: ", lm)
print("LM p-value: ", lm_pvalue)
print("F statistic: ", fvalue)
print("F p-value: ", f_pvalue)

# Define the predictor variables (3 statistically significant sectors) and any other relevant variables
X = data[["Professional, scientific, and technical services", "Manufacturing", "Retail trade"]]
y = data["TOTAL_GDP_GROWTH"]

# Fit a linear regression model using statsmodels
model = sm.OLS(y, sm.add_constant(X)).fit()

# Print the regression results
print(model.summary())

# Fit a simplified model that excludes the non-significant variables
simplified_model = sm.OLS(y, sm.add_constant(X[["Professional, scientific, and technical services", "Manufacturing", "Retail trade"]])).fit()

# Print the regression results for the simplified model
print(simplified_model.summary())

# Compare the performance of the full model and the simplified model using the R-squared and the adjusted R-squared
print("Full Model R-squared:", model.rsquared)
print("Full Model Adjusted R-squared:", model.rsquared_adj)
print("Simplified Model R-squared:", simplified_model.rsquared)
print("Simplified Model Adjusted R-squared:", simplified_model.rsquared_adj)

# Define the predictor variables (3 statistically significant sectors)
X = data[["Professional, scientific, and technical services", "Manufacturing", "Retail trade"]]
y = data["TOTAL_GDP_GROWTH"]

# Create a pairplot to visualize the correlations between the variables
sns.pairplot(data, x_vars=X.columns, y_vars="TOTAL_GDP_GROWTH", kind="reg", height=5)
plt.show()

# Define the predictor variables (3 statistically significant sectors)
X = data[["Professional, scientific, and technical services", "Manufacturing", "Retail trade"]]
y = data["TOTAL_GDP_GROWTH"]

# Calculate the weighted average growth rate of the 3 significant sectors
weights = [1/3, 1/3, 1/3]
sector_growth = (X * weights).sum(axis=1)

# Create a scatterplot to visualize the relationship between the variables
sns.scatterplot(x=sector_growth, y=y)
plt.xlabel("Weighted Average Growth Rate of Significant Sectors")
plt.ylabel("Total GDP Growth Rate")
plt.show()

# Define the predictor variables (3 statistically significant sectors)
X = data[["Professional, scientific, and technical services", "Manufacturing", "Retail trade"]]
y = data["TOTAL_GDP_GROWTH"]

# Calculate the weighted average growth rate of the 3 significant sectors
weights = [1/3, 1/3, 1/3]
weighted_growth = (X * weights).sum(axis=1)

# Create a matrix with the two variables (weighted_growth and TOTAL_GDP_GROWTH)
matrix = pd.concat([weighted_growth, y], axis=1)
matrix.columns = ["Weighted Growth", "Total GDP Growth"]

# Create a heatmap to visualize the relationship between the two variables for all states
sns.heatmap(matrix, cmap="YlGnBu")
plt.xlabel("Total GDP Growth Rate")
plt.ylabel("Weighted Growth Rate of Significant Sectors")
plt.show()



# Define the predictor variables (3 statistically significant sectors)
X = data[["Professional, scientific, and technical services", "Manufacturing", "Retail trade"]]
y = data["TOTAL_GDP_GROWTH"]

# Calculate the weighted average growth rate of the 3 significant sectors
weights = [1/3, 1/3, 1/3]
weighted_growth = (X * weights).sum(axis=1)

# Create a matrix of the two variables (weighted_growth and TOTAL_GDP_GROWTH) for each state
matrix = pd.concat([weighted_growth, y], axis=1)
matrix.columns = ["Weighted Growth", "Total GDP Growth"]
state_names = data["STATE"].tolist()

# Get the 10 states with the highest weighted growth
top_weighted = matrix.nlargest(10, "Weighted Growth")
top_weighted["State"] = top_weighted.index.map(dict(zip(range(len(state_names)), state_names)))

print("States with the highest weighted growth:")
print(top_weighted[["State", "Weighted Growth"]])

# Get the 10 states with the highest total GDP growth
top_total = matrix.nlargest(10, "Total GDP Growth")
top_total["State"] = top_total.index.map(dict(zip(range(len(state_names)), state_names)))

print("\nStates with the highest total GDP growth:")
print(top_total[["State", "Total GDP Growth"]])

# Get the states that appear in both lists
common_states = set(top_weighted.index).intersection(set(top_total.index))

# Create a new matrix for the common states
common_matrix = matrix.loc[common_states]
common_matrix["State"] = common_matrix.index.map(dict(zip(range(len(state_names)), state_names)))

# Create a heatmap to visualize the relationship between the two variables for the common states
sns.heatmap(common_matrix.set_index("State"), cmap="YlGnBu")
plt.xlabel("Total GDP Growth Rate")
plt.ylabel("Weighted Growth Rate of Significant Sectors")
plt.show()

new_data = data
data = pd.read_csv("/home/pintz/dev/analytics/gdp-by-state/data/processed/data.csv")

df = data

# melt the DataFrame to transform it to long format
df_melted = pd.melt(df, id_vars=['STATE', 'SECTOR'], var_name='YEAR', value_name='GDP')

# select the rows for the three sectors of interest
df_sectors = df_melted[df_melted['SECTOR'].isin(['Professional, scientific, and technical services', 'Manufacturing', 'Retail trade'])]

# group by state and year to get the total GDP for each state and year
df_totals = df_sectors.groupby(['STATE', 'YEAR'])['GDP'].sum().reset_index()

# pivot the DataFrame to transform it to wide format
df_pivoted = df_totals.pivot(index='STATE', columns='YEAR', values='GDP')

# select the columns you want to keep and save to a new file
df_final = df_pivoted[['1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
                       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
                       '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']]


df = data

# melt the DataFrame to transform it to long format
df_melted = pd.melt(df, id_vars=['STATE', 'SECTOR'], var_name='YEAR', value_name='GDP')

# select the rows for the three sectors of interest
df_sectors = df_melted[df_melted['SECTOR'].isin(['Accommodation and food services',
                                                 'Administrative and support and waste management and remediation services',
                                                 'Agriculture, forestry, fishing and hunting',
                                                 'Arts, entertainment, and recreation',
                                                 'Construction',
                                                 'Educational services',
                                                 'Finance and insurance',
                                                 'Government and government enterprises',
                                                 'Health care and social assistance',
                                                 'Information',
                                                 'Management of companies and enterprises',
                                                 'Manufacturing',
                                                 'Mining, quarrying, and oil and gas extraction',
                                                 'Other services (except government and government enterprises)',
                                                 'Professional, scientific, and technical services',
                                                 'Real estate and rental and leasing',
                                                 'Retail trade',
                                                 'Transportation and warehousing',
                                                 'Utilities',
                                                 'Wholesale trade'])]

# group by state and year to get the total GDP for each state and year
df_totals = df_sectors.groupby(['STATE', 'YEAR'])['GDP'].sum().reset_index()

# pivot the DataFrame to transform it to wide format
df_pivoted = df_totals.pivot(index='STATE', columns='YEAR', values='GDP')

# select the columns you want to keep and save to a new file
df_final2 = df_pivoted[['1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
                       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
                       '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']]

import pandas as pd
import matplotlib.pyplot as plt

# load the two datasets into pandas dataframes
all_sectors_df = states_all_sectors
significant_sectors_df = states_sig_sectors

# define the list of states to include
states_of_interest = ['North Dakota', 'Arizona', 'California', 'Colorado', 'Utah', 'Idaho', 'Washington']

# create a separate line chart for each of the seven states
for state in states_of_interest:
    # subset the data for the current state
    all_sectors_state_series = all_sectors_df.loc[state]
    significant_sectors_state_series = significant_sectors_df.loc[state]

    # create a larger figure
    plt.figure(figsize=(10, 6))

    # create the line chart with two lines
    plt.plot(all_sectors_state_series.index, all_sectors_state_series.values, label='ALL_SECTORS')
    plt.plot(significant_sectors_state_series.index, significant_sectors_state_series.values, label='SIGNIFICANT_SECTORS')

    # add chart title and axis labels
    plt.title(f'GDP trends for {state}')
    plt.xlabel('Year')
    plt.ylabel('GDP')

    # adjust font size of x-axis tick labels
    plt.xticks(fontsize=6)

    # add legend
    plt.legend()

    # show the plot
    plt.show()

