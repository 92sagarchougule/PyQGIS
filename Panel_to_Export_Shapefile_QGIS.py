import os
from qgis.core import QgsVectorLayer, QgsVectorFileWriter

# Specify the path to the file geodatabase (GDB)
gdb_path = "C:/Users/sagar.chougule/Desktop/cropsap/data/Maha_Parcel.gdb"

# Specify the output directory for shapefiles
output_dir = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles"

# Ensure the output directory exists, create it if necessary
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the GDB using OGR
gdb_layer = QgsVectorLayer(gdb_path, "gdb_layer", "ogr")

# Get the list of layers from the Layers Panel
layers = QgsProject.instance().layerTreeRoot().layerOrder()

# Iterate through layers and export them to shapefiles
for layer in layers:
    if isinstance(layer, QgsVectorLayer):
        layer_name = layer.name()

        # Create the output shapefile path
        output_shapefile = os.path.join(output_dir, f"{layer_name}.shp")

        # Export the layer to a shapefile
        QgsVectorFileWriter.writeAsVectorFormat(layer, output_shapefile, "utf-8", layer.crs(), "ESRI Shapefile")

        print(f"Exported {layer_name} to {output_shapefile}")

print("Shapefile export completed.")
