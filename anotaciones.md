urban_services/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Exploración de datos OSM, limpieza, filtrado
│   ├── 02_visualization.ipynb         # Mapas interactivos con Folium/HeatMap
│   ├── 03_analysis.ipynb              # Análisis de densidad, superposición, clustering
│
├── src/
│   ├── data_loader.py                 # Funciones para descargar OSM y cachear
│   ├── map_generator.py               # Funciones para generar mapas y HeatMaps
│   ├── analysis.py                    # Funciones de análisis espacial
│
├── app.py                             # Streamlit interactivo
├── requirements.txt                   # Dependencias
├── README.md
└── .gitignore