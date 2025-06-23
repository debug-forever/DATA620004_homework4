import os
import json
import numpy as np
from read_write_model import read_images_binary, read_cameras_binary

def qvec2rotmat(qvec):
    return np.array([
        [
            1 - 2 * qvec[2]**2 - 2 * qvec[3]**2,
            2 * qvec[1]*qvec[2] - 2 * qvec[0]*qvec[3],
            2 * qvec[3]*qvec[1] + 2 * qvec[0]*qvec[2]
        ],
        [
            2 * qvec[1]*qvec[2] + 2 * qvec[0]*qvec[3],
            1 - 2 * qvec[1]**2 - 2 * qvec[3]**2,
            2 * qvec[2]*qvec[3] - 2 * qvec[0]*qvec[1]
        ],
        [
            2 * qvec[1]*qvec[3] - 2 * qvec[0]*qvec[2],
            2 * qvec[2]*qvec[3] + 2 * qvec[0]*qvec[1],
            1 - 2 * qvec[1]**2 - 2 * qvec[2]**2
        ]
    ])

def main():
    sparse_dir = ".\\COLMAP_test\\test4"
    output_file = "transforms_train4.json"

    images = read_images_binary(os.path.join(sparse_dir, "images.bin"))
    cameras = read_cameras_binary(os.path.join(sparse_dir, "cameras.bin"))

    frames = []
    for i, image in images.items():
        rotation = qvec2rotmat(image.qvec)
        translation = image.tvec.reshape(3, 1)
        w2c = np.concatenate([rotation, translation], axis=1)
        w2c = np.vstack([w2c, [0, 0, 0, 1]])

        # NeRF 使用 c2w（世界到相机的逆）
        c2w = np.linalg.inv(w2c)

        cam = cameras[image.camera_id]

        if cam.model == "SIMPLE_PINHOLE" or cam.model == "SIMPLE_RADIAL":
            fl_x = cam.params[0]
            fl_y = cam.params[0]
            cx = cam.params[1]
            cy = cam.params[2]
        elif cam.model == "PINHOLE":
            fl_x = cam.params[0]
            fl_y = cam.params[1]
            cx = cam.params[2]
            cy = cam.params[3]

        frame = {
            "file_path": f"images/{image.name}",
            "transform_matrix": c2w.tolist(),
            "fl_x": fl_x,
            "fl_y": fl_y,
            "cx": cx,
            "cy": cy,
        }
        frames.append(frame)

    out = {
        "frames": frames,
        "camera_angle_x": 2 * np.arctan2(cam.params[1], fl_x),
    }

    with open(output_file, "w") as f:
        json.dump(out, f, indent=4)

if __name__ == "__main__":
    main()