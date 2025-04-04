import geopandas as gpd
import streamlit as st
import pydeck as pdk
import json

def zeige_karte(geojson_text: str):
    """Zeigt eine GeoJSON-Fläche auf einer interaktiven Karte an."""
    gdf = gpd.read_file(geojson_text)

    # In GeoJSON umwandeln
    geojson = json.loads(gdf.to_json())

    # Extrahiere Mittelpunkt
    lon, lat = gdf.geometry.centroid.x.mean(), gdf.geometry.centroid.y.mean()

    # Karte mit PyDeck anzeigen
    layer = pdk.Layer(
        "GeoJsonLayer",
        data=geojson,
        get_fill_color="[180, 0, 200, 100]",
        pickable=True,
    )

    view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=12, pitch=0)
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
