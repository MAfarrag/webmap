# socstock 

Install
-------
- to install the dependencies using pip

```
pip install -r requirements.txt
```
- to install the dependencies using conda
```
conda install --yes --file requirement.txt
```
- to install directly from the github repository
```
pip install git+https://github.com/MAfarrag/webmap.git
```

Run
---
- to run the application navigate the root directory of the repository
```
python server.py
``` 
- in case you have different python version installed in your local machine you have to provide the absolute path to the python interpreter
```
path/to/python server.py
```
View Map
--------
- to view the generated map
- open your google chrome and type 
```
locahost:80
```
- The Map Contains 6 layers 3 point maps (SOCstock 100, 30, 5) and 3 heat maps (SOCstock-Heat Map 100, 30, 5) which can be check on/off using the later control at the top right corner 
- the SOCstock 100 point map has a popup when you hover over any point showing the site id , the value of the SOCstock 100, 30, and 5
- the background tile can be changed to one of the 6 tile (cartodbpositron, cartodbdark_matter, Stamen Terrain, Stamen Toner, Stamen Water Color) through the layer control at the top right corner  
- the map has a popup for the location when you press left click on any part of the map showing the latitude and longitude of the location
- the map has a zoom on click shich zoom the the location with the left mouse click

<iframe src="src/RCS.html" width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>



Docker image
--------
- to download the docker image and install directly using docker
```
docker run mafarrag/socstock:v.1
```
- to view the generated map
```
locahost:4000
```