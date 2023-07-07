import dash_leaflet as dl
from dash import Dash, html, Output, Input
from dash.exceptions import PreventUpdate
from dash_extensions.javascript import assign

# How to render geojson.
point_to_layer = assign("""function(feature, latlng, context){
    const p = feature.properties;
    if(p.type === 'circlemarker'){return L.circleMarker(latlng, radius=p._radius)}
    if(p.type === 'circle'){return L.circle(latlng, radius=p._mRadius)}
    return L.marker(latlng);
}""")
l ={'type': 'FeatureCollection',
 'features': [{'id': '0',
   'type': 'Feature',
   'properties': {'d_meters_pt': 117.33166029,
    'gh': 'dry02v0buwfvmtzqyc47',
    'gh_ss': 'dry02',
    'id_ss': 4596165041,
    'loccd': 'ME0009',
    'osm_d_meters': 4495.99991571,
    'pt': '0101000020E6100000360186E5CF9151C0A912656F29D54540',
    'start_geom': '0101000020E6100000ED4218E4D39151C0D3D8035207D54540',
    'start_id': 26726777,
    'state': 'ME',
    'svclocid': 47328985,
    'the_geom_ss': '0101000020E6100000BCEBC781329551C03B922639BBD64540'},
   'geometry': {'type': 'Polygon',
    'coordinates': [[[-70.33145266517053, 43.67661906812057],
      [-70.33163710452003, 43.67668548773778],
      [-70.33180504209464, 43.676786613452755],
      [-70.33195002414755, 43.67691855906098],
      [-70.33206647909975, 43.677076253966725],
      [-70.33214993165278, 43.677253638043204],
      [-70.33219717477178, 43.67744389451983],
      [-70.33220639293022, 43.67763971194692],
      [-70.33217723187941, 43.67783356517054],
      [-70.33211081226221, 43.67801800452004],
      [-70.33200968654724, 43.67818594209464],
      [-70.33187774093902, 43.67833092414755],
      [-70.33172004603327, 43.678447379099765],
      [-70.33154266195679, 43.67853083165278],
      [-70.33135240548016, 43.67857807477179],
      [-70.33115658805308, 43.678587292930224],
      [-70.33096273482946, 43.67855813187943],
      [-70.27831283482946, 43.66525543187943],
      [-70.27812839547997, 43.665189012262225],
      [-70.27796045790535, 43.66508788654725],
      [-70.27781547585245, 43.66495594093902],
      [-70.27769902090024, 43.66479824603328],
      [-70.27761556834722, 43.6646208619568],
      [-70.27756832522822, 43.66443060548017],
      [-70.27755910706978, 43.664234788053086],
      [-70.27758826812058, 43.664040934829465],
      [-70.27765468773778, 43.66385649547996],
      [-70.27775581345276, 43.66368855790536],
      [-70.27788775906097, 43.66354357585245],
      [-70.27804545396673, 43.66342712090024],
      [-70.2782228380432, 43.663343668347224],
      [-70.27841309451983, 43.66329642522821],
      [-70.27860891194692, 43.66328720706978],
      [-70.27880276517054, 43.663316368120576],
      [-70.33145266517053, 43.67661906812057]]]}},
  {'id': '1',
   'type': 'Feature',
   'properties': {'d_meters_pt': 38.11383062,
    'gh': 'dry02ubsvsrty8gb4z7q',
    'gh_ss': 'dry02',
    'id_ss': 4596165041,
    'loccd': 'ME0009',
    'osm_d_meters': 4495.99991571,
    'pt': '0101000020E6100000DB19A6B6D49151C0F1845E7F12D54540',
    'start_geom': '0101000020E6100000ED4218E4D39151C0D3D8035207D54540',
    'start_id': 26726777,
    'state': 'ME',
    'svclocid': 47319914,
    'the_geom_ss': '0101000020E6100000BCEBC781329551C03B922639BBD64540'},
   'geometry': {'type': 'Polygon',
    'coordinates': [[[-70.33145266517053, 43.67661906812057],
      [-70.33163710452003, 43.67668548773778],
      [-70.33180504209464, 43.676786613452755],
      [-70.33195002414755, 43.67691855906098],
      [-70.33206647909975, 43.677076253966725],
      [-70.33214993165278, 43.677253638043204],
      [-70.33219717477178, 43.67744389451983],
      [-70.33220639293022, 43.67763971194692],
      [-70.33217723187941, 43.67783356517054],
      [-70.33211081226221, 43.67801800452004],
      [-70.33200968654724, 43.67818594209464],
      [-70.33187774093902, 43.67833092414755],
      [-70.33172004603327, 43.678447379099765],
      [-70.33154266195679, 43.67853083165278],
      [-70.33135240548016, 43.67857807477179],
      [-70.33115658805308, 43.678587292930224],
      [-70.33096273482946, 43.67855813187943],
      [-70.27831283482946, 43.66525543187943],
      [-70.27812839547997, 43.665189012262225],
      [-70.27796045790535, 43.66508788654725],
      [-70.27781547585245, 43.66495594093902],
      [-70.27769902090024, 43.66479824603328],
      [-70.27761556834722, 43.6646208619568],
      [-70.27756832522822, 43.66443060548017],
      [-70.27755910706978, 43.664234788053086],
      [-70.27758826812058, 43.664040934829465],
      [-70.27765468773778, 43.66385649547996],
      [-70.27775581345276, 43.66368855790536],
      [-70.27788775906097, 43.66354357585245],
      [-70.27804545396673, 43.66342712090024],
      [-70.2782228380432, 43.663343668347224],
      [-70.27841309451983, 43.66329642522821],
      [-70.27860891194692, 43.66328720706978],
      [-70.27880276517054, 43.663316368120576],
      [-70.33145266517053, 43.67661906812057]]]}}]}

# Create example app.
app = Dash()

app.layout = html.Div([
    # Setup a map with the edit control.
    dl.Map(center=[56, 10], zoom=4, children=[
        dl.TileLayer(), dl.FeatureGroup([
            dl.EditControl(id="edit_control"),  dl.GeoJSON(data = l, id="geojn", )]),
    ], style={'width': '50%', 'height': '50vh', 'margin': "auto", "display": "inline-block"}, id="map"),
    # Setup another map to that mirrors the edit control geometries using the GeoJSON component.
    dl.Map(center=[56, 10], zoom=4, children=[
        dl.TileLayer(), dl.GeoJSON(id="geojson", options=dict(pointToLayer=point_to_layer), zoomToBounds=True),
    ], style={'width': '50%', 'height': '50vh', 'margin': "auto", "display": "inline-block"}, id="mirror"),
])

# Copy data from the edit control to the geojson component.
@app.callback(Output("geojson", "data"), Input("edit_control", "geojson"))
def mirror(x):
    if not x:
        raise PreventUpdate
    return x

if __name__ == '__main__':
    app.run_server()