# Louisiana Parish Inspection Analysis

This is an end-to-end geospatial analytics pipeline built with **GeoPandas**: it loads authoritative Louisiana parish boundaries from the US Census, scatters synthetic inspection points across the state, spatial joins them to parishes, computes per area statistics, visualizes results statically and interactively, and extract useful insights.

This project was done to demonstratively understand the core GIS workflow which is used quite often in geospatial and environmental applied data science: **load boundary data, reproject, spatial join, aggregate, visualize**. 

## Why this project

Coastal Louisiana work constantly deals with the question: *for a set of field observations, which jurisdictional area does each fall in, and what do the totals look like per area?* That is exactly what this notebook tries to answers end to end with real parish polygons and a realistic spatial workflow.

## What it does

1. **Downloads real Louisiana parish polygons** from the US Census Bureau TIGER/Line 2023 county shapefile filtered to Louisiana
2. **Generates 500 synthetic inspection points** scattered across Louisiana using rejection sampling (random points inside the state bounding box, kept only if they fall inside a parish polygon)
3. **Tags each inspection** with a type (Pipeline, Wetland, Coastal, Utility, Transportation) and severity (1 to 3) using weighted random distributions
4. **Spatial joins** the inspections to parishes using the `within` predicate in geopandas
5. **Aggregates per parish**: count, average severity, high severity count
6. **Reprojects** to Louisiana State Plane South (EPSG:3452) so area can be computed in square miles
7. **Computes inspection density** per square mile
8. **Visualizes** with a side by side matplotlib choropleth and an interactive Folium map with clickable markers
9. **Extracts insights** about hot spot identification, type mix by parish, and urban vs rural coverage analysis

## Stack

- Python 3.13
- GeoPandas
- Shapely
- pyproj
- matplotlib
- Folium
- pandas, numpy

## Data sources

- **Parishes**: US Census Bureau TIGER/Line 2023 county shapefile.
- **Inspections**: synthetic for this demonstration, generated using rejection sampling inside the parish boundaries.

## Results

### Overview

| Metric | Value |
|---|---|
| Total inspections generated | 500 |
| Louisiana parishes total | 64 |
| Parishes with at least one inspection | 60 |
| Parishes with zero activity | 4 |
| Average inspections per parish | 7.8 |
| Unmatched inspections after spatial join | 0 |

### Inspection type breakdown

| Type | Count | Share |
|---|---:|---:|
| Pipeline | 148 | 30% |
| Wetland | 112 | 22% |
| Coastal | 108 | 22% |
| Utility | 89 | 18% |
| Transportation | 43 | 8% |

### Top parishes by inspection count

| Parish | Inspections | Avg severity | High severity |
|---|---:|---:|---:|
| Vernon | 21 | 1.62 | 4 |
| Plaquemines | 19 | 1.42 | 1 |
| Bossier | 18 | 1.56 | 1 |
| Terrebonne | 18 | 1.56 | 1 |
| Lafourche | 17 | 1.41 | 2 |
| St. Bernard | 16 | 1.44 | 2 |
| Caddo | 15 | 1.47 | 1 |
| Rapides | 15 | 1.47 | 0 |

### High severity hot spots

- **Vernon** leads with 4 high severity inspections
- **St. Tammany** has the highest average severity in the top 10 (2.1)
- The top 5 parishes hold **13 of 46 (28%)** of all high severity cases, suggesting spatial concentration worth prioritizing for crew scheduling

### Type specialization (top 5 parishes by volume)

| Parish | Coastal | Pipeline | Transportation | Utility | Wetland |
|---|---:|---:|---:|---:|---:|
| Vernon | 7 | 10 | 1 | 2 | 1 |
| Plaquemines | 3 | 3 | 1 | 6 | 6 |
| Bossier | 4 | 5 | 1 | 4 | 4 |
| Terrebonne | 4 | 5 | 4 | 1 | 4 |
| Lafourche | 4 | 4 | 4 | 1 | 4 |

Plaquemines skews toward Utility and Wetland work, consistent with its coastal wetland geography. Vernon's Pipeline dominance shows the pipeline corridor density in western Louisiana.

### Urban vs rural coverage:

Parishes were binned into tertiles by land area (small / medium / large). In this synthetic dataset, density per square mile came out roughly equal across tertiles (around 0.01 inspections / sq mi), because points were generated uniformly across Louisiana's bounding box without weighting toward urban infrastructure corridors. On a real dataset (for example pulled from a Survey123 feature service) you would expect small urban parishes to show meaningfully higher density. This outcome is a reflection of the synthetic data generation process and not the underlying spatial logic.

## Project structure

```bash
project-b-parish-analysis/
├── Louisiana_parish_analysis.ipynb     # the main notebook
├── parish_choropleth.png               # static side by side choropleth
├── hot_spots_bar.png                   # top 10 high severity bar chart
├── parish_inspections_map.html         # interactive Folium map
├── data/
│   ├── counties/                       # downloaded TIGER shapefile (gitignored)
│   ├── inspections_with_parishes.gpkg  # enriched inspections as GeoPackage
│   └── parish_summary.csv              # parish level aggregates
└── README.md
```

## To run it

```bash
# Install dependencies (uses parent venv)
pip install geopandas folium matplotlib

# Launch the notebook
jupyter notebook Louisiana_parish_analysis.ipynb
```

## Possible extensions

- Replacing synthetic inspections with a public real dataset such as LDEQ incident reports or Louisiana oil and gas well locations
- Pull live records from an ArcGIS Online feature service using the ArcGIS REST API, then run the same pipeline
- Adding a proximity analysis: distance from each inspection to the nearest water body or wetland polygon
- Produce parish level summary reports as Word documents
- Expose the parish statistics through a FastAPI endpoint so a downstream dashboard can query them live
- Add multi level spatial hierarchy: overlay USACE districts or watershed boundaries in addition to parishes
- Weight the synthetic point generation by parish population or infrastructure density so the urban vs rural analysis has meaningful signal
