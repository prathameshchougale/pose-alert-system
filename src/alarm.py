import winsound
import threading

class AlarmSystem:
    def __init__(self):
        self.beep_signal = None
        self.beep_worker = None

    def make_beep_sound(self):
        """Keep beeping until told to stop."""
        while self.beep_signal and not self.beep_signal.is_set():
            winsound.Beep(1000, 400) 
            threading.Event().wait(0.1)

    def start_alarm(self):
        """Start beeping in background."""
        if self.beep_worker and self.beep_worker.is_alive():
            return
        self.beep_signal = threading.Event()
        self.beep_worker = threading.Thread(target=self.make_beep_sound, daemon=True)
        self.beep_worker.start()

    def stop_alarm(self):
        """Stop beeping."""
        if self.beep_signal:
            self.beep_signal.set()
            self.beep_signal = None