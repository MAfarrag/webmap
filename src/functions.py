import os, sys
import geopandas as gpd
from shapely.geometry import Point

def CreatePoint(coords):
    """CreatePoint

    CreatePoint takes a list of tuples of coordinates and convert it into
    a list of Shapely point object

    inputs
    ----------
        1-coords : [List]
            list of tuples [(x1,y1),(x2,y2)] or [(long1,lat1),(long2,lat1)]

    Outputs:
    ----------
        1-points : [List]
            list of Shaply point objects [Point,Point]

    Examples:
    ----------
        coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
        PointList = GIS.CreatePoint(coordinates)
        # to assign these objects to a geopandas dataframe
        # NopreviousGeoms is the number of geometries already exists in the
        # geopandas dataframe
        NopreviousGeoms = 5
        for i in range(NopreviousGeoms,NopreviousGeoms+len(PointList)):
            NewGeometry.loc[i,'geometry'] = PointList[i-NopreviousGeoms]
    """
    points = list()
    for i in range(len(coords)):
        points.append(Point(coords[i]))

    return points

def PrepareData():
    rootpath = os.path.abspath(os.getcwd())
    sys.path.append(rootpath + "/src")
    datapath = os.path.join(rootpath, "data")
    os.chdir(rootpath)

    #  read the data
    data = gpd.read_file("data/RaCa_general_location.csv")
    print(data.shape)
    data2 = gpd.read_file("data/RaCA_SOC_pedons.csv")
    print(data2.shape)
    # unify column name for merging
    data = data.rename(columns={"RaCA_Id": "rcasiteid"})
    #  check duplicate
    print(data.shape)
    data.drop_duplicates(["rcasiteid"], inplace=True)
    print(data.shape)

    print(data2.shape)
    data2.drop_duplicates(["rcasiteid"], inplace=True)
    print(data2.shape)
    #  merge
    new_data = data2.merge(data, on='rcasiteid', how='inner', sort=False)
    # convert to  geodataframe
    new_data = gpd.GeoDataFrame(new_data)
    print(new_data.shape)
    # new_data.drop_duplicates(["rcasiteid"], inplace=True)
    # print(new_data.shape)
    #  create a shapely geometry object for the geopanda table
    # create the lat and long as a list of tuples
    lats = new_data.loc[:, 'Gen_lat'].tolist()
    lons = new_data.loc[:, 'Gen_long'].tolist()

    lats = [float(i) for i in lats]
    lons = [float(i) for i in lons]

    # for i in range(len())
    coords = list(zip(lons, lats))
    # not necessary
    objects = CreatePoint(coords)
    new_data['geometry'] = objects
    del new_data['geometry_y'], new_data['geometry_x']

    return new_data
    # new_data.to_file("data/data.geojson", driver="GeoJSON")



