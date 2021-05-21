#!/usr/bin/env python3
'''
Identify those areas without coverage.
1. Add a new field to the shapefile tile index.
2.Cursor through the rows and check if the tif exists for that tile.
3. Update attribute with yes or now depending on if tif exists.
'''

__author__ = 'Gerry Gabrisch/Lummi GIS Division'
__date__ = 'May 2021'
__copyright__ = '(C) 2021, Lummi Indian Business Council'
__license__ = "MIT"
__version__ = "1.0"
__email__ = "geraldg@lummi-nsn.gov"
__status__ = "Production"

import sys
import traceback
import os
import arcpy



try:
    
    
    #The input directory of tif files
    in_fc = r'K:\WDFWPhotogrammetryDSM\tile_indexes\WRIA_4_Upper_Skagit_TILES.shp'
    #the WRIA tile shape file.
    in_dir = r'K:\WDFWPhotogrammetryDSM\WRIA4UpperSkagit'


    #check to see if the field exists, if not add it...
    desc = arcpy.Describe(in_fc)
    flds = desc.fields
    for fld in flds:
        if fld.name == 'is_tile':
            pass
        else:
            arcpy.AddField_management(in_fc, "is_tile", "TEXT", field_length=3)


    cursor = arcpy.UpdateCursor(in_fc)
    for row in cursor:
        #get the tile name...
        tif = row.getValue('TILE')+ '.tif'
        #build the path to the tif...
        tif = str(os.path.join(in_dir, tif))
        print('working on: ', tif)
        if os.path.exists(tif):
            row.setValue("is_tile", 'yes')
        else:
            row.setValue("is_tile", 'no')
        cursor.updateRow(row)

    del row
    del cursor
        
        













    
    
##    def file_name(file, out_dir):
##        '''build the new file path and name'''
##        file_list = file.split("\\")
##        file_name = file_list[-1]
##        file_name = file_name.split(".")[0]
##        out_file = file_name+ '.tif'
##        out_file =  os.path.join(out_dir, out_file)
##        return out_file
##    
##
##    for root, dirs, files in os.walk(in_dir):
##        for file in files:
##            if(file.endswith("")):
##                out_file = file_name(file, out_dir)
##                in_las = os.path.join(root, file)
##               
##                print('Working on: ',in_las)
##                kwargs = {'value_field': 'ELEVATION', 'data_type': 'FLOAT', 'sampling_type': 'CELLSIZE', 'sampling_value':5.0, 'z_factor':3.28084}
##                arcpy.conversion.LasDatasetToRaster(in_las, out_file, **kwargs)    
##  

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
