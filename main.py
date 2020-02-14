import geopandas as gpd

import pandas as pd

file = r'C:\Users\jhardco\Documents\workDocs\ScratchWorkSHPS\geojsons\pocngcnts.geojson'

cnts = gpd.read_file(file)
print(cnts)


y=0
t=1
print(y+t)