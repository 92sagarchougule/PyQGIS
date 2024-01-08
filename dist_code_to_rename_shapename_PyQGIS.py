from qgis.core import QgsVectorLayer, QgsVectorFileWriter, QgsCoordinateReferenceSystem
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

# Source directory containing the shapefiles
source_directory_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles_Rename"

# Destination directory to save the renamed shapefiles
destination_directory_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/cad_data"

# Function to check if a shapefile with a specific dtename exists
def check_shapefile_existence(directory, dtename):
    shapefile_name = f"{dtename}.shp"
    shapefile_path = os.path.join(directory, shapefile_name)
    return os.path.exists(shapefile_path)

# Function to rename and save the shapefile
def save_shapefile_with_rename(source_directory, destination_directory, dtename, new_name):
    source_shapefile_path = os.path.join(source_directory, f"{dtename}.shp")
    destination_shapefile_path = os.path.join(destination_directory, f"{new_name}.shp")

    print(f"Copying from {source_shapefile_path} to {destination_shapefile_path}")

    # Load the source shapefile
    source_layer = QgsVectorLayer(source_shapefile_path, 'layer_name', 'ogr')

    # Get the source layer's CRS
    crs = source_layer.crs()

    # Save the layer with the new name
    QgsVectorFileWriter.writeAsVectorFormat(source_layer, destination_shapefile_path, 'UTF-8', crs, 'ESRI Shapefile')

# Get the list of shapefiles in the source directory
shapefile_list = [f for f in os.listdir(source_directory_path) if f.endswith(".shp")]

# Iterate through the list of shapefiles
for shapefile in shapefile_list:
    # Extract dtename from the shapefile name
    dtename = shapefile.split(".shp")[0]

    print(f"Processing shapefile: {shapefile}, dtename: {dtename}")

    # Check if the dtename is present in the source folder shapefiles
    if check_shapefile_existence(source_directory_path, dtename):
        # Find the corresponding dtncode for the dtename
        dtncode = next(item[0] for item in dtncode_dtename_list if item[1] == dtename)

        # Rename and save the shapefile with dtncode
        new_name = f"{dtncode}"
        print(f"Renaming and saving as: {new_name}")
        save_shapefile_with_rename(source_directory_path, destination_directory_path, dtename, new_name)
        print(f"Shapefile {shapefile} for dtename {dtename} exists. Renamed and saved as {new_name}.")
    else:
        print(f"Shapefile {shapefile} does not exist for dtename {dtename}.")

print('Script completed.')
