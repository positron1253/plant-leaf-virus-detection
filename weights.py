from ultralytics import YOLO


model=YOLO()
model.train(data="PlantDoc.v4i.yolov8/data.yaml",epochs=50)