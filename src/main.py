import cv2
import mediapipe as mp
import time
import threading
from pose_detector import PoseDetector
from alarm import AlarmSystem
from utils import save_picture, write_log

# Constants
ALERT_TIME = 3
ALERT_POSES = {"Hands Up (Surrender)", "Hand on Face", "Lying Down (Fall?)"}

# Initialize components
mp_pose = mp.solutions.pose  # Add this line to define mp_pose
mp_draw = mp.solutions.drawing_utils
pose_detector = PoseDetector()
alarm_system = AlarmSystem()

# Global variables
time_pose_started = None
current_pose_name = None
alarm_is_on = False
last_frame_time = 0

# Initialize camera
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Cannot open camera. Check if it's connected.")
    exit()

print(f"{list(ALERT_POSES)}")
print("   Press 'q' to quit.")

try:
    while True:
        # Read frame from camera
        success, frame = camera.read()
        if not success:
            print("Failed to read from camera.")
            break

        # Calculate FPS (Frames Per Second)
        current_time = time.time()
        fps = 1 / (current_time - last_frame_time) if last_frame_time > 0 else 0
        last_frame_time = current_time

        # Convert frame to RGB (MediaPipe needs this)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect pose
        result = pose_detector.pose.process(frame_rgb)

        detected_pose = "No Person Detected"

        if result.pose_landmarks:
            # Draw skeleton on screen
            mp_draw.draw_landmarks(
                frame,
                result.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,  # Now this will work
                landmark_drawing_spec=mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=3),
                connection_drawing_spec=mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2)
            )
            # Detect what pose it is
            detected_pose = pose_detector.check_what_pose(result.pose_landmarks)

            # SMART ALARM LOGIC
            if detected_pose == current_pose_name:
                if (time_pose_started and
                    detected_pose in ALERT_POSES and
                    not alarm_is_on and
                    time.time() - time_pose_started >= ALERT_TIME):

                    print(f"ALERT! Pose '{detected_pose}' held for {ALERT_TIME} seconds!")
                    write_log(f"ALERT: {detected_pose}")
                    save_picture(frame.copy(), detected_pose)
                    alarm_system.start_alarm()
                    alarm_is_on = True

            else:
                # Pose changed → reset timer and stop alarm
                current_pose_name = detected_pose
                time_pose_started = time.time()
                if alarm_is_on:
                    print("Alarm stopped — pose changed.")
                    write_log("ALARM STOPPED — pose changed")
                    alarm_system.stop_alarm()
                    alarm_is_on = False

            # VISUAL FEEDBACK
            if detected_pose in ALERT_POSES and time_pose_started:
                seconds_held = int(time.time() - time_pose_started)
                seconds_left = max(0, ALERT_TIME - seconds_held)
                status_text = f"{detected_pose} | Held: {seconds_held}s | Alarm in: {seconds_left}s"
                if alarm_is_on:
                    status_text = "ALARM ACTIVE — " + detected_pose
                    # Add red border when alarming
                    frame = cv2.copyMakeBorder(frame, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 255))
            else:
                status_text = detected_pose

        else:
            if alarm_is_on:
                print("Alarm stopped — person left the screen.")
                write_log("ALARM STOPPED — person lost")
                alarm_system.stop_alarm()
                alarm_is_on = False
            current_pose_name = None
            time_pose_started = None
            status_text = detected_pose

        cv2.putText(frame, f"Status: {status_text}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.putText(frame, f"FPS: {int(fps)}", (20, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Show the frame
        cv2.imshow("Smart Pose Alert System", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    alarm_system.stop_alarm()
    camera.release()
    cv2.destroyAllWindows()
    print("Check 'logs/pose_alerts.log' and saved pictures in snapshots/!")