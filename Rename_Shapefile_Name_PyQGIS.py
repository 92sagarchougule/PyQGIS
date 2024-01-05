from qgis.core import QgsVectorLayer, QgsProject
import os

# Input and output directories
input_dir = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles"
output_dir = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles_Rename"

# Iterate through each file in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".shp"):
        # Construct the full paths for input and output
        input_path = os.path.join(input_dir, file_name)
        
        # Rename the shapefile removing "Maha_Parcel —" and "_Parcel"
        output_name = file_name.replace("Maha_Parcel — ", "").replace("_Parcel", "")
        output_path = os.path.join(output_dir, output_name)

        # Load the input shapefile
        layer = QgsVectorLayer(input_path, file_name, "ogr")
        
        # Save the layer to the new location with the modified name
        QgsVectorFileWriter.writeAsVectorFormat(layer, output_path, "utf-8", layer.crs(), "ESRI Shapefile")

        # Remove the layer from the QGIS project
        QgsProject.instance().removeMapLayer(layer)

# Refresh the QGIS project to reflect the changes
QgsProject.instance().reload()
