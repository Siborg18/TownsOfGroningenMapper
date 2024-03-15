import requests
import json

HTTP_SERVER = 'http://router.project-osrm.org'


def route_request():
    # request_string ='http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false'
    # request_string = f"{HTTP_SERVER}" + "/nearest/v1/bike/6.369444,53.308333?"
    request_string = f'{HTTP_SERVER}' + '/route/v1/bike/6.369861,53.308685;7.09161,53.174945?overview=false&annotations=true&steps=true'
    r = requests.get(request_string)
    print(r.text)
    my_json = json.loads(r.text)
    print(my_json)

    # /route/v1/{profile}/{coordinates}?alternatives={true|false|number}&steps={true|false}&geometries={polyline|polyline6|geojson}&overview={full|simplified|false}&annotations={true|false}

    route_request()
