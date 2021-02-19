"""
This example illustrates the automatic download of STRM data, and adding of
shading to create a so-called "Shaded Relief SRTM".

Originally contributed by Thomas Lecocq (http://geophysique.be).

"""
import numpy as np
import cartopy.crs as ccrs
from cartopy.io import srtm
import matplotlib.pyplot as plt

from cartopy.io import PostprocessedRasterSource, LocatedImage
from cartopy.io.srtm import SRTM3Source
import cartopy.feature as cfeature

def shade(located_elevations):
    """
    Fungsi untuk memberikan hillshade pada data DEM

    """
    new_img = srtm.add_shading(located_elevations.image,
                               azimuth=135, altitude=15)
    return LocatedImage(new_img, located_elevations.extent)


Source=SRTM3Source
name='SRTM3'
fig = plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
    
# Define a raster source which uses the SRTM data and applies the
# shade function when the data is retrieved.
shaded_srtm = PostprocessedRasterSource(Source(), shade)

# Add the shaded SRTM source to our map with a grayscale colormap.
ax.add_feature(cfeature.OCEAN, zorder=10)
ax.add_raster(shaded_srtm, cmap='Greys', alpha=.75)

# This data is high resolution, so pick a small area which has some
# interesting orography.
ax.set_extent([118.5, 119.2, -3.25, -2.65])
ax.set_xlabel("Longitude [deg]")
ax.set_ylabel("Latitude [deg]")

gl = ax.gridlines(draw_labels=True, dms=False, x_inline=False, y_inline=False, zorder=11)

gl.xlabels_top = False
gl.ylabels_right = False

plt.legend(*eq.legend_elements("sizes", num=4, func=lambda x: x**(1/2.5)))
plt.savefig("test_srtm.png", dpi=300)
