🚨 Smart Pose Alert System

A Python-based application that uses computer vision and machine learning to detect human poses in real time.
When a dangerous or specified pose is held for a certain duration, the system triggers an alarm, saves snapshots, and logs the event.

Built using OpenCV, MediaPipe, Threading, and Python.

🚀 Features

🎯 Real-time pose detection using MediaPipe

⚠️ Smart alert system (Hands Up, Hand on Face, Lying Down/Fall)

🔊 Audible alarm when dangerous poses are detected

📸 Automatic snapshot saving

📝 Log file generation with timestamps

📊 Real-time FPS display

🎨 Skeleton overlay for landmarks

⏱️ Customizable alert duration

🛠️ Tech Stack

OpenCV – Image processing & webcam handling

MediaPipe Pose – Pose estimation & landmarks

Threading – For background alarm execution

DateTime – For snapshots & logging

Math – Angle-based pose calculations

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/prathameshchougale/pose-alert-system.git
cd pose-alert-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Manual Installation (Optional)
pip install opencv-python mediapipe numpy

4️⃣ Run the Application
python src/main.py

📋 Usage

Starts webcam automatically

Displays real-time skeleton + detected pose

If a dangerous pose is held for 3 seconds, alarm triggers

Press q to exit

After running, check:

logs/pose_alerts.log

snapshots/ folder

🎯 Detected Poses
Pose Name	Description
Standing	Normal upright posture
Sitting	Bent knee sitting posture
Hands Up (Surrender)	Both hands raised above shoulders
Hand on Face	Hand close to face/nose
Lying Down (Fall?)	Possible fall detected
Unknown Pose	No known pattern matched
📁 File Structure
pose-alert-system/
├── src/
│   ├── main.py                # Main application code
│   ├── pose_detector.py       # Pose detection logic (optional modularization)
│   ├── alarm.py               # Alarm functions (optional)
│   └── utils.py               # Helper functions for saving logs/images
│
├── snapshots/                 # Auto-saved alerts (images)
│
├── logs/
│   └── pose_alerts.log        # Log file (generated automatically)
│
├── docs/
│   └── setup_guide.md         # Additional documentation (optional)
│
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation

⚠️ Notes

Ensure proper lighting for better pose detection

Camera must have a clear view of full body

Avoid cluttered backgrounds

False positives may occur if:

   Only half the body is visible

   Multiple people enter the frame