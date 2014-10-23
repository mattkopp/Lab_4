#Matt Koppelman
#GIS 501
#Lab 4 Chapter 6 Challenge 2



import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter6/Exercise06/Challenge2Original.gdb"

arcpy.CreateFileGDB_management("C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter6", "Challenge2New.gdb")

fclist = arcpy.ListFeatureClasses("*", 'POLYGON')

for fc in fclist:
	fcdesc = arcpy.Describe(fc)
	arcpy.CopyFeatures_management(fc, "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter6/Challenge2New.gdb/" + fcdesc.basename)