import datetime
import cv2
import os

def save_picture(frame, pose_name, snapshots_dir="snapshots"):
    """Save current frame as image file with timestamp."""
    # Create snapshots directory if it doesn't exist
    os.makedirs(snapshots_dir, exist_ok=True)
    
    now = datetime.datetime.now()
    filename = f"alert_{pose_name}_{now.strftime('%Y%m%d_%H%M%S')}.jpg"
    filepath = os.path.join(snapshots_dir, filename)
    cv2.imwrite(filepath, frame)
    print(f"Picture saved: {filepath}")

def write_log(message, logs_dir="logs"):
    """Add message to log file with timestamp."""
    # Create logs directory if it doesn't exist
    os.makedirs(logs_dir, exist_ok=True)
    
    now = datetime.datetime.now()
    filepath = os.path.join(logs_dir, "pose_alerts.log")
    with open(filepath, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")