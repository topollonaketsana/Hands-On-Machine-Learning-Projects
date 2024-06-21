import os
import tarfile
from six.moves import urllib
import pandas as pd

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH): 
    if not os.path.isdir(housing_path): 
        os.makedirs(housing_path)
        print(f"Created directory: {housing_path}")
    else:
        print(f"Directory already exists: {housing_path}")
    
    tgz_path = os.path.join(housing_path, "housing.tgz")
    print(f"Downloading data from {housing_url} to {tgz_path}")
    urllib.request.urlretrieve(housing_url, tgz_path)
    
    print(f"Extracting {tgz_path} to {housing_path}")
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    print("Extraction complete.")

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    print(f"Loading data from {csv_path}")
    if not os.path.isfile(csv_path):
        print(f"CSV file not found: {csv_path}")
        return None
    return pd.read_csv(csv_path)

# Fetch the data
fetch_housing_data()

# Load the data
housing = load_housing_data()
if housing is not None:
    print(housing.head())
else:
    print("Failed to load housing data.")
