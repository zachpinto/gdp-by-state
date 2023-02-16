# Convert "1997" and "2021" columns to numeric values
data["1997"] = pd.to_numeric(data["1997"])
data["2021"] = pd.to_numeric(data["2021"])

# Calculate the overall GDP growth for each state
state_gdp = data.groupby("STATE").sum()
state_gdp_growth = ((state_gdp["2021"] - state_gdp["1997"]) / state_gdp["1997"]) * 100

# Find the top 5 and bottom 5 states by GDP growth
top_5_states = state_gdp_growth.nlargest(5)
bottom_5_states = state_gdp_growth.nsmallest(5)

# Loop through the states and print out the top 3 sectors with the highest growth rate
for state in state_gdp_growth.index:
    label = ""
    if state in top_5_states.index:
        label = "(Top 5)"
    elif state in bottom_5_states.index:
        label = "(Bottom 5)"
    if label:
        print(f"\nTop 3 growing sectors in {state} {label}:")
        state_data = data[data["STATE"] == state]
        sector_gdp = state_data.groupby("SECTOR").sum()
        sector_growth = ((sector_gdp["2021"] - sector_gdp["1997"]) / sector_gdp["1997"]) * 100
        top_3_sectors = sector_growth.nlargest(3)
        print(top_3_sectors)
Top 3 growing sectors in Alaska (Bottom 5
