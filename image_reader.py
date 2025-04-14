"""
image_reader.py

This module provides a utility function to read an image file into a
numpy array using Matplotlib.

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
read_image(path):
    Reads the image from the given file path and returns it as a numpy array.
    The function uses Matplotlib's `imread` to load the image.

    Parameters:
    path (str): The file path of the image to be read.

    Returns:
    numpy.ndarray: The image represented as a multidimensional array.

Usage:
-------
To use this module, call the `read_image` function with the file path to the
image.

Example:
--------
from image_reader import read_image

image = read_image('example_image.png')
"""


import matplotlib.pyplot as plt


def read_image(path):
    """
    Reads an image file and returns it as a numpy array.

    Parameters:
    ----------
    path : str
        The file path of the image to be read.

    Returns:
    -------
    numpy.ndarray
        The image represented as a multidimensional array.

    Notes:
    ------
    This function uses Matplotlib's `imread` method to load the image. Ensure
    that the file path provided points to a valid image file. Supported
    formats include common image types like PNG, JPEG, etc.

    Example:
    --------
    image = read_image('example_image.png')
    """

    return plt.imread(path)