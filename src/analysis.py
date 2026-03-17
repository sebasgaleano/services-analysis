import geopandas as gpd
from sklearn.cluster import DBSCAN
import numpy as np

def compute_clusters(gdf, eps=0.01, min_samples=3):
    """
    Aplica clustering DBSCAN para encontrar agrupaciones de servicios.
    
    Args:
        gdf (GeoDataFrame): GeoDataFrame con puntos de servicios.
        eps (float): Distancia máxima para considerar vecinos.
        min_samples (int): Mínimo de puntos por cluster.
    
    Returns:
        GeoDataFrame: GDF con columna 'cluster' indicando el cluster asignado.
    """
    coords = np.array(list(zip(gdf.geometry.y, gdf.geometry.x)))
    db = DBSCAN(eps=eps, min_samples=min_samples, metric='haversine').fit(np.radians(coords))
    gdf = gdf.copy()
    gdf['cluster'] = db.labels_
    return gdf