import gpxpy
import gpxpy.gpx
import srtm
from srtm import Srtm3HeightMapCollection
srtm3_data = Srtm3HeightMapCollection()

# groningen_elevation = srtm3_data.get_altitude(40.123, -7.456)
# print('Elevation of Groningen:', groningen_elevation)

gpx_file = open('test_file.gpx', 'w')

gpx = gpxpy.gpx.GPX()

# Creating a new file:
# --------------------

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)



# Create points:
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(53.308333, 6.369444, elevation=1))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(53.219444, 6.566667, elevation=1))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(53.170833, 6.613889, elevation=1))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(53.206944, 6.304167, elevation=1))

# You can add routes and waypoints, too...

print('Created GPX:', gpx.to_xml())
gpx_file.write(gpx.to_xml())
gpx_file.close()