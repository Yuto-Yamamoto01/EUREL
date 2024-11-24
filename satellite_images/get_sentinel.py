from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, MimeType, CRS, BBox
import matplotlib.pyplot as plt
import numpy as np
from keys import sentinel_client_id, sentinel_client_secret

# Konfiguráció
config = SHConfig()
config.instance_id = 'CassiniHackathon2024'
config.sh_client_id = sentinel_client_id
config.sh_client_secret = sentinel_client_secret

# Terület meghatározása (példa koordináták)
bbox = BBox(bbox=[16.37, 48.20, 16.38, 48.21], crs=CRS.WGS84)

# Műholdkép lekérdezés
evalscript = """
//VERSION=3
function setup() {
    return {
        input: ["B04", "B03", "B02"],
        output: { bands: 3 }
    };
}

function evaluatePixel(sample) {
    return [sample.B04, sample.B03, sample.B02];
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
image = response[0]

# Kép normalizálása és megjelenítése Jupyter Notebookban
image = np.clip(image / 10000, 0, 1)
plt.imshow(image)
plt.title('Sentinel-2 Image')
plt.axis('off')
plt.show()
