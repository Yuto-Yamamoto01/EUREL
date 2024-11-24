# Water level estimation based on satellite images and historical data

<center><img src="images/logo.png"></center>

We've trained a computer (AI) to predict future water levels using historical data ([1] and [2]) from rivers. We're also analyzing satellite images [3] to measure the weight of the water in rivers. By comparing this weight to known water levels, we can estimate the current depth of the river at any point.

To do this, we're using images from Sentinel-2 satellites and processing them to highlight water bodies. We then measure the distance between the water's edge and the riverbank on these images.

![sentinel to ndwi  to distance](images/turning%20satellite%20image%20to%20ndwi%20and%20measure%20on%20ndwi.png)

Data that we are using:

1. [River Water Level 2002-present (vector), global, Near Real Time – version 2](https://land.copernicus.eu/en/products/water-bodies/water-level-rivers-near-real-time-v2.0)
2. [Water Level Rivers 2002-present (vector), global, per overpass - version 2](https://www.wekeo.eu/data?view=dataset&dataset=EO%3ACLMS%3ADAT%3ACLMS_GLOBAL_WL_RIVERS_V2_DAILY_GEOJSON)
3. [Normalized Difference Water Index Sentinel-2 images](https://custom-scripts.sentinel-hub.com/sentinel-2/ndwi/)

Data that we collected for this project:
4. [River Water Level Data in the EU](https://www.kaggle.com/datasets/sndorburian/river-water-level-data-in-the-eu)


Live scripts: 
- https://www.kaggle.com/code/sndorburian/get-the-shoreline-on-satellite-images?scriptVersionId=209282505
- https://www.kaggle.com/code/sndorburian/measure-distances-on-satellite-images/edit/run/209167117
- https://www.kaggle.com/code/sndorburian/using-sentinel-satellite-images/edit/run/209140110

----------------------------------------------------------

> The NDWI is used in [`using-sentinel-satellite-images.ipynb`](satellite_images/using-sentinel-satellite-images.ipynb) to monitor changes related to water content in water bodies. As water bodies strongly absorb light in the visible to the infrared electromagnetic spectrum, NDWI uses green and near-infrared bands to highlight water bodies. It is sensitive to built-up land and can result in over-estimating water bodies.
>
> $$NDWI = \frac{green-nir}{green+nir}$$
>
> Values Description: Index values greater than 0.5 usually correspond to water bodies. Vegetation usually corresponds to much smaller values and built-up areas between zero and 0.2.
>
> more: https://custom-scripts.sentinel-hub.com/custom-scripts/hls/ndwi/


## Distance Measurements

Distance measurements are crucial for analyzing spatial relationships in satellite images. By calculating the distance between various points of interest, we can derive meaningful insights about the geographical features and their spatial distribution.

In the [`measure-distances.ipynb`](satellite_images/measure-distances-on-satellite-images.ipynb) notebook, we utilize several methods to measure distances:

**Geodesic Distance**: This is the shortest distance between two points on the Earth's surface, considering the Earth's curvature. It is often calculated using the Haversine formula:
    $$a = \sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1) \cos(\phi_2) \sin^2\left(\frac{\Delta \lambda}{2}\right)$$
    
$$c = 2 \cdot \text{atan2}\left(\sqrt{a}, \sqrt{1-a}\right)$$
    
$$d = R \cdot c$$
    where \( \phi \) is latitude, \( \lambda \) is longitude, and \( R \) is the Earth's radius.

These distance measurements help in various applications such as mapping water bodies, monitoring environmental changes, and urban planning.

For more details, refer to the `measure-distances.ipynb` notebook.
