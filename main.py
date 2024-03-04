import math

import matplotlib.pyplot as plt
import numpy as np
from geopy import distance


def coords_as_ints(coords_string):
    lat_lon = [x.strip() for x in coords_string.split(',')]
    lat = lat_lon[0].lstrip('"')
    lon = lat_lon[1].rstrip('"')
    lat = float(lat)
    lon = float(lon)
    return lat, lon


def open_file_and_copy_lines():
    text_input = open("Groningen Towns.txt")
    places_dict = {}
    for line in text_input:
        line = [x.strip() for x in line.split('\t')]
        places_dict[line[0]] = line[1]
    return places_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    towns = open_file_and_copy_lines()
    for town in towns:
        coords = coords_as_ints(towns[town])
        print(coords)

    print(distance.distance(town_a, town_b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Use matplotlib, points can just be dots, circles whatever, then lines can be vectors.

# Plot graph relative to x, y. Groningen can be origin. Then make vectors between each one.
