import csv
import os

# Specify the source and destination folder paths
src_folder = os.path.join(os.path.expanduser("~"), "Downloads")
dest_folder = os.path.join(os.path.expanduser("~"), "/home/pintz/dev/analytics/gdp-by-state/gdp-by-state/data/interim")

# Specify the name of the CSV file
filename = "interim.csv"

# Load the CSV file from the source folder
with open(os.path.join(src_folder, filename), "r") as src_file:
    reader = csv.reader(src_file)
    data = list(reader)

# Write the data to the destination folder
with open(os.path.join(dest_folder, filename), "w", newline="") as dest_file:
    writer = csv.writer(dest_file)
    writer.writerows(data)

print(f"The file {filename} has been moved from {src_folder} to {dest_folder}")
