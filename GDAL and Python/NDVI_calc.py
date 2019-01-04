"""
    This program calculates the Normalized Difference Vegetation Index
        from two .tif files (red and near infrared bands)and creates an output .tif file.
"""

import os 
import gdal # make gdal available
import gdalconst
import numpy as N # package for array processing

##mydir = ('C:\\work\\lab7\\landsat\\')

# Implement directory exception and change directory if folder exists.
directory = raw_input("Please enter the directory for the landsat folder (e.g., C:\work\lab7\landsat):")
try:
    os.chdir(directory)
except:
    print "\nCan't open",directory,".","Please try again."
    exit()


# Assign file names to variables.
redFile = 'L71026029_02920000609_B30_CLIP.tif'
nirFile = 'L71026029_02920000609_B40_CLIP.tif'


# Create two objects from two files.
redBand = gdal.Open(redFile,gdalconst.GA_Update)
if redBand is None:
    print "Couldn't open",redFile
    exit(1)

nirBand = gdal.Open(nirFile,gdalconst.GA_Update)
if nirBand is None:
    print "Couldn't open",nirFile
    exit(1)


cols = redBand.RasterXSize
rows = redBand.RasterYSize
total = cols*rows
print total


red = 1.0*redBand.ReadAsArray() #read the entire file
nir = 1.0*nirBand.ReadAsArray() #read the entire file

checkZero = N.logical_and(red > 0, nir > 0) # apply condition to both arrays that check for 0 in data
NDVI = N.where(checkZero,(nir - red)/(nir + red),1) # use where() method with specified conditions

geo = redBand.GetGeoTransform() # assign geo coordinates of the redBand file to a variable
proj = redBand.GetProjection()  # assign projection of the redBand file to a variable
shape = red.shape # dimensions of the array
format = 'GTiff'
outDriver = gdal.GetDriverByName(format) # get driver for Tiff format
# Create file named NDVI with specified amount of columns, rows, and bands, and value type.
outNDVI = outDriver.Create('NDVI.tif',shape[1],shape[0],1,gdal.GDT_Float32) 
outNDVI.SetGeoTransform(geo) # set geo coordinates
outNDVI.SetProjection(proj) # set projection
outNDVI.GetRasterBand(1).WriteArray(NDVI)
outNDVI = None # save and close file.
print "\nNVDI.tif file has been created.\n"

