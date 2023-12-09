import json
import cv2
import numpy as np

segmentation_mask = cv2.imread("D:\CSC 621\segmentation_mask.png", cv2.IMREAD_GRAYSCALE)

def get_segment_coordinates(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    segment_coordinates = [list(map(int, point[0])) for contour in contours for point in contour]
    return segment_coordinates

json_data = {
    "image_id": "1",
    "segments": [
        {"label": "class1", "coordinates": get_segment_coordinates(segmentation_mask)},
    ]
}


json_string = json.dumps(json_data, indent=2)


with open("segmentation_result.json", "w") as json_file:
    json_file.write(json_string)
