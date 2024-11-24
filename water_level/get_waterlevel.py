import json
import csv

file_path = 'c_gls_WL_202410192045_0000000008709_ALTI_V2.2.0.json'

# Load the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

data_points = json_data.get('data', [])
# Example: Accessing specific data from the "data" array
data_list = []
for point in data_points:
    date = point['datetime']
    height = point['orthometric_height_of_water_surface_at_reference_position']
    data_list.append([date, height])

with open("Rhine_river_water_level.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data_list)
