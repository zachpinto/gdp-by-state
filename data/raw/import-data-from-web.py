import os
import zipfile
import requests

zip_url = "https://apps.bea.gov/regional/histdata/releases/0922gdpstate/SAGDP.zip"
file_name = "SAGDP9N__ALL_AREAS_1997_2021.csv"
downloads_folder = "/home/pintz/Downloads"
destination_folder = "/home/pintz/dev/analytics/gdp-by-state/gdp-by-state/data/raw"

try:
    response = requests.get(zip_url)
    response.raise_for_status()
    file_path = os.path.join(downloads_folder, "files.zip")
    with open(file_path, "wb") as f:
        f.write(response.content)
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extract(file_name, downloads_folder)
    extracted_file_path = os.path.join(downloads_folder, file_name)
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, file_name)
    os.rename(extracted_file_path, destination_path)
except requests.exceptions.RequestException as e:
    print("Error:", e)
