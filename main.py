import geopandas as gpd
import streamlit as st
from src.data_loader import load_osm_data
from src.map_generator import generate_map
from streamlit_folium import st_folium

st.title("Urban Services in Asunción")

city = "Asuncion, Paraguay"
tags = {"amenity": True}
service_options = ["hospital", "restaurant", "pharmacy", "school"]


try:
    # cargar datos desde el archivo geojson preparado
    gdf = gpd.read_file("data/asuncion_amenities.geojson")
    
except:
    # Si no existe el archivo, cargar desde OSM y guardar para futuras ejecuciones
    gdf = load_osm_data(city, tags)
    gdf.to_file("data/asuncion_amenities.geojson", driver="GeoJSON")

# Selección de uno o dos servicios
services_selected = st.multiselect(
    "Select service(s) to display",
    service_options,
    default=["hospital"]
)



# Filtrar datos
filtered_gdfs = {service: gdf[gdf["amenity"] == service] for service in services_selected}





# Generar mapa dinámico
if filtered_gdfs:
    m = generate_map(filtered_gdfs)
    st_folium(m, width=700, height=500)