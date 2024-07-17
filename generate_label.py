import cv2
import os
from ultralytics import YOLO

image_folder = 'output_frame'
label_folder = 'labels'
head_model = YOLO('model/yolov8m_v2.pt')

def generate_yolo_label(image_path, objects, image_width, image_height):
    label_content = ""
    for obj in objects:
        label_content += f"{obj['class']} {obj['x_center']/image_width} {obj['y_center']/image_height} {obj['width']/image_width} {obj['height']/image_height}\n"
    return label_content

def annotate_and_generate_label(image_path, output_label_path):
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    results = head_model.predict(img, conf=0.4, verbose=False, classes=[0], device='cuda:0')[0].boxes
    
    detected_objects = []
    for bbox, conf, cls in zip(results.xyxy, results.conf, results.cls):
        [x1, y1, x2, y2] = [int(index) for index in bbox.tolist()]
        detected_objects.append({
            "class": int(cls),
            "x_center": (x1 + x2) / 2,
            "y_center": (y1 + y2) / 2,
            "width": x2 - x1,
            "height": y2 - y1
        })
    # detected_objects = [
    #     {"class": "person", "x_center": 100, "y_center": 50, "width": 30, "height": 60},
    #     {"class": "car", "x_center": 200, "y_center": 150, "width": 50, "height": 40}
    # ]
    
    label_content = generate_yolo_label(image_path, detected_objects, width, height)
    
    label_filename = os.path.splitext(os.path.basename(image_path))[0] + ".txt"
    label_filepath = os.path.join(output_label_path, label_filename)
    with open(label_filepath, "w") as label_file:
        label_file.write(label_content)

    return detected_objects

def delete_images_with_empty_objects(image_path, label_objects):
    if not label_objects:
        os.remove(image_path)

os.makedirs(label_folder, exist_ok=True)

for image_filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_filename)
    
    detected_objects = annotate_and_generate_label(image_path, label_folder)
    
    delete_images_with_empty_objects(image_path, detected_objects)
