from geopy.distance import vincenty
import math
"""
Using geopy-1.11.0 library for computing lat-long distances
"""


def compute_distance(lat_long1, lat_long2):
    return vincenty(lat_long1, lat_long2).kilometers


def read_csv_file(file_name):
    navigation_points = []
    with open(file_name) as f:
        for line in f:
            line = line.split(',')
            if line[0] and line[1]:
                navigation_points.append((float(line[0]), float(line[1])))

    return navigation_points

def get_direction(first, second, third):
    try:
        #slope1 = (second[1]-first[1])/(second[0]-first[0])
        #slope2 = (third[1]-second[1])/(third[0]-second[0])
        #angle = math.degrees(math.atan(slope2) - math.atan(slope1))

        vector1 = (second[0]-first[0], second[1]-first[1])
        vector2 = (third[0]-second[0], third[1]-second[1])
        angle = math.degrees(vector1[0]*vector2[1] - vector1[1]*vector2[0])
        if vector1 == (0,0) or vector2 == (0,0):
            return ""
        if angle > 0:
            direction = "Left"
        elif angle < 0:
            direction = "Right"
        else:
            direction = "Take U turn"
        angle = abs(angle)
        if angle < 30:
            direction += "Slight "
        elif angle > 140:
            direction = "Take U turn towards" + direction
        return direction
    except:
        return "No turn"
    """
    a = math.sqrt((second[0]-first[0])**2 + (second[1]-first[1])**2)
    b = math.sqrt((second[0]-third[0])**2 + (second[1]-third[1])**2)
    c = math.sqrt((third[0]-first[0])**2 + (third[1]-first[1])**2)
    angle = math.acos((a**2 + b**2 - c**2) / (2*a*b) )
    return angle"""


def get_navigation_instructions(navigation_points, speed, timestamp):
    if navigation_points:
        if len(navigation_points) == 1:
            print timestamp, ": Reached Destination"
            return
        distance_meters = compute_distance(navigation_points[0], navigation_points[1])*1000
        print timestamp, "minutes: Go straight for %d meters.\n" % distance_meters
        time_minutes = distance_meters*60/(speed*1000)
        timestamp += time_minutes
        if len(navigation_points) > 2 and distance_meters:
            #print "Angle",
            print str(timestamp)+" minutes", get_direction(navigation_points[0], navigation_points[1], navigation_points[2])

        get_navigation_instructions(navigation_points[1:], speed, timestamp)
    else:
        print "No navigation points specified!"

if __name__ == "__main__":
    file_name = "lat_long.csv"
    speed = input("Enter the speed: ")
    navigation_points = read_csv_file(file_name)
    get_navigation_instructions(navigation_points, speed, 0)