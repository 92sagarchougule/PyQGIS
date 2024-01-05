from qgis.core import QgsVectorLayer, QgsProject
import os

# Directory containing the shapefiles
directory_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles_Rename"

# Function to get the count of features in a shapefile
def count_features(shapefile_path):
    layer = QgsVectorLayer(shapefile_path, "temp_layer", "ogr")
    if not layer.isValid():
        print(f"Invalid layer: {shapefile_path}")
        return 0

    feature_count = layer.featureCount()
    return feature_count

# Iterate through each shapefile in the directory
for file_name in os.listdir(directory_path):
    if file_name.endswith(".shp"):
        shapefile_path = os.path.join(directory_path, file_name)
        features_count = count_features(shapefile_path)
        
        print(f"Shapefile: {file_name}, Feature Count: {features_count}")
v

#"VINCODE" "PIN"