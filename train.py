from ultralytics import YOLO

# Load a model
model = YOLO("yolo11m.pt")  # load a pretrained model (recommended for training)

results = model.train(
    data="solutions/pole_objects/data.yaml",
    epochs=100,
    imgsz=640,
    batch=4,
    device=0,  # force GPU
    amp=False,  # turn off amp
)
