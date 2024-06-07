import geopandas as gpd

# Load a GeoPackage file
gdf = gpd.read_file("./data/test.gpkg")  # type: ignore

# Further operations
print(gdf.head())  # type: ignore
