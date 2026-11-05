# Geospatial Analysis and Representation for Data Science

**University of Trento — Academic Year 2026/2027**  
Teaching materials by Maurizio Napolitano

How do we turn spatial data into meaningful information?

This course explores how to find, inspect, integrate, analyse and represent geospatial data. Practical examples introduce spatial concepts through Python notebooks, maps and discussion.

The focus is on understanding the data: their origin, structure, coordinate reference system, quality and limitations. AI-assisted coding is used critically: generated code and results must be inspected, explained and checked.

## Lecture schedule

Maurizio Napolitano’s lectures take place on Fridays, with four hours per session.

The schedule describes the main themes. Some practical activities continue across sessions.

| Date | Topic | Slides |
|---|---|---|
| 16 October 2026 | Understanding and Inspecting Spatial Data | [Slides](https://docs.google.com/presentation/d/e/2PACX-1vT6BpGAjXPvI5jgWpVdxIuoSVUgEuXL5tOcJC5YqMqF7_nIr5AmzDCEU2UxjpjQESzv2XKuP4oBHRva/pub?start=false&loop=false&delayms=3000) |
| 23 October 2026 | Integrating Data through Spatial Relationships | |
| 30 October 2026 | Spatial Data Sources, OpenStreetMap and Network Analysis | [Slides](https://docs.google.com/presentation/d/e/2PACX-1vSOzuO4VBASctsQpIUxo6zH_w-GnEH8mYzKieVo7vsLFq8obJE8l9x3JTqnjj3iRzCYk5YGxxkR5yMp/pub?start=false&loop=false&delayms=3000) |
| 6 November 2026 | From Routes to Movement and Raster Analysis | |
| 13 November 2026 | From Analysis to Maps and Web Publishing | |

## Notebooks

The notebooks follow the practical activities. They are not in a one-to-one relationship with the lectures.

| Notebook | Main topics |
|---|---|
| [01 — Geospatial Vector Data](code/01_geospatial_vector_data_2026.ipynb) | Geometries, attributes, coordinate reference systems and inspecting spatial datasets. |
| [02 — Inspecting and Transforming Spatial Data](code/02_exercise_lecture_gis_introduction_2026.ipynb) | Practical exercises on reading data, transforming coordinates and converting formats. |
| [03 — Spatial Relationships and Operations](code/03_spatial_relationships_and_operations_2026_pharmacies.ipynb) | Spatial predicates, joins and overlays, using administrative boundaries and pharmacies. |
| [04 — Retrieving Spatial Data and Understanding Sources](code/04_retrieving_spatial_data_2026.ipynb) | Downloading data, accessing web services, geocoding and comparing official sources with OpenStreetMap. |
| [05 — Distance, Networks and Accessibility](code/05_distance_networks_accessibility_2026.ipynb) | Straight-line and network distances, walking networks, shortest paths and accessibility, starting from Sanbapolis and BUC. |
| [06 — Routing and Map Matching with GraphHopper](code/06_graphhopper_map_matching_2026.ipynb) | OpenStreetMap PBF extracts, routing and matching GPS observations to a network. |
| [07 — GPX and Movement Analysis with MovingPandas](code/07_gpx_movingpandas_incident_2026.ipynb) | Reconstructing a journey from recorded positions: timestamps, sampling intervals, speed, stops and changes in movement. |
| [08 — Raster Data: Terrain, Vegetation and Surface Temperature](code/08_raster_pixels_indicators_2026.ipynb) | Understanding raster grids, analysing visibility from Sardagna and deriving indicators from satellite observations. |

## Working with the notebooks

Open the notebooks in Jupyter or Google Colab and run the cells in order. Installation and data access instructions are provided within each notebook.

Before interpreting an output, check:

- Where do the data come from, and when were they collected?
- What does each feature, observation or pixel represent?
- Which coordinate reference system and measurement units are used?
- Are there missing values, duplicate records or suspicious coordinates?
- Which assumptions does the analysis introduce?
- What can the result support, and what remains uncertain?

For movement data, distinguish recorded observations from inferred events. For satellite comparisons, consider acquisition dates, cloud cover, spatial resolution and processing choices.

## Repository contents

- [`code/`](code/) — teaching notebooks.
- [`data/`](data/) — datasets and supporting files used in the exercises.
- [`data/raster_2024_2026/`](data/raster_2024_2026/) — raster data and metadata for the satellite examples.

The year in the repository name identifies the course edition. Individual datasets may refer to different observation periods.

## Data sources and documentation

Sources and dataset-specific links are provided in the notebooks.

Main resources include:

- [ISTAT](https://www.istat.it/) — administrative boundaries and statistical data.
- [Trentino Open Data](https://dati.trentino.it/) — local public datasets.
- [APSS pharmacy dataset](https://servizi.apss.tn.it/opendata/FARM001.csv) — pharmacies in Trentino.
- [OpenStreetMap](https://www.openstreetmap.org/) — collaboratively maintained geographic data.
- [Geofabrik downloads](https://download.geofabrik.de/) — regional OpenStreetMap extracts.
- [Mapterhorn](https://mapterhorn.com/) — tiled elevation data.
- [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) — access to Copernicus satellite data.
- [USGS Landsat](https://www.usgs.gov/landsat-missions) — Landsat imagery and documentation.

Software documentation:

- [GeoPandas](https://geopandas.org/)
- [OSMnx](https://osmnx.readthedocs.io/)
- [GraphHopper](https://github.com/graphhopper/graphhopper)
- [MovingPandas](https://movingpandas.org/)
- [Rasterio](https://rasterio.readthedocs.io/)
- [WhiteboxTools](https://www.whiteboxgeo.com/manual/wbt_book/intro.html)

## Attribution

Datasets retain their original licences and attribution requirements. Refer to the source documentation before reusing or redistributing them.

OpenStreetMap data © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright).
