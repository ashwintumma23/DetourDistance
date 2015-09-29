##########################################################################3
# Program to find the shorter detour distance 
##########################################################################3
import math


def distanceBetweenPoints(latitude1, longitude1, latitude2, longitude2):
	# The input values are in degrees, but Haversine needs the values to be 
	# computed in radians
	
	latitude1 = degreesToRadians(latitude1)
	longitude1 = degreesToRadians(longitude1)
	latitude2 = degreesToRadians(latitude2)
	longitude2 = degreesToRadians(longitude2)

	latDifference = latitude2 - latitude1
	longDifference = longitude2 - longitude1
		
	alpha  = math.pow(math.sin(latDifference/2),2) + math.cos(latitude1) * math.cos(latitude2) * math.pow(math.sin(longDifference/2),2);
	c  = 2 * math.atan2(math.sqrt(alpha),math.sqrt(1-alpha)); 
	
	radiusOfEarth = 3961
	return c * radiusOfEarth

def degreesToRadians(degrees):
	return degrees * math.pi / 180;

def main():

	# Latitude, Longitude for Point A
	latitudeA = float(raw_input("Enter Latitude of Point A: "))
	longitudeA = float(raw_input("Enter Longitude of Point A: "))

	# Latitude, Longitude for Point B
	latitudeB = float(raw_input("Enter Latitude of Point B: "))
	longitudeB = float(raw_input("Enter Longitude of Point B: "))
	
	# Latitude, Longitude for Point C
	latitudeC = float(raw_input("Enter Latitude of Point C: "))
	longitudeC = float(raw_input("Enter Longitude of Point C: "))

	# Latitude, Longitude for Point D
	latitudeD = float(raw_input("Enter Latitude of Point D: "))
	longitudeD = float(raw_input("Enter Longitude of Point D: "))

	# Calculate the distance between points
	distAB = distanceBetweenPoints(latitudeA, longitudeA, latitudeB, longitudeB)
	distAC = distanceBetweenPoints(latitudeA, longitudeA, latitudeC, longitudeC)
	distCD = distanceBetweenPoints(latitudeC, longitudeC, latitudeD, longitudeD)
	distBD = distanceBetweenPoints(latitudeB, longitudeB, latitudeD, longitudeD)

	# Compute the two possible detour paths, ACDB and CABD
	# First detour ACDB - AB
	first = (distAC + distCD + distBD) - distAB
	
	# Second detour CABD - CD
	second = (distAC + distAB + distBD) - distCD
	
	if first < second: 
		print "Detour Distance: " + str(first) + " miles"
		print "Path: A -> C -> D -> B" 	
	elif first == second:
		print "Detour Distance: " + str(first)  + " miles"
		print "Either of the Paths: A -> C -> D -> B or C -> A -> B -> D" 	
	else: 
		print "Detour Distance: " + str(second) + " miles"
		print "Path: C -> A -> B -> D" 	
		
main()
