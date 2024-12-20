import os
import shutil
import random

# 定义路径
source_images_dir = "./images"
source_labels_dir = "./labels"
val_dir = "./val"
val_images_dir = os.path.join(val_dir, "images")
val_labels_dir = os.path.join(val_dir, "labels")

# 创建 val/images 和 val/labels 目录
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 获取文件列表（自动匹配扩展名）
image_files = sorted(
    [
        f
        for f in os.listdir(source_images_dir)
        if os.path.isfile(os.path.join(source_images_dir, f))
    ]
)
label_files = sorted(
    [
        f
        for f in os.listdir(source_labels_dir)
        if os.path.isfile(os.path.join(source_labels_dir, f))
    ]
)

# 获取文件名和扩展名映射
image_mapping = {os.path.splitext(f)[0]: f for f in image_files}
label_mapping = {os.path.splitext(f)[0]: f for f in label_files}

# 匹配 images 和 labels 的文件名
common_files = set(image_mapping.keys()) & set(label_mapping.keys())

# 转换为列表并排序，确保顺序一致
common_files = sorted(list(common_files))

# 按照 20% 的比例随机抽取
sample_count = max(1, int(len(common_files) * 0.2))  # 至少抽取一个文件
selected_files = random.sample(common_files, sample_count)

# 将选中的文件移动到 val/images 和 val/labels
for file_name in selected_files:
    # 移动 images 文件
    image_file = image_mapping[file_name]
    src_image_path = os.path.join(source_images_dir, image_file)
    dst_image_path = os.path.join(val_images_dir, image_file)
    shutil.move(src_image_path, dst_image_path)

    # 移动 labels 文件
    label_file = label_mapping[file_name]
    src_label_path = os.path.join(source_labels_dir, label_file)
    dst_label_path = os.path.join(val_labels_dir, label_file)
    shutil.move(src_label_path, dst_label_path)

print(f"已成功将 {len(selected_files)} 个文件及其标签移动到 val 目录下。")
