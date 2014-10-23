#Matt Koppelman
#GIS 501
#Lab 4 Chapter 7 Challenge 2


import arcpy
from arcpy import env
env.workspace = "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter7/Exercise07"



fc = "ChallengeResults/roads.shp"


arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)

cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])

for row in cursor:
	if row[0] == "Ferry Crossing":
		row[1] = "YES"
	else:
		row[1]= "NO"
	cursor.updateRow(row)