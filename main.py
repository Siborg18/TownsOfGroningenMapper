import math

import matplotlib.pyplot as plt
import os
from matplotlib import transforms
import numpy as np
from geopy import distance

fig, ax = plt.subplots()


def open_file_and_copy_lines():
    text_input = open("Groningen Towns.txt")
    places_dict = {}
    for line in text_input:
        try:
            line = [x.strip() for x in line.split('\t')]
            places_dict[line[0]] = coords_as_ints(line[1])
        except IndexError:
            places_dict[line[0]] = line[1]
    text_input.close()
    return places_dict


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


def find_towns_within_distance(origin_coords, towns_dict, distance_limit):
    towns_in_range = []
    for town in towns_dict:
        current_distance = distance.distance(origin_coords, towns_dict[town])
        if current_distance == 0:
            origin_name = town
            print("Do nothing")
        elif current_distance < distance_limit:
            towns_in_range.append((town, current_distance))
    print(f"Towns within {distance_limit}km of {origin_name}: {len(towns_in_range)}")
    print(towns_in_range)


def find_the_nearest(origin_coords, towns_dict):
    distance_nearest_town = 1000
    for town in towns_dict:
        current_distance = distance.distance(origin_coords, towns_dict[town])
        if current_distance == 0:
            origin_name = town
        elif current_distance < distance_nearest_town:
            distance_nearest_town = current_distance
            name_of_town = town
    print(f"The closest town to {origin_name} is {name_of_town}. The distance between is {distance_nearest_town})")
    return name_of_town


def find_key(towns_dict, target):
    return next((key for key, value in towns_dict.items() if value == target), None)


def find_neighbours(origin_coords, number_of_neighbours, towns_dict):
    neighbours = {}
    for town in towns_dict:
        current_distance = distance.distance(origin_coords, towns_dict[town])
        if current_distance == 0:
            origin_name = town
        else:
            neighbours[town] = current_distance
    values = neighbours.values()
    values = sorted(values)
    values = values[0:number_of_neighbours]
    i = 1
    output_neighbours = []
    for value in values:
        print(f"{i}: {find_key(neighbours, value)}")
        output_neighbours.append(towns_dict[find_key(neighbours, value)])
        i += 1
    return output_neighbours


def find_the_furthest(origin_coords, towns_dict):
    distance_furthest_town = 0
    for town in towns_dict:
        current_distance = distance.distance(origin_coords, towns_dict[town])
        if current_distance == 0:
            origin_name = town
            print("Do nothing")
        elif current_distance > distance_furthest_town:
            distance_furthest_town = current_distance
            name_of_town = town
    print(f"The furthest town to {origin_name} is {name_of_town}. The distance between is {distance_furthest_town})")
    return name_of_town


def graph_completed_green(town_completed):
    x, y = town_completed[1], town_completed[0]
    ax.scatter(x, y, color="green")

def graph_target_red(town):
    x, y = town[1], town[0]
    ax.scatter(x, y, color="red")

def graph_towns(*town_to_graph, towns_dict):
    groningen = towns_dict["Groningen"]
    for my_town in town_to_graph:
        x, y = my_town[1], my_town[0]  # x y are opposite when graphing to compensate for distance calc using y x
        if my_town == groningen:
            ax.scatter(x, y, color="orange")
        else:
            ax.scatter(x, y, color="black")
        # print(my_town)


def Dijkstra_algorithm(origin_town, target_town):
    # Find distance between two towns without any deviation
    # Find neighbours of origin town
    # Find if distance from neighbour is greater than origin

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    towns_dict = open_file_and_copy_lines()
    print(distance.distance(towns_dict["Stadskanaal"], towns_dict["Lauwersoog"]))

    for town in towns_dict:
        graph_towns(towns_dict[town], towns_dict=towns_dict)

    test_town = towns_dict["Schildwolde"]
    find_the_nearest(test_town, towns_dict)
    find_the_furthest(test_town, towns_dict)
    # test_town_2 = coords_as_ints(towns["Groningen"])
    find_towns_within_distance(test_town, towns_dict, 5)
    # graph_completed_green(test_town)
    #
    my_neighbours = find_neighbours(test_town, 10, towns_dict)
    graph_target_red(test_town)
    for neighbour in my_neighbours:
        graph_completed_green(neighbour)
    #
    # lauwersoog = coords_as_ints(towns["Lauwersoog"])
    # Delfzijl = coords_as_ints(towns["Delfzijl"])
    # ter_apel = coords_as_ints(towns["Ter Apel"])
    # graph_towns(groningen, ter_apel, zoutkamp)
    # find_the_nearest(origin_coords=groningen, town_dict=towns)
    # find_the_furthest(origin_coords=groningen, town_dict=towns)
    # x = lauwersoog[0]
    # y = lauwersoog[1]
    # my_color = "green"
    # fig, ax = plt.subplots()
    # my_distance = distance.distance(lauwersoog, Delfzijl)
    # print(f"Distance from Groningen to Ter Apel: {my_distance}")
    # my_distance = distance.distance(lauwersoog, ter_apel)
    # print(f"Distance from Groningen to Zoutkamp: {my_distance}")
    # my_distance = distance.distance(ter_apel, Delfzijl)
    # print(f"Distance from Zoutkamp to Ter Apel: {my_distance}")
    # ax.scatter(x, y, color=my_color)
    # print(f"Groningen: {x}, {y}")
    # x = Delfzijl[0]
    # y = Delfzijl[1]
    # my_color = "red"
    # ax.scatter(x, y, color=my_color)
    # print(f"Ter Apel: {x}, {y}")
    # x = ter_apel[0]
    # y = ter_apel[1]
    # my_color = "orange"
    # ax.scatter(x, y, color=my_color)
    # print(f"Zoutkamp: {x}, {y}")

    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Use matplotlib, points can just be dots, circles whatever, then lines can be vectors.

# Plot graph relative to x, y. Groningen can be origin. Then make vectors between each one.
