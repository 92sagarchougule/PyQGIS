from qgis.core import QgsVectorLayer, QgsProject
import os

# Directory containing the shapefiles
directory_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles_Rename"

# Function to check if the field "VINCODE" is available in a shapefile
def check_field_availability(shapefile_path, field_name):
    layer = QgsVectorLayer(shapefile_path, "temp_layer", "ogr")
    if not layer.isValid():
        print(f"Invalid layer: {shapefile_path}")
        return False

    fields = [field.name() for field in layer.fields()]
    return field_name in fields

# Field to check for
field_to_check = "PIN"

# Iterate through each shapefile in the directory
for file_name in os.listdir(directory_path):
    if file_name.endswith(".shp"):
        shapefile_path = os.path.join(directory_path, file_name)
        field_available = check_field_availability(shapefile_path, field_to_check)
        
        if field_available:
            print(f"Field '{field_to_check}' is available in shapefile: {file_name}")
        else:
            print(f"Field '{field_to_check}' is not available in shapefile: {file_name}")
