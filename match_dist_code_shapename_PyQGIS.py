from qgis.core import QgsVectorLayer
import os

# List of dtncode and dtename pairs
dtncode_dtename_list = [
    (510, 'Yavatmal'),
    (524, 'Latur'),
    (512, 'Hingoli'),
    (503, 'Amravati'),
    (521, 'Pune'),
    (513, 'Parbhani'),
    (520, 'Raigad'),
    (501, 'Akola'),
    (508, 'Gadchiroli'),
    (509, 'Chandrapur'),
    (523, 'Beed'),
    (502, 'Washim'),
    (497, 'Nandurbar'),
    (601, 'Palghar'),
    (506, 'Bhandara'),
    (517, 'Thane'),
    (525, 'Osmanabad'),
    (528, 'Ratnagiri'),
    (530, 'Kolhapur'),
    (507, 'Gondiya'),
    (531, 'Sangli'),
    (511, 'Nanded'),
    (526, 'Solapur'),
    (500, 'Buldana'),
    (516, 'Nashik'),
    (514, 'Jalna'),
    (527, 'Satara'),
    (505, 'Nagpur'),
    (498, 'Dhule'),
    (499, 'Jalgaon'),
    (522, 'Ahmednagar'),
    (504, 'Wardha'),
    (515, 'Aurangabad'),
    (529, 'Sindhudurg')
]


# Directory containing the shapefiles
directory_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles_Rename"

# Function to check if a shapefile with a specific dtename exists
def check_shapefile_existence(directory, dtename):
    shapefile_name = f"{dtename}.shp"
    shapefile_path = os.path.join(directory, shapefile_name)
    return os.path.exists(shapefile_path)

# Get the list of shapefiles in the directory
shapefile_list = [f for f in os.listdir(directory_path) if f.endswith(".shp")]

# Iterate through the list of shapefiles
for shapefile in shapefile_list:
    # Extract dtename from the shapefile name
    dtename = shapefile.split(".shp")[0]

    # Check if the dtename is present in the folder shapefiles
    if check_shapefile_existence(directory_path, dtename):
        print(f"Shapefile {shapefile} exists for dtename {dtename}.")
    else:
        print(f"Shapefile {shapefile} does not exist for dtename {dtename}.")