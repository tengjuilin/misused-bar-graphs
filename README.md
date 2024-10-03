# Quantifying Data Distortion in Bar Graphs in Biological Research

T.-J. Lin, M.P. Landry*. Quantifying Data Distortion in Bar Graphs in Biological Research. *bioRxiv* (2024). [DOI: 10.1101/2024.09.20.609464](https://www.biorxiv.org/content/10.1101/2024.09.20.609464)

## Analysis Jupyter Notebooks (`/analysis/`)

- `bar_constants.py`
  - Order: 1
  - Plot settings and constants
- `bar_util.py`
  - Order: 2
  - Utility functions and custom statistics
- `bar-graph-classification.ipynb`
  - Order: 3
  - Classification of articles
  - Graph-level bias analysis
  - Author number analysis
- `bar-graph-examples.ipynb`
  - Order: 0
  - Examples of correct and incorrect bar graphs in Cartesian coordinates
- `lie-factor-quantification.ipynb`
  - Order: 4
  - Quantify extend of data distortion with data distortion metrics by mistake types
    - No grouping
    - Grouped by absolute/relative measurands
    - Grouped by measurand identity
    - Grouped by journals
- `polar-bar-plot.ipynb`
  - Order: 0
  - Examples of bar graphs in polar coordinates

## Data (`/data/`)

- `misused_bar_graph_annotation`
  - Order: 3
  - The raw annotation data file from WebPlotDigitizer v5 stored in folders by journals and mistake types
  - Each article has a visualization value file (viz) and a true value file (val)
- `misused_bar_graph_data`
  - Order: 4
  - CSV data file from WebPlotDigitizer v5 stored in folders by journals and mistake types
  - Each article has a visualization value file (viz) and a true value file (val)
- `misused_bar_graph_figures`
  - Order: 2
  - Misused bar graphs are screenshotted and stored in folders by journals and mistake types
  - Each folder contains a CSV file storing the manually labeled metadata of each figure
- `processed_data`
  - Order: 5
- `zotero_data`
  - Order: 1
  - CSV of Zotero export of articles included in the study
    - "Manual Tags" column contains the categorization of each article
