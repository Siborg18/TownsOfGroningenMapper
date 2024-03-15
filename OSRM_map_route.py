import requests
import json

HTTP_SERVER = 'http://router.project-osrm.org'
test_coords = "6.566667,53.219444"

def route_request():
    # request_string ='http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false'
    request_string = f"{HTTP_SERVER}/nearest/v1/bike/{test_coords}?"
    #request_string = f'{HTTP_SERVER}/route/v1/bike/{test_coords};7.09161,53.174945?overview=false&annotations=true&steps=true'
    r = requests.get(request_string)
    print(r.text)
    my_json = json.loads(r.text)
    print(json.dumps(my_json, indent=2))

    # /route/v1/{profile}/{coordinates}?alternatives={true|false|number}&steps={true|false}&geometries={polyline|polyline6|geojson}&overview={full|simplified|false}&annotations={true|false}

route_request()
