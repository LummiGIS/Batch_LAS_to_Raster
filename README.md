# Batch_LAS_to_Raster
An arcpy/Python script to batch convert LAS in one directory to GeoTiff in a different directory.

This tool requires an installation of ArcGIS Pro.

User defined parameters:

  in_dir = a directory of LAS files
  
  out_dir = a directory to hold the geotiffs
  
  
Run in your favorite Python IDE or in an ArcGIS Pro Python Window.



Include is id_missing_tiles.py.  id_missing_tiles.py takes as inputs the NWIFC/WDFW Photogrammetry tile index shapefile and populates the shapefile with a new attribute.  The script will sift through the resulting directory if tif from batch_las_to_raster.py.  If a tif exists for that polygon extent the script will populate the the attribute with 'yes'.
