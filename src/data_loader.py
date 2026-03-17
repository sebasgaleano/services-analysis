import osmnx as ox
import geopandas as gpd
import streamlit as st

@st.cache_data
def load_osm_data(city_name, tags):
    """
    Carga datos de OpenStreetMap para una ciudad específica.
    
    Args:
        city_name (str): Nombre de la ciudad.
        tags (dict): Diccionario de tags de OSM a filtrar.
    
    Returns:
        GeoDataFrame: Datos geoespaciales filtrados.
    """
    try:
        gdf = ox.features_from_place(city_name, tags)
    except AttributeError:
        gdf = ox.features.features_from_place(city_name, tags)
    
    return gdf

