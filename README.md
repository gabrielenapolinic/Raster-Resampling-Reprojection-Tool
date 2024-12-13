# Raster-Resampling-Reprojection-Tool

## Overview
This Python script provides functionality to resample raster datasets to a specified resolution and reproject them to the EPSG:3857 (Web Mercator) coordinate reference system. It utilizes the `rasterio` library to handle geospatial raster data efficiently.

## Features
- Resample raster files to a custom resolution (default is 1x1 unit).
- Reproject rasters to EPSG:3857 (Web Mercator).
- Outputs the result as a GeoTIFF file.

## Requirements
- Python 3.x
- `rasterio` library

## Usage
1. Define the input raster file path and the desired output file path.
2. Run the script, providing the paths and optional resolution.

Example:
```python
input_raster_path = "/path/to/input_raster.tif"
output_raster_path = "/path/to/output_raster_resampled.tif"

resample_raster(input_raster_path, output_raster_path)
```

## Notes
- Ensure the `rasterio` library is installed before running the script.
- The default resampling method is bilinear interpolation, but this can be modified in the script if needed.

