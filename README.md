
# Medical Image Segmentation using Level Set Method

This repository contains a Python implementation of medical image segmentation using the deformable model-based level set method. The code is designed to work with DICOM image series, commonly used in medical imaging like CT or MRI scans.

## Description

The script performs segmentation on medical images using the level set method, which is particularly effective for capturing complex shapes in medical images. It includes functionalities for loading DICOM series, preprocessing images, interactive seed point selection, and applying level set segmentation.

###### This was performed on Chest CT Scan Datasets : https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=80969742 

## Features

- Load and process DICOM image series.
- Rescale image intensities and enhance contrast using adaptive histogram equalization.
- Interactive selection of seed points for segmentation.
- Apply level set segmentation with adjustable parameters.
- Iterative approach for refining segmentation results.

## Getting Started

### Dependencies

- Python 3.x
- SimpleITK
- NumPy
- Matplotlib
- IPython
- Jupyter Notebook (for running the script interactively)

### Installing

- Ensure Python 3.x is installed on your system.
- Install required Python packages:
  ```bash
  pip install simpleitk numpy matplotlib ipython jupyter
- Use for running Jupyter notebook : https://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/

### Executing the Program

- Clone the repository or download the script.
- Open the script in Jupyter Notebook.
- Run the cells sequentially to perform image segmentation.

### Usage

**Load DICOM Series:** Specify the directory containing DICOM files and the number of files to load.
**Preprocess Images:** View the original and enhanced images.
**Select Seed Point: Use interactive sliders to select the seed point and its radius.
**Segmentation: Adjust parameters like factor, RMS error, and iterations for level set segmentation.
**Iterative Segmentation: Observe the segmentation results after each iteration.

### Author

Aryaman Patel

### Acknowledgments
https://simpleitk.readthedocs.io/en/master/filters.html 
