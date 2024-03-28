import requests
import json
from main import coord_as_float

HTTP_SERVER = 'http://router.project-osrm.org'
test_coord_a = "53.219444, 6.566667"
test_coord_b = "6.548037763963784, 53.234860359373265"


def pretty_coords(coords):
    coords_as_string = [x.strip() for x in coords.split(',')]
    coords_as_floats = []
    for i in range(len(coords_as_string)):
        coords_as_floats.append(coord_as_float(coords_as_string[i]))
    if coords_as_floats[0] < coords_as_floats[1]:
        coords_as_string = ','.join(coords_as_string)
        print(coords_as_string)
        return coords_as_string
    else:
        coords_as_string.reverse()
        coords_as_string = ','.join(coords_as_string)
        print(coords_as_string)
        return coords_as_string


def route_request(route_coords):
    # request_string ='http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false'
    # request_string = f"{HTTP_SERVER}/nearest/v1/bike/{route_coords}?"
    request_string = f'{HTTP_SERVER}/route/v1/bike/{route_coords}?overview=false&annotations=true&steps=true'
    r = requests.get(request_string)
    #print(r.text)
    output_route_json = json.loads(r.text)
    return output_route_json

def pick_locations_from_json(route_json):
    coord_list = []
    new_list = []
    coords_as_string = ""
    print(json.dumps(route_json, indent=2))
    for i in range(len(route_json["routes"][0]["legs"][0]["steps"])):
        coord_list.append(route_json["routes"][0]["legs"][0]["steps"][i]["maneuver"]["location"])

    print(coord_list)

my_test_coord_a = pretty_coords(test_coord_a)
my_test_coord_b = pretty_coords(test_coord_b)
my_coords = f"{my_test_coord_a};{my_test_coord_b}"
print(my_coords)
# my_route = route_request(my_coords)
# my_location = pick_locations_from_json(my_route)
# print(my_location)