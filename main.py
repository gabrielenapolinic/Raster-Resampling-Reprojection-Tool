import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.enums import Resampling as ResamplingMethod

def resample_raster(input_path, output_path, new_resolution=1):
    """
    Resamples a raster to a specified resolution and reprojects it to the EPSG:3857 (Web Mercator) CRS.

    Parameters:
        input_path (str): Path to the input raster file.
        output_path (str): Path to save the resampled raster file.
        new_resolution (float): Target resolution in CRS units (default is 1).
    """
    # Open the input raster file
    with rasterio.open(input_path) as src:
        # Define the target CRS as EPSG:3857 (Web Mercator)
        dst_crs = "EPSG:3857"

        # Calculate the transform, width, and height for the new resolution and CRS
        transform, width, height = calculate_default_transform(
            src.crs,               # Source CRS
            dst_crs,               # Target CRS
            src.width,             # Width of the source raster
            src.height,            # Height of the source raster
            *src.bounds,           # Bounding box of the source raster
            resolution=(new_resolution, new_resolution)  # Target resolution
        )

        # Copy and update the source raster's profile
        profile = src.profile.copy()
        profile.update({
            'crs': dst_crs,        # Update the CRS to EPSG:3857
            'transform': transform, # Update the affine transformation matrix
            'width': width,         # New raster width in pixels
            'height': height,       # New raster height in pixels
            'driver': 'GTiff'       # Output format: GeoTIFF
        })

        # Write the resampled raster to the output file
        with rasterio.open(output_path, 'w', **profile) as dst:
            # Process each band in the input raster
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),       # Read data from the source band
                    destination=rasterio.band(dst, i),  # Write data to the destination band
                    src_transform=src.transform,        # Source affine transform
                    src_crs=src.crs,                    # Source CRS
                    dst_transform=transform,            # Target affine transform
                    dst_crs=dst_crs,                    # Target CRS (EPSG:3857)
                    resampling=ResamplingMethod.bilinear # Resampling method: bilinear interpolation
                )

    print(f"Raster saved to {output_path} with {new_resolution}x{new_resolution} resolution in CRS {dst_crs}.")

# Example usage
input_raster_path = r"/path/to/input_raster.tif"
output_raster_path = r"/path/to/output_raster_resampled.tif"

# Run the resampling function
resample_raster(input_raster_path, output_raster_path)


# In[ ]:




