import image_reader
import lidar_reader

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Paths to the image and point cloud files
    img_path = r"./data/018282150.png"
    lid_path = r"./data/018282150.pcd"

    # Read the image and pcd-file
    img = image_reader.read_image(img_path)
    pcd = lidar_reader.read_pcd(lid_path)

    # Camera matrix
    camera_matrix = np.array([[307.4315301, 0., 387.17404027],
                              [0., 304.42845041, 157.74584542],
                              [0, 0, 1.0]])
    # Extrinsics
    rotation = np.array([
        [0.30389705, -0.95224289, -0.02966584],
        [-0.02329885,  0.02370089, -0.99944757],
        [0.95241995,  0.30442035, -0.01498354]])
    translation = np.array([[-0.167], [1.685], [-1.587]])
    # Generate 4x4 transformation matrix
    transformation_lidar_to_cam = np.eye(4)
    transformation_lidar_to_cam[:3, :3] = rotation
    transformation_lidar_to_cam[:3, 3] = translation.flatten()

    # Decompose the pcd infoprmation
    point_xyz = pcd[:, 0:3]
    intensity_raw = pcd[:, 6]

    # Convert pcd to homogeneous coordinates to match the projection dimensions
    num_points = point_xyz.shape[0]
    lidar_points_hom = np.hstack((point_xyz, np.ones((num_points, 1))))

    # Transform pcd points to camera frame
    cam_points_hom = transformation_lidar_to_cam @ lidar_points_hom.T
    cam_points = cam_points_hom[:3, :]  # Remove homogeneous coordinate

    # Project points onto image plane
    image_points_hom = camera_matrix @ cam_points
    # Normalizing step
    image_points = image_points_hom[:2, :] / image_points_hom[2, :]

    # Convert to pixel coordinates
    pixel_x = np.round(image_points[0, :]).astype(int)
    pixel_y = np.round(image_points[1, :]).astype(int)

    # Normalize intensity values
    intensity_min, intensity_max = np.min(intensity_raw), np.max(intensity_raw)
    intensity_normalized = (
        (intensity_raw - intensity_min)
        / (intensity_max - intensity_min)
        * 255).astype(np.uint8)

    # Apply color mapping using matplotlib's colormap
    colormap = plt.get_cmap('jet')
    color_map = (colormap(intensity_normalized)[:, :3] * 255).astype(np.uint8)

    # Copy the image to avoid modifying the original
    img_combined = img.copy()

    # Ensure points are within image bounds
    for x, y, color in zip(pixel_x, pixel_y, color_map):
        if 0 <= x < img_combined.shape[1] and 0 <= y < img_combined.shape[0]:
            img_combined[y, x, :] = color

    # Show projection
    plt.imshow(img_combined)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
