import bpy
import random
import math

#### Finding Random Location

def random_coord_point():

    randlat = random.uniform(-90,90)
    randlng = random.uniform(-180,180)
    
    return(randlat,randlng)

randCoord = random_coord_point()

print(randCoord)


#### Finding Random Location Near another Location

#latlng to find around
initlat = 37.861912
initlong = -84.661720
#distance in meters
distance = 250

def random_around_point(lat, lng, dist):
    #distance is in meters
    #111300 # of meters in a degree at equator
    r = dist / 111300
    u = random.uniform(0,1)
    v = random.uniform(0,1)
    w = r * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    x1 = x / math.cos(lng)
    y = w * math.sin(t)
    
    lat = lat+x1
    lng = lng+y
    
    return(lat,lng)

randnear = random_around_point(initlat,initlong,distance)

print(randnear)