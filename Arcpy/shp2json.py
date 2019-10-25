import json
import ogr

driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r''
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
    }

lyr = data_source.GetLayer(0)
for feature in lyr:
    fc['features'].append(feature.ExportToJson(as_object=True))

with open('counties.json', 'wb') as f:
json.dump(fc, f)