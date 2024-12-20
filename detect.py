from ultralytics import YOLO

# 加载训练好的模型
model = YOLO("runs/detect/train6/weights/best.pt")

# 进行推理，传入测试图像或图像文件夹路径
results = model("test")  # 也可以是单张图像路径，或者是一个包含多张图像的文件夹路径
for result in results:
    result.show()  # 显示每个推理结果
