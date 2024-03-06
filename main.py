import math

import matplotlib.pyplot as plt
import numpy as np
from geopy import distance


def coords_as_ints(coords_string):
    try:
        lat_lon = [x.strip() for x in coords_string.split(',')]
        lat = lat_lon[0].lstrip('"')
        lon = lat_lon[1].rstrip('"')
        lat = float(lat)
        lon = float(lon)
        return lat, lon
    except ValueError:
        print(f"error: {coords_string}")
    return 0, 0


def open_file_and_copy_lines():
    text_input = open("Groningen Towns.txt")
    places_dict = {}
    for line in text_input:
        try:
            line = [x.strip() for x in line.split('\t')]
            print(line[0])
            places_dict[line[0]] = line[1]
        except IndexError:
            print(line[0])
            places_dict[line[0]] = line[1]
    print(len(places_dict))
    return places_dict

def find_the_nearest(town_1, town_dict):
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    towns = open_file_and_copy_lines()
    count = 0
    for town in towns:
        count += 1
        coords = coords_as_ints(towns[town])
        # print(f"{count}: {coords}")
    print(len(towns))
    town_a = coords_as_ints(towns["Groningen"])
    town_b = coords_as_ints(towns["Ter Apel"])
    print(distance.distance(town_a, town_b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Use matplotlib, points can just be dots, circles whatever, then lines can be vectors.

# Plot graph relative to x, y. Groningen can be origin. Then make vectors between each one.
