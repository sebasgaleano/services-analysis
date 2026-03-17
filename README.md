# Geospatial Urban Services Analysis — Asunción

## Overview
This project analyzes the spatial distribution and coverage of urban services in Asunción, Paraguay using OpenStreetMap data.

It combines geospatial data processing, spatial analysis, and interactive visualization to identify areas with high service density and zones lacking adequate coverage.

## Objectives
- Collect and process urban service data from OpenStreetMap
- Explore spatial distribution of services (hospitals, pharmacies, schools, etc.)
- Analyze service coverage using buffer-based methods
- Identify underserved areas in the city
- Provide an interactive visualization using Streamlit

## Tech Stack
- Python
- GeoPandas
- OSMnx
- Folium
- Streamlit
- Scikit-learn

## Project Structure
```
geospatial-urban-services/
│
├── data/  # Processed geospatial data (GeoJSON)
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_visualization.ipynb
│   └── 03_analysis.ipynb
│
├── src/
│   ├── analysis.py
│   ├── data_loader.py
│   └── map_generator.py
│
├── main.py             # streamlit app
│
├── requirements.txt
└── README.md
```

## Data Source
Data is obtained from OpenStreetMap using OSMnx.

## Methodology

### 1. Data Collection
- Extract amenities data using OSMnx
- Filter point geometries
- Store as GeoJSON for reproducibility

### 2. Spatial Exploration
- Analyze distribution of services
- Count amenities by type
- Visualize spatial patterns

### 3. Service Coverage Analysis
- Generate buffers around service locations (e.g., 500 meters)
- Merge buffers to estimate coverage area
- Compute uncovered areas within the city boundary

### 4. Clustering 
- Apply DBSCAN to identify clusters of services

## Key Features
- Interactive map with multiple service layers
- Heatmap visualization
- Multi-service overlay

## Running the Project

### Install dependencies
```
pip install -r requirements.txt
```

### Run Streamlit app
```
streamlit run main.py
```

## Example Use Cases
- Urban planning and infrastructure analysis
- Accessibility studies for public services
- Supporting data-driven policy decisions

## Future Improvements
- Network-based service coverage (travel time instead of radius)
- Integration with demographic data
- Advanced spatial statistics
- Deployment as a public dashboard

## License
MIT License