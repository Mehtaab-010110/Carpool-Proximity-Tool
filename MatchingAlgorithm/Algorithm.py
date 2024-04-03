import math

# Constants for the Earth's radius in kilometers
EARTH_RADIUS = 6371

def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    
    # Haversine formula to calculate the great-circle distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    distance_km = EARTH_RADIUS * c
    return distance_km

def group_by_proximity(coordinates):
    within_500m = set()
    within_1000m = set()
    
    # Loop over each coordinate pair and calculate distances
    for i, (lon1, lat1) in enumerate(coordinates):
        for j, (lon2, lat2) in enumerate(coordinates):
            if i != j:  # Avoid comparing the coordinate with itself
                distance = haversine(lon1, lat1, lon2, lat2) * 1000  # Convert to meters
                if distance <= 500:
                    # Add both points to the within_500m set
                    within_500m.add((lon1, lat1))
                    within_500m.add((lon2, lat2))
                elif distance <= 1000:
                    # Add both points to the within_1000m set
                    within_1000m.add((lon1, lat1))
                    within_1000m.add((lon2, lat2)) 
                    
    # Include all points within 500m in the within_1000m set as well
    within_1000m.update(within_500m)
    
    # Convert sets to lists to make them JSON serializable or easier to work with
    return list(within_500m), list(within_1000m)

# Example usage:
# coordinates = [(lon1, lat1), (lon2, lat2), ...]
# proximity_groups = group_by_proximity(coordinates)
# within_500m, within_1000m = proximity_groups
'''Haversine Function:

This function calculates the great-circle distance between two points on the earth's surface.
It converts longitude and latitude from degrees to radians.
The function then applies the Haversine formula to compute the distance in kilometers.
group_by_proximity Function:

The function takes a list of coordinates as input.
It uses two sets, within_500m and within_1000m, to store unique coordinate pairs that fall within the specified distances.
It iterates over each pair of coordinates using a nested loop and calculates the distance between them using the haversine function.
If the distance is less than or equal to 500 meters, both points are added to the within_500m set.
If the distance is more than 500 meters but less than or equal to 1000 meters, both points are added to the within_1000m set.
After all comparisons, the function includes all the points within 500 meters into the set of points within 1000 meters to meet the 
requirement that points within 500 meters are also considered to be within 1000 meters.
Finally, it returns two lists derived from the sets, which contain the coordinates grouped by their proximity.
Note: The use of sets (within_500m and within_1000m) ensures that each coordinate pair is unique and no duplicates are present.
The update method is used to add elements from within_500m into within_1000m.
The conversion to lists at the end is for ease of use if the result needs to be serialized to JSON or processed in a way that 
requires list data structures.'''