# Hauptlogik oder Skript zum Ausführen der App

import geopandas as gpd

url = "https://geodienste.bfn.de/ogc/ffh?service=WFS&version=1.1.0&request=GetFeature&typeName=bfn:ffh_gebiet&outputFormat=application/json"
ffh = gpd.read_file(url)

#Beispielkoordinaten
punkt = gpd.read_file(url)


#SChnittmenge
ergebnis = gpd.sjoin(ffh, punkt, how="inner", predicate='intersects')
print(ergebnis[['sitecode', 'sitename']])