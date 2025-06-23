import cv2
import os

# 设置图像所在的文件夹路径
image_folder = 'renders//renders'  # 替换为你的图像文件夹路径
video_name = 'renders//render.mp4'  # 输出视频文件名
fps = 30  # 视频帧率

# 获取所有图像文件名，并按名称排序
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()  # 按文件名排序

# 确保有图像文件
if not images:
    raise ValueError("指定的文件夹中没有图像文件。")

# 读取第一张图像以获取尺寸信息
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
if frame is None:
    raise ValueError(f"无法读取图像文件: {first_image_path}")

height, width, layers = frame.shape

# 创建 VideoWriter 对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 mp4v 编码器
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

# 将每张图像写入视频
for image in images:
    image_path = os.path.join(image_folder, image)
    img = cv2.imread(image_path)
    if img is None:
        print(f"警告: 无法读取图像文件 {image_path}，跳过该帧。")
        continue
    video.write(img)

# 释放资源
video.release()

print(f"视频已成功生成: {video_name}")