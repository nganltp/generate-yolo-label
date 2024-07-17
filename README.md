# Video to Frame and YOLO Label Generator

This project consists of two main scripts: `video2frame.py` and `generate_label.py`. These scripts facilitate the conversion of a video into individual frames and the generation of YOLO format labels for the detected objects in each frame.

## File Structure

- `video2frame.py`: Python script to convert a video into individual frames.
- `generate_label.py`: Python script to generate YOLO format labels for the detected objects in the frames.
- `labels/`: Folder to store the generated YOLO format labels.
- `model/`: Folder containing the pre-trained YOLO model and related files.
- `output_frame/`: Folder to store the output frames extracted from the video.

## Usage

1. Place your input video file in the project folder.
2. Run `video2frame.py` to convert the video into individual frames. The output frames will be saved in the `output_frame/` folder.
3. Run `generate_label.py` to generate YOLO format labels for the detected objects in the frames. The generated labels will be stored in the `labels/` folder.

## Requirements

- Python 3.9
- OpenCV (cv2)
- Pre-trained YOLO model (located in the `model/` folder)

