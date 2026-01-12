import ee

ee.Initialize(project='sentinel2-483807')

# Area of interest
aoi = ee.Geometry.Rectangle([72.85, 19.05, 72.95, 19.15])

# Cloud masking using SCL band
def mask_s2_clouds(image):
    scl = image.select('SCL')
    
    # Keep pixels that are NOT clouds or shadows
    mask = scl.neq(3) \
        .And(scl.neq(8)) \
        .And(scl.neq(9)) \
        .And(scl.neq(10))
    
    return image.updateMask(mask)

# Load Sentinel-2 (UPDATED DATASET)
s2 = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterBounds(aoi)
    .filterDate("2023-01-01", "2023-12-31")
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10))
    .map(mask_s2_clouds)
)

print("Number of images:", s2.size().getInfo())

# Calculate NDVI
def add_ndvi(image):
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
    return image.addBands(ndvi)

s2_ndvi = s2.map(add_ndvi)

# Mean NDVI image
ndvi_image = s2_ndvi.select('NDVI').mean()

# Reduce region (FIXED)
stats = ndvi_image.reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=aoi,
    scale=20,        # increased scale
    maxPixels=1e9,
    bestEffort=True # VERY IMPORTANT
)

print("NDVI stats dictionary:", stats.getInfo())

