# Sensor Data Projection for ADAS

This repository contains a Python script to visualize LiDAR point cloud data projected onto a camera image. The project is part of the **"Software Development Methods"** lecture in the **Advanced Driver Assistance Systems (ADAS)** Master's program (2025).

## Overview

The script performs the following tasks:

- Reads camera image and LiDAR point cloud
- Applies extrinsic and intrinsic camera calibration
- Projects 3D LiDAR points into the 2D image plane
- Colors projected points based on LiDAR intensity
- Displays the resulting image overlay

This visualization helps understand the sensor fusion pipeline, particularly the spatial alignment between LiDAR and camera systems.

## File Structure

```
├── main.py               # Entry point: performs projection and visualization
├── image_reader.py       # Utility to read and preprocess image files
├── lidar_reader.py       # Utility to load and parse PCD files
├── data/
│   ├── 018282150.png     # Sample image
│   └── 018282150.pcd     # Corresponding LiDAR point cloud
```

## Requirements

Make sure you have the following installed:

- Python 3.8+
- NumPy
- Matplotlib
- Pandas

You can install dependencies using:

```bash
pip install numpy matplotlib pandas
```

or alternatively

```bash
pip install -r requirements.txt
```

## Usage

To run the script:

```bash
python main.py
```

Make sure the `data` directory contains the corresponding `.png` and `.pcd` files with matching filenames.

## Camera & LiDAR Configuration

- **Camera Intrinsics**:

  ```
  [[307.43, 0.00, 387.17],
   [0.00, 304.43, 157.75],
   [0.00, 0.00, 1.00]]
  ```

- **Extrinsic Transformation (LiDAR → Camera)**:
  - **Rotation** and **Translation** are encoded in a 4×4 transformation matrix.
  - This matrix aligns the LiDAR coordinate system to the camera frame.

The given point cloud is given as:
![Lidar input](https://github.com/schneider-daniel/SEM25-solution/blob/76f9d9394b69c5640946ea1478be5b346c298664/pcd.png?raw=true)

Whereby the input image is already undistorted:
![Image input](https://github.com/schneider-daniel/SEM25-python/blob/cd6a9ca5037bd475acbe6f1815c44f2dd4d037e7/data/018282150.png?raw=true)

## Output

The result is a 2D camera image overlaid with LiDAR points color-coded by intensity:

- High intensity → brighter colors
- Low intensity → darker colors

Example output:

![Projection Output](https://github.com/schneider-daniel/SEM25-solution/blob/76f9d9394b69c5640946ea1478be5b346c298664/projection.png?raw=true)

## License

This project is intended for educational use within the ADAS Master's program. It is provided along with the MIT license.

---

Happy coding!
