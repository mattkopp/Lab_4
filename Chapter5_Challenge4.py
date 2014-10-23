#Matt Koppelman
#GIS 501
#Lab 4 Chapter 5 Challenge 2



import arcpy

Extensions = ["3D", "Network", "Spatial"]


for extension in Extensions:
	if arcpy.CheckExtension(extension) == "Available":
		print extension + " Analyst is available"
	else:
		print extension + " Analyst is not available"
	
	
	
