import os
os.chdir("F:/01Algorithms/webmap")
import geopandas as gpd
import mplleaflet
from Hapi.gis.vector import Vector as V
import numpy as np
# read the data
data = gpd.read_file("data/RaCa_general_location.csv")
print(data.shape)
data2 = gpd.read_file("data/RaCA_SOC_pedons.csv")
print(data2.shape)
# unify column name for merging
data = data.rename(columns={"RaCA_Id":"rcasiteid"})
#%% check duplicate
print(data.shape)
data.drop_duplicates(["rcasiteid"], inplace=True)
print(data.shape)

print(data2.shape)
data2.drop_duplicates(["rcasiteid"], inplace=True)
print(data2.shape)
#%% merge
new_data = data2.merge(data, on='rcasiteid', how='left', sort=False)
print(new_data.shape)
new_data.drop_duplicates(["rcasiteid"], inplace=True)
print(new_data.shape)
#%% create a shapely geometry object for the geopanda table
# create the lat and long as a list of tuples
lats = new_data.loc[:,'Gen_lat'].tolist()
lons = new_data.loc[:,'Gen_long'].tolist()

lats = [float(i) for i in lats]
lons = [float(i) for i in lons]

coords = [(i,j) for i in lons for j in lats]
#%%
x = V.CreatePoint(coords)
#%%