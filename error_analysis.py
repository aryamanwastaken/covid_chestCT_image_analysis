import cv2
import json
import numpy as np
from skimage.metrics import pairwise, confusion_matrix

segmentation_result = cv2.imread("segmentation_result.png", cv2.IMREAD_GRAYSCALE)

with open("ground_truth_annotation.json", "r") as json_file:
    ground_truth_annotation = json.load(json_file)

ground_truth_mask = np.zeros_like(segmentation_result)
for segment in ground_truth_annotation["segments"]:
    coordinates = np.array(segment["coordinates"])
    cv2.fillPoly(ground_truth_mask, [coordinates], 255)

segmentation_result_binary = (segmentation_result > 0).astype(np.uint8)
ground_truth_mask_binary = (ground_truth_mask > 0).astype(np.uint8)

intersection = np.logical_and(segmentation_result_binary, ground_truth_mask_binary)
union = np.logical_or(segmentation_result_binary, ground_truth_mask_binary)
iou = np.sum(intersection) / np.sum(union)

print(f"Intersection over Union (IoU): {iou}")
