🚨 Smart Pose Alert System

A Python-based application that uses computer vision and machine learning to detect human poses in real time.
When a dangerous pose is held for a certain duration, the system triggers an alarm, saves snapshots, and logs the event.

Built with OpenCV, MediaPipe, Threading, and Python.

🚀 Features

🎯 Real-time pose detection using MediaPipe

⚠️ Smart alert system (Hands Up, Hand on Face, Lying Down/Fall)

🔊 Audible alarm when dangerous poses are detected

📸 Automatic snapshot saving

📝 Event logging with timestamps

📊 Real-time FPS display

🎨 Skeleton overlay for body landmarks

⏱️ Customizable alert duration

🛠️ Tech Stack

OpenCV – Image processing & webcam handling

MediaPipe Pose – Pose estimation & body landmarks

Threading – Background alarm execution

DateTime – Snapshot timestamps & logging

Math – Angle-based pose calculations

⚙️ Setup Instructions
1️⃣ Clone the Repository
```bash
git clone https://github.com/prathameshchougale/pose-alert-system.git
cd pose-alert-system
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Manual Installation (Optional)
```bash
pip install opencv-python mediapipe numpy
```

4️⃣ Run the Application
```bash
python src/main.py
```

📋 Usage

Starts webcam automatically

Displays real-time skeleton + detected pose

If a dangerous pose is held for 3 seconds, alarm triggers

Press q to exit

After running:

Check logs in logs/pose_alerts.log

Check snapshots in snapshots/

🎯 Detected Poses
Pose Name	Description
Standing	Normal upright posture
Sitting	Bent knee sitting posture
Hands Up (Surrender)	Hands raised above shoulders
Hand on Face	Hand close to face or nose
Lying Down (Fall?)	Possible fall detected
Unknown Pose	Does not match known pattern
📁 File Structure
pose-alert-system/
├── src/
│   ├── main.py                # Main application code
│   ├── pose_detector.py       # Pose detection logic
│   ├── alarm.py               # Alarm functions
│   └── utils.py               # Helper functions
│
├── snapshots/                 # Auto-saved snapshots
├── logs/
│   └── pose_alerts.log        # Auto-generated log file
├── docs/
│   └── setup_guide.md         # Extra documentation
├── requirements.txt
└── README.md

⚠️ Notes

Use good lighting for accurate pose detection

Camera should clearly see your full body

Avoid cluttered backgrounds

False positives may occur when:

   Only half-body is visible
   
   Multiple people in the frame
