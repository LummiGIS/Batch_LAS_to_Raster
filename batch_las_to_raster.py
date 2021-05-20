'''Converts all las files in a directory (and any subdirectories) to a raster format.  The resulting rasters have their vertical datums transformed from WGS84(EGM96) to NAVD88'''

import sys
import traceback
import os
import arcpy
arcpy.env.overwriteOutput = True
try:
    in_dir = r'F:\2019DSM\test'
    for root, dirs, files in os.walk(in_dir):
        for file in files:
            if(file.endswith(".las")):
                in_las = os.path.join(root, file)
                out_ras = in_las.replace('.las', '.tif')
                print('Working on: ',in_las)
        
                kwargs = {'value_field': 'ELEVATION', 'data_type': 'FLOAT', 'sampling_type': 'CELLSIZE', 'sampling_value':5.0, 'z_factor':3.28084}
                arcpy.conversion.LasDatasetToRaster(in_las, out_ras, **kwargs)    
    
                #arcpy.ProjectRaster_management("image.tif", "reproject.tif", "World_Mercator.prj","BILINEAR", "5", "NAD_1983_To_WGS_1984_5", "#", "#")                















    

except arcpy.ExecuteError: 
    # Get the tool error messages 
    msgs = arcpy.GetMessages(2) 

    # Return tool error messages for use with a script tool 
    arcpy.AddError(msgs) 

    # Print tool error messages for use in Python
    print(msgs)

except:
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    # Return Python error messages for use in script tool or Python window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

    # Print Python error messages for use in Python / Python window
    print(pymsg)
    print(msgs)