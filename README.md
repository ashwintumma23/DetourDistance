# Detour Distance
[![Code Climate](https://codeclimate.com/repos/56096f1669568012ce0004dc/badges/1110086f7d7debdb2c12/gpa.svg)](https://codeclimate.com/repos/56096f1669568012ce0004dc/feed)

This repository contains the solution for the calculate Detour distance problem.

### Example

The example which I have taken is of New York City. As shown in the map below: 
* Point A - Empire State Building
* Point B - Central Park North
* Point C - Times Square
* Point D - Rockeffeler Center

![New York City map](https://github.com/ashwintumma23/DetourDistance/blob/master/images/NewYorkCity.png "New York City Map")


In this case, Driver 1 is travelling from Point A to Point B, and Driver 2 is travelling from Point C to Point D. As seen, driver 1 can pick up and drop off the second driver, since the detour distance for him is less.

```
Point A: Empire State Building, 34th Street
40.74877690495834, -73.98543119430542

Point B: Central Park, 111th Street
40.798314488417, -73.95227909088135

Point C: Times Square, 42nd Street
40.75896043391528, -73.98468017578125

Point D: Rockeffeler Center, 49th Street
40.758245280893014, -73.97802829743432

ashwin@ashwin-Studio-1537:~/DetourDistance$ python calculateDetourDistance.py 

Enter Latitude of Point A: 40.74877690495834 
Enter Longitude of Point A: -73.98543119430542
Enter Latitude of Point B: 40.798314488417 
Enter Longitude of Point B: -73.95227909088135
Enter Latitude of Point C: 40.75896043391528 
Enter Longitude of Point C: -73.98468017578125
Enter Latitude of Point D: 40.758245280893014 
Enter Longitude of Point D: -73.97802829743432

Detour Distance: 0.298216148068 miles
Path: A -> C -> D -> B

```

### 

