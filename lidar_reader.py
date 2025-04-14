"""
lidar_reader.py

This module provides functionality to read LiDAR point cloud data from a PCD
(Point Cloud Data) file. The binary file is parsed to extract point cloud data
and header information.

Author:
-------
Daniel Schneider
Email: daniel.schneider@hs-kempten.de

Created:
--------
April 8, 2025

Revisions:
----------
- April 8, 2025: Initial creation.

Functions:
-----------
read_pcd(file_path):
    Reads a binary PCD file and returns the point cloud data as a numpy array.

    Parameters:
    file_path (str): Path to the PCD file.

    Returns:
    numpy.ndarray: A 2D array where each row represents a point in the point
    cloud.

Usage:
-------
To use this module, call the `read_pcd` function with the file path to the
PCD-file.

Example:
--------
from lidar_reader import read_pcd

point_cloud = read_pcd('example.pcd')
"""

import numpy as np


def read_pcd(file_path):
    """
    Reads a binary PCD (Point Cloud Data) file and extracts the point cloud
    data.

    Parameters:
    ----------
    file_path : str
        Path to the PCD file to be read.

    Returns:
    -------
    numpy.ndarray
        A 2D numpy array where each row represents a point in the point cloud,
        and columns contain the attributes (e.g., x, y, z coordinates, rgb,
        intensity, etc.).

    Notes:
    ------
    - This function parses the header of the PCD file to determine metadata,
    such as the number of points in the file.
    - Binary data following the header is decoded into a numpy array.
    - Ensure the input file is in binary PCD format.

    Example:
    --------
    point_cloud = read_pcd('example.pcd')
    """
    with open(file_path, 'rb') as f:  # Open in binary mode
        lines = []
        while True:
            line = f.readline()
            lines.append(line.decode('ascii', errors='ignore').strip())
            if line.startswith(b'DATA'):
                break

        # Parse header to get the number of points
        header = lines[:-1]
        for h in header:
            if h.startswith('POINTS'):
                num_points = int(h.split()[-1])
                break

        # Read binary data after the header
        data = f.read()
        point_cloud = np.frombuffer(data, dtype=np.float32)
        # Reshape based on the number of points
        point_cloud = point_cloud.reshape((num_points, -1))
        return point_cloud