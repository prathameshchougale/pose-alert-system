import math
import mediapipe as mp

mp_pose = mp.solutions.pose

class PoseDetector:
    def __init__(self):
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        
    def get_angle(self, point_a, point_b, point_c):
        """Calculate angle between 3 points (in degrees)."""
        angle_rad = math.atan2(point_c.y - point_b.y, point_c.x - point_b.x) - math.atan2(point_a.y - point_b.y, point_a.x - point_b.x)
        angle_deg = abs(math.degrees(angle_rad))
        return angle_deg if angle_deg <= 180 else 360 - angle_deg

    def check_what_pose(self, landmarks):
        """Look at body points and return what pose person is doing."""
        # Shortcuts to body parts
        lm = landmarks.landmark
        left_shoulder = lm[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_elbow = lm[mp_pose.PoseLandmark.LEFT_ELBOW]
        right_elbow = lm[mp_pose.PoseLandmark.RIGHT_ELBOW]
        left_wrist = lm[mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = lm[mp_pose.PoseLandmark.RIGHT_WRIST]
        left_hip = lm[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = lm[mp_pose.PoseLandmark.RIGHT_HIP]
        left_knee = lm[mp_pose.PoseLandmark.LEFT_KNEE]
        right_knee = lm[mp_pose.PoseLandmark.RIGHT_KNEE]
        left_ankle = lm[mp_pose.PoseLandmark.LEFT_ANKLE]
        right_ankle = lm[mp_pose.PoseLandmark.RIGHT_ANKLE]
        nose = lm[mp_pose.PoseLandmark.NOSE]

        # 1. HANDS UP
        if left_elbow.y < left_shoulder.y - 0.05 and right_elbow.y < right_shoulder.y - 0.05:
            return "Hands Up (Surrender)"

        # 2. HAND ON FACE
        left_hand_to_face = math.sqrt((left_wrist.x - nose.x)**2 + (left_wrist.y - nose.y)**2)
        right_hand_to_face = math.sqrt((right_wrist.x - nose.x)**2 + (right_wrist.y - nose.y)**2)
        if left_hand_to_face < 0.15 or right_hand_to_face < 0.15:
            return "Hand on Face"

        # 3. FALL DETECTION
        avg_shoulder_y = (left_shoulder.y + right_shoulder.y) / 2
        avg_ankle_y = (left_ankle.y + right_ankle.y) / 2
        if avg_shoulder_y > avg_ankle_y - 0.1:
            return "Lying Down (Fall?)"

        # 4. Calculate knee angles
        left_knee_bend = self.get_angle(left_hip, left_knee, left_ankle)
        right_knee_bend = self.get_angle(right_hip, right_knee, right_ankle)

        # 4. STANDING
        if (left_knee_bend > 160 and right_knee_bend > 160 and
            left_hip.y < left_knee.y and right_hip.y < right_knee.y):
            return "Standing"

        # 5. SITTING
        if (left_knee_bend < 120 and right_knee_bend < 120 and
            left_hip.y < left_knee.y and right_hip.y < right_knee.y):
            return "Sitting"

        return "Unknown Pose"