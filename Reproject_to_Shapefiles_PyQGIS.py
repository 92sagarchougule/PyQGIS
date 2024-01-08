from qgis.core import QgsVectorLayer, QgsCoordinateReferenceSystem, QgsVectorFileWriter
import os

# Source directory containing the shapefiles
source_directory_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/cad_data"

# Destination directory to save the reprojected shapefiles
destination_directory_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/D_Code_Data"

# Target CRS (WGS84)
target_crs = 'EPSG:4326'

# Function to reproject and save the shapefile
def reproject_and_save(source_directory, destination_directory, filename, target_crs):
    source_shapefile_path = os.path.join(source_directory, filename)
    destination_shapefile_path = os.path.join(destination_directory, filename)

    print(f"Reprojecting from {source_shapefile_path} to {destination_shapefile_path}")

    # Load the source shapefile
    source_layer = QgsVectorLayer(source_shapefile_path, 'layer_name', 'ogr')

    # Set the source layer's CRS
    source_layer.setCrs(QgsCoordinateReferenceSystem(source_layer.crs()))

    # Reproject the layer to the target CRS
    reprojected_layer = source_layer.clone()
    reprojected_layer.setCrs(QgsCoordinateReferenceSystem(target_crs))

    # Save the reprojected layer
    QgsVectorFileWriter.writeAsVectorFormat(reprojected_layer, destination_shapefile_path, 'UTF-8', QgsCoordinateReferenceSystem(target_crs), 'ESRI Shapefile')

# Get the list of shapefiles in the source directory
shapefile_list = [f for f in os.listdir(source_directory_path) if f.endswith(".shp")]

# Iterate through the list of shapefiles
for shapefile in shapefile_list:
    print(f"Processing shapefile: {shapefile}")

    # Reproject and save each shapefile
    reproject_and_save(source_directory_path, destination_directory_path, shapefile, target_crs)

print('Reprojection completed.')
