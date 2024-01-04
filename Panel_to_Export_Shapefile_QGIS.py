import os
from qgis.core import QgsVectorLayer

# Specify the output directory for shapefiles
output_dir = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles"

# Ensure the output directory exists, create it if necessary
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the list of layers from the Layers Panel
layers = QgsProject.instance().layerTreeRoot().layerOrder()

# Iterate through layers and export them to shapefiles
for layer in layers:
    if isinstance(layer, QgsVectorLayer):
        layer_name = layer.name()

        # Create the output shapefile path
        output_shapefile = os.path.join(output_dir, f"{layer_name}.shp")

        # Create a new vector layer with the same CRS as the original layer
        new_layer = QgsVectorLayer("Point?crs=" + layer.crs().authid(), "temporary_layer", "memory")
        new_layer.startEditing()

        # Copy features from the original layer to the new layer
        new_layer.addFeatures(layer.getFeatures())

        # Save the new layer to a shapefile
        QgsVectorFileWriter.writeAsVectorFormat(new_layer, output_shapefile, "utf-8", layer.crs(), "ESRI Shapefile")

        # Stop editing and remove the temporary layer
        new_layer.commitChanges()
        new_layer = None

        print(f"Exported {layer_name} to {output_shapefile}")

print("Shapefile export completed.")
