"""
    This program creates two shapefiles. The first shapefile is a 250ft buffer of the power
    line from the input PowerLine.shp file. The second shapefile contains the parcels from
    the Parcels.shp file contained by the buffer.
"""

import os
import sys
import ogr
import gdalconst
import math

# Implement directory exception and change directory if folder exists.
directory = raw_input("Please enter the directory for both shapefiles: ")
try:
    os.chdir(directory)
except:
    print "\nCan't open",directory,".","Please try again."
    exit()

plFile = 'PowerLine.shp'
outBuffer = 'Buffer_250ft'

# Assigning a value to the variable bufferWidth. The value is in ft as the layer's CS is in ft.
bufferWidth = 250
# Get drivers apporpiate for input and output files
inDriver1 = ogr.GetDriverByName('ESRI Shapefile')
outDriver = ogr.GetDriverByName('ESRI Shapefile')
# Open the file using the driver
inDataSource1 = inDriver1.Open(plFile,0)
# Get the layer from datasource
powerLine = inDataSource1.GetLayer()
# Get the layer's spatial ref
spatialRef = powerLine.GetSpatialRef()
SRS = spatialRef
# Get the layer's extent
extent = powerLine.GetExtent()

# remove output shapefile if it already exists
if os.path.exists(outBuffer):
   outDriver.DeleteDataSource(outBuffer)

# Open the file using the driver
outDataSource = outDriver.CreateDataSource(outBuffer)
# Create a layer in the output file
outLayer1 = outDataSource.CreateLayer(outBuffer,SRS,geom_type=ogr.wkbMultiPolygon)
# Checks if the layer was successfully created
if outLayer1 is None:
   print "couldn't create layer for buffer in output DS"
   exit(1)
# Set up features for the output layer and
# add new buffer feature to the output layer.
outLayerDef = outLayer1.GetLayerDefn()
oldFeature1 = powerLine.GetNextFeature()
geom = oldFeature1.GetGeometryRef()
buff = geom.Buffer(bufferWidth)
newFeature1 = ogr.Feature(outLayerDef)
newFeature1.SetGeometry(buff)
newFeature1.SetFID(0)
outLayer1.CreateFeature(newFeature1)

inDataSource1.Destroy()
outDataSource.Destroy()


pFile = 'Parcels.shp'
# get driver apporpiate for input file
inDriver2 = ogr.GetDriverByName('ESRI Shapefile')
# open the file using the driver
inDataSource2 = inDriver2.Open(pFile,0)

# verify the file was openned
if inDataSource2 is None:
   print 'Failed to open file'
   sys.exit(1)
   
# get the layer from datasource
parcels = inDataSource2.GetLayer(0)  

outFile = 'Parcels_Buffer.shp'
outDriver = ogr.GetDriverByName('ESRI Shapefile')

# remove output shapefile if it already exists
if os.path.exists(outFile):
   outDriver.DeleteDataSource(outFile)

# create the output shapefile  
outDataSource = outDriver.CreateDataSource(outFile)
SRS = spatialRef
outLayer = outDataSource.CreateLayer(outFile, SRS, geom_type=ogr.wkbMultiPolygon)

if outLayer is None:
   print "couldn't create layer for buffer in output DS"
   exit(1)

# Add input layer fields to the output layer.
inLayerDefn = parcels.GetLayerDefn()

for i in range(0,inLayerDefn.GetFieldCount()):
    fieldDefn = inLayerDefn.GetFieldDefn(i)
    fieldName = fieldDefn.GetName()
    outLayer.CreateField(fieldDefn)

# Get the output layers feature definition   
outLayerDefn = outLayer.GetLayerDefn()

# Add features to the output layer
for inFeature in parcels:
    # Create output feature
    outFeature = ogr.Feature(outLayerDefn)

    # Add field values from input layer
    for i in range (0,outLayerDefn.GetFieldCount()):
        fieldDefn = outLayerDefn.GetFieldDefn(i)
        filedName = fieldDefn.GetName()
        outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(),inFeature.GetField(i))

    # set geometry
    geometry = inFeature.GetGeometryRef()
    if buff.Contains(geometry):
        outFeature.SetGeometry(geometry.Clone())
        # Add new feature to output layer
        outLayer.CreateFeature(outFeature)

inDataSource2.Destroy()
outDataSource.Destroy()

