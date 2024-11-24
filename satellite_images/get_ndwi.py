from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, MimeType, CRS, BBox
from keys import sentinel_client_id, sentinel_client_secret

# Konfiguráció
config = SHConfig()
config.instance_id = 'CassiniHackathon2024'
config.sh_client_id = sentinel_client_id
config.sh_client_secret = sentinel_client_secret

# Terület meghatározása (példa koordináták)
bbox = BBox(bbox=[16.37, 48.20, 16.38, 48.21], crs=CRS.WGS84)

# NDWI lekérdezés
evalscript = """
//VERSION=3
function setup() {
    return {
        input: ["B03", "B08"],
        output: { bands: 1 }
    };
}

function evaluatePixel(sample) {
    let ndwi = (sample.B03 - sample.B08) / (sample.B03 + sample.B08);
    return [ndwi];
}
"""

request = SentinelHubRequest(
    evalscript=evalscript,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A,
            time_interval=('2024-11-01', '2024-11-23')
        )
    ],
    responses=[
        SentinelHubRequest.output_response('default', MimeType.TIFF)
    ],
    bbox=bbox,
    size=(512, 512),
    config=config
)

response = request.get_data()
ndwi_image = response[0]

# Kép mentése
from PIL import Image
import numpy as np

ndwi_image = np.clip(ndwi_image * 255, 0, 255).astype(np.uint8)
Image.fromarray(ndwi_image).save('ndwi_image.tiff')
