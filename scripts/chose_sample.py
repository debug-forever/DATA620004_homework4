import os
import shutil

# 设置源文件夹和目标文件夹路径
source_folder = '.\\3'  # 替换为你的源文件夹路径
destination_folder = '.\\sample4'  # 替换为你的目标文件夹路径

# 创建目标文件夹（如果它不存在）
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 获取源文件夹中的所有图片文件名
image_files = [f for f in os.listdir(source_folder) if f.startswith('frame') and f.endswith('.png')]
image_files.sort()  # 确保文件按顺序排列

# 每间隔25张挑选一张图片
selected_images = image_files[::10]

# 将挑选出的图片复制到目标文件夹
for img in selected_images:
    source_path = os.path.join(source_folder, img)
    destination_filename = img  # 在文件名前加上'S'
    destination_path = os.path.join(destination_folder, destination_filename)
    shutil.copy2(source_path, destination_path)
    print(f"Copied {img} to {destination_folder}")

print("Selection process completed.")