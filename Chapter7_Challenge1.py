#Matt Koppelman
#GIS 501
#Lab 4 Chapter 7 Challenge 1



import arcpy
from arcpy import env
env.workspace = "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_4/Chapter7/Exercise07"



infc = "airports.shp"
outAirport = "ChallengeResults/airports.shp"
outAirportBuffer = "ChallengeResults/airports_buffer.shp"
outSeaplane = "ChallengeResults/seaplanebase.shp"
outSeaplaneBuffer = "ChallengeResults/seaplanebase_buffer.shp"

delimiter = arcpy.AddFieldDelimiters(infc, "FEATURE")


arcpy.Select_analysis(infc, outAirport, delimiter + " = 'Airport'")
arcpy.analysis.Buffer(outAirport, outAirportBuffer, "15000 METERS")

arcpy.Select_analysis(infc, outSeaplane, delimiter + " = 'Seaplane Base'")
arcpy.analysis.Buffer(outSeaplane, outSeaplaneBuffer, "7500 METERS")
