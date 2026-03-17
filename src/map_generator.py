import folium
from folium.plugins import HeatMap

def generate_map(filtered_gdfs, center=[-25.3, -57.6], zoom_start=12):
    """
    Genera un mapa de Folium con uno o varios servicios.
    
    Args:
        filtered_gdfs (dict): Diccionario con {nombre_servicio: GeoDataFrame filtrado}.
        center (list): Coordenadas del centro del mapa.
        zoom_start (int): Nivel de zoom inicial.
    
    Returns:
        folium.Map: Mapa interactivo con marcadores y HeatMaps.
    """
    m = folium.Map(location=center, zoom_start=zoom_start)
    colors = {"hospital":"red", "restaurant":"green", "pharmacy":"purple", "school":"blue"}

    for service, gdf in filtered_gdfs.items():
        heat_data = []
        for _, row in gdf.iterrows():
            if row.geometry.geom_type == "Point":
                folium.CircleMarker(
                    location=[row.geometry.y, row.geometry.x],
                    radius=4,
                    color=colors.get(service, "blue"),
                    fill=True,
                    fill_opacity=0.7,
                    popup=row.get("name", service.title())
                ).add_to(m)
                heat_data.append([row.geometry.y, row.geometry.x])
        if heat_data:
            HeatMap(heat_data).add_to(m)
    return m