import os
import cv2
import numpy as np

def resize_image(img, target_size=(800, 800), padding=True):
    """
    调整图像大小为目标尺寸，可以选择是否进行填充以保持宽高比
    :param img: 原始图像 (numpy array)
    :param target_size: 目标尺寸 (width, height)
    :param padding: 是否保持比例并在短边填充黑色
    :return: 处理后的图像
    """
    if not padding:
        return cv2.resize(img, target_size)

    # 获取原图尺寸
    h, w = img.shape[:2]
    target_w, target_h = target_size

    # 计算缩放比例
    scale = min(target_w / w, target_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # 缩放图像
    resized_img = cv2.resize(img, (new_w, new_h))

    # 创建空白图像并居中粘贴
    canvas = 255 * np.zeros((target_h, target_w, 3), dtype=np.uint8)
    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    canvas[y:y+new_h, x:x+new_w] = resized_img

    return canvas


def batch_resize_images(input_dir, output_dir, target_size=(800, 800), padding=True):
    """
    批量调整图像尺寸
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    supported_formats = ('.jpg', '.jpeg', '.png')
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)
            if img is None:
                print(f"无法读取图像: {filename}")
                continue

            resized_img = resize_image(img, target_size=target_size, padding=padding)

            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, resized_img)
            print(f"已处理并保存: {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="批量将图像调整为指定尺寸（默认 800x800）")
    parser.add_argument("--size", type=int, default=800, help="目标尺寸（默认 800x800）")
    parser.add_argument("--no-padding", action="store_true", help="不保持比例，直接拉伸图像")

    args = parser.parse_args()

    batch_resize_images(
        input_dir=".\\sample2\\",
        output_dir=".\\sample3\\",
        target_size=(args.size, args.size),
        padding=not args.no_padding
    )