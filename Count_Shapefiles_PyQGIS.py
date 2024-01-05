import os

def count_shapefiles(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Count the number of shapefiles
    shapefile_count = sum(file.lower().endswith(".shp") for file in files)

    return shapefile_count

# Specify the directory containing shapefiles
shapefile_directory = "C:/Users/sagar.chougule/Desktop/cropsap/data/Shapefiles_Rename"

# Call the function to count shapefiles in the specified directory
number_of_shapefiles = count_shapefiles(shapefile_directory)

print(f"Number of shapefiles in {shapefile_directory}: {number_of_shapefiles}")
