# Geomapping Notebooks

This directory contains Jupyter notebooks and associated files for generating geomaps based on the Noscemus project metadata.

## Subdirectories

The geomapping processes are organized based on the primary metadata set used:

-   **`with_Cleaned_Metadata_Set/`**:
    Contains the notebook (`NOSCEMUS_geomapping_using_cleaned_dataset.ipynb`), input data (`cleaned_sofia.csv`), and outputs/cache related to geomapping using the cleaned and corrected Sofia metadata. This approach leverages enhanced place information for potentially more accurate geocoding.

-   **`with_Nosecmus_Metadata_Set/`**:
    Contains the notebook (`NOSCEMUS_geomapping.ipynb`) and outputs/cache related to geomapping using the original Noscemus project metadata. This represents the baseline geomapping process.

Each subdirectory typically includes:
-   The main Jupyter Notebook (`.ipynb`) for the specific geomapping task.
-   The primary input CSV file (if applicable, like `cleaned_sofia.csv`).
-   Output CSV files (e.g., `noscemus_metadata_with_primary_coords.csv`) containing the metadata enriched with coordinates.
-   Cache files (e.g., `raw_geocoded_places_cache.csv`) to store geocoding results and speed up subsequent runs.

Please refer to the individual notebooks within each subdirectory for detailed execution steps and descriptions of the processes.
