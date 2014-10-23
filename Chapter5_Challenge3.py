#Matt Koppelman
#GIS 501
#Lab 4 Chapter 5 Challenge 2


import arcpy
Parks = "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter5/Exercise05/parks.shp"
ParksOutput = "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter5/Exercise05/Results/parks_Dissolve.shp"

arcpy.management.Dissolve(Parks, ParksOutput, ["PARK_TYPE"], "", "SINGLE_PART", "")