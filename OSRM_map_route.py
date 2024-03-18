import requests
import json

HTTP_SERVER = 'http://router.project-osrm.org'
test_coord_a = "53.219444, 6.566667"
test_coord_b = "53.234860359373265, 6.548037763963784"


def coords_lon_lat_no_spaces(coords):
    coords_as_list = [x.strip() for x in coords.split(',')]
    coords_as_list.reverse()
    coords_as_string = ','.join(coords_as_list)
    print(coords_as_string)
    return coords_as_string


def route_request(route_coords):
    # request_string ='http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false'
    # request_string = f"{HTTP_SERVER}/nearest/v1/bike/{route_coords}?"
    request_string = f'{HTTP_SERVER}/route/v1/bike/{route_coords}?overview=false&annotations=true&steps=true'
    r = requests.get(request_string)
    print(r.text)
    my_json = json.loads(r.text)
    print(json.dumps(my_json, indent=2))

    # /route/v1/{profile}/{coordinates}?alternatives={true|false|number}&steps={true|false}&geometries={polyline|polyline6|geojson}&overview={full|simplified|false}&annotations={true|false}


my_coords = f"{coords_lon_lat_no_spaces(test_coord_a)};{coords_lon_lat_no_spaces(test_coord_b)}"
route_request(my_coords)
