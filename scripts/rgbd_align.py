import numpy as np
import json
import cv2

class DEPTH_TO_POINTCLOUD:
    def __init__(self, distance_to_camera_path, rgb_path, camera_params_path) -> None:
        self._distance_to_camera_path = distance_to_camera_path
        self._rgb_path = rgb_path
        self._camera_params_path = camera_params_path
        self._setup()

    def _setup(self):
        self._read_params()
        self._get_intrinsic_matrix()
        self._get_extrinsic_matrix()

    def _read_params(self):
        self._depth = np.load(self._distance_to_camera_path)
        self._rgb = cv2.imread(self._rgb_path, cv2.COLOR_BGR2RGB)
        with open(self._camera_params_path) as f:
            self._camera_params = json.load(f)

        self._h_aperture = self._camera_params["cameraAperture"][0]
        self._v_aperture = self._camera_params["cameraAperture"][1]
        self._h_aperture_offset = self._camera_params["cameraApertureOffset"][0]
        self._v_aperture_offset = self._camera_params["cameraApertureOffset"][1]
        self._focal_length = self._camera_params["cameraFocalLength"]
        self._h_resolution = self._camera_params["renderProductResolution"][0]
        self._v_resolution = self._camera_params["renderProductResolution"][1]
        self._cam_t = self._camera_params["cameraViewTransform"]

    def _get_intrinsic_matrix(self):
        self._focal_x = self._h_resolution * self._focal_length / self._h_aperture
        self._focal_y = self._v_resolution * self._focal_length / self._v_aperture
        self._center_x = self._h_resolution / 2
        self._center_y = self._v_resolution / 2
        self.intrinsic_matrix = np.array([[self._focal_x, 0, self._center_x],
                                          [0, self._focal_y, self._center_y],
                                          [0, 0, 1]])
        return self.intrinsic_matrix
        
    def _get_extrinsic_matrix(self):
        self._cam_pose = np.linalg.inv(np.resize(self._cam_t, (4,4))).T
        return self._cam_pose
        
    def get_pcd(self):
        points = []
        colors = []
        depth_scale = 1000
        for u in range(self._h_resolution):
            for v in range(self._v_resolution):
                # print("u: "+str(u)+", v: "+str(v))
                d = self._depth[v][u]
                z = d / depth_scale
                x = (u - self._center_x) * z / self._focal_x
                y = (v - self._center_y) * z / self._focal_y
                r = self._rgb[v][u][2] / 255
                g = self._rgb[v][u][1] / 255
                b = self._rgb[v][u][0] / 255
                # print([x, y, z], [r, g, b])
                points.append([x, y, z])
                colors.append([r, g, b])

        return points, colors