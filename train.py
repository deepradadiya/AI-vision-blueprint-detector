from ultralytics import YOLO

def train_yolo():
    model = YOLO("yolov8n.pt")  # Start with nano for faster inference

    model.train(
        data="datasets/dataset/data.yaml",
        epochs=200,               # More epochs due to small initial dataset
        imgsz=640,                # Standard size
        batch=8,                  # Smaller batch for CPU
        device="cpu",             # No GPU (based on slow inference)
        project="runs/train",
        name="blueprint_detector_v4",
        patience=50,
        lr0=0.0001,               # Very low learning rate
        optimizer="AdamW",
        augment=True,
        hsv_h=0.03,               # Hue
        hsv_s=0.9,                # Saturation
        hsv_v=0.6,                # Value
        degrees=20,               # Rotation
        translate=0.3,            # Translation
        scale=0.7,                # Scaling
        shear=10.0,               # Shearing
        mosaic=0.9,               # Mosaic
        mixup=0.4,                # Mixup
        dropout=0.3,              # Prevent overfitting
        iou=0.5,
        #conf_thres=0.2            # Lower threshold
    )

if __name__ == "__main__":
    train_yolo()