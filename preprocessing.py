import os
from osgeo import gdal

import rasterio

import pandas as pd
import geopandas as gpd
from shapely.geometry import mapping, Point, Polygon
from shapely.ops import cascaded_union

import numpy as np
import matplotlib.pyplot as plt


def generate_mask(raster_path, shape_path, output_path, file_name):
    
    """Function that generates a binary mask from a vector file (shp or geojson)
    
    raster_path = path to the .tif;

    shape_path = path to the shapefile or GeoJson.

    output_path = Path to save the binary mask.

    file_name = Name of the file.
    
    """
    
    #load raster
    
    with rasterio.open(raster_path, "r") as src:
        raster_img = src.read()
        raster_meta = src.meta
    
    #load o shapefile ou GeoJson
    train_df = gpd.read_file(shape_path)

    #Function that generates the mask
    def poly_from_utm(polygon, transform):
        poly_pts = []

        poly = cascaded_union(polygon)
        for i in np.array(poly.exterior.coords):

            poly_pts.append(~transform * tuple(i))

        new_poly = Polygon(poly_pts)
        return new_poly
    
    
    poly_shp = []
    im_size = (src.meta['height'], src.meta['width'])
    for num, row in train_df.iterrows():
        if row['geometry'].geom_type == 'Polygon':
            poly = poly_from_utm(row['geometry'], src.meta['transform'])
            poly_shp.append(poly)
        else:
            for p in row['geometry']:
                poly = poly_from_utm(p, src.meta['transform'])
                poly_shp.append(poly)

    mask = rasterio.rasterize(shapes=poly_shp,
                     out_shape=im_size)
    
    #Salve
    mask = mask.astype("uint8")
    
    bin_mask_meta = src.meta.copy()
    bin_mask_meta.update({'count': 1})
    os.chdir(output_path)
    with rasterio.open(file_name, 'w', **bin_mask_meta) as dst:
        dst.write(mask, 1)


def generate_empty_mask(raster_path, output_path, file_name):
    
    """Function that generates an empty binary mask (all 0) from a vector file (shp or geojson). Used for patches where there is no target object.
    
    raster_path = path to the .tif;

    shape_path = path to the shapefile or GeoJson.

    output_path = Path to save the binary mask.

    file_name = Name of the file.
    
    """
    
    #load raster
    
    with rasterio.open(raster_path, "r") as src:
        raster_img = src.read()
        raster_meta = src.meta
    im_size = (src.meta['height'], src.meta['width'])
    
    mask = np.zeros(im_size)
    
    #Save
    mask = mask.astype("uint8")
    
    bin_mask_meta = src.meta.copy()
    bin_mask_meta.update({'count': 1})
    os.chdir(output_path)
    with rasterio.open(file_name, 'w', **bin_mask_meta) as dst:
        dst.write(mask, 1)


#Change the path to your directory

#For Google Colaboratory users, update the directory:
Data_folder = "./data/"
#For Jupyter Notebook users, update the directory:
#Data_folder = "Wildebeest-UNet/SampleData/1_Data_preparation"

IMAGE_PATH = os.path.join(Data_folder, "22MAR25134903-P3DS-014983717010_01_P001.tif")
ROI_PATH = os.path.join(Data_folder, "roi")
MASK_PATH = os.path.join(Data_folder, "mask")


if __name__ == "__main__":
    for f in sorted(os.listdir(IMAGE_PATH)):
        #print(f)
        fdir = os.path.join(IMAGE_PATH, f)
        image_name, ext = os.path.splitext(f)
        if ext.lower() == ".tif":
            ID = image_name
            print(ID)

            match_status = 0
            for f in sorted(os.listdir(ROI_PATH)):
                roi_dir = os.path.join(ROI_PATH, f)
                mask_name, ext = os.path.splitext(f)
                if ext.lower() == ".shp":
                    roi_ID = mask_name
                    print(roi_ID)
                    

                    if roi_ID == ID:
                        generate_mask(fdir, roi_dir, MASK_PATH, ID+'.tif')
                        print("Generated FN mask image " + ID)
                        match_status = 1
                        
            if match_status == 0:
                
                generate_empty_mask(fdir, MASK_PATH, ID+'.tif')
                print("Generated FP mask image " + ID)          