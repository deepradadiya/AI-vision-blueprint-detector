from ultralytics import YOLO

def evaluate_yolo():
    model = YOLO("runs/train/blueprint_detector13/weights/best.pt")
    metrics = model.val(data="datasets/dataset/data.yaml", split="test", imgsz=640, conf=0.3)
    print(f"mAP@0.5: {metrics.box.map50}")
    print(f"mAP@0.5:0.95: {metrics.box.map}")
    print(f"Class-wise AP@0.5: {metrics.box.maps}")
    return metrics.box.map50

if __name__ == "__main__":
    map50 = evaluate_yolo()
    print(f"Target Achieved: {map50 > 0.6}")