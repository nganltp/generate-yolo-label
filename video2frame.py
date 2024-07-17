import cv2
import os

second_per_frame = 10
video_folder = '/home/eatlab/recorder'
output_folder = 'output_frame'


os.makedirs(output_folder, exist_ok=True)


video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error opening video file {video_file}")
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        print(f"Error getting FPS for {video_file}")
        continue
    
    frame_interval = int(fps * second_per_frame) 
    frame_count = 0
    success = True
    
    while success:
        success, frame = cap.read()
        if frame_count % frame_interval == 0 and success:
            frame_name = f"{os.path.splitext(video_file)[0]}_frame{frame_count}.jpg"
            frame_path = os.path.join(output_folder, frame_name)
            cv2.imwrite(frame_path, frame)
            print(f"Saved frame {frame_count} from {video_file} to {frame_path}")
        
        frame_count += 1
    
    cap.release()

print("Done!")
