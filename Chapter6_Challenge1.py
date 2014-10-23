#Matt Koppelman
#GIS 501
#Lab 4 Chapter 6 Challenge 1



import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter6/Exercise06/Challenge2Original.gdb"

fclist = arcpy.ListFeatureClasses()

for fc in fclist:
	fcdescribe = arcpy.Describe(fc)
	print fcdescribe.name + " is a " + fcdescribe.shapetype + " feature class"