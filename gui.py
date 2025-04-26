import tkinter as tk
from recorder import start_recording, stop_recording

def launch_gui():
    window = tk.Tk()
    window.title("Audio Recorder & Summarizer")
    window.geometry("400x200")

    status_label = tk.Label(window, text="Idle", font=("Arial", 12))
    status_label.pack()

    def toggle_recording():
        if record_btn['text'] == "Start Recording":
            start_recording(status_label, record_btn)
        else:
            stop_recording(status_label, record_btn)

    record_btn = tk.Button(window, text="Start Recording", font=("Arial", 14),
                           command=toggle_recording)
    record_btn.pack(pady=20)

    window.mainloop()