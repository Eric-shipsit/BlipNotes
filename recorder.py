import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
import threading
import time
from datetime import datetime
from transcriber import transcribe_and_summarize
import os

is_recording = False
samplerate = 44100
channels = 2
recorded_data = []
filename = ""

def generate_filename():
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")

def callback(indata, frames, time, status):
    if is_recording:
        recorded_data.append(indata.copy())

def start_recording(status_label, button):
    global is_recording, recorded_data, filename
    is_recording = True
    recorded_data = []
    filename = generate_filename()
    status_label.config(text="Recording...")

    def record_loop():
        with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
            while is_recording:
                sd.sleep(200)
        save_recording(status_label)

    threading.Thread(target=record_loop, daemon=True).start()
    button.config(text="Stop Recording")

def stop_recording(status_label, button):
    global is_recording
    is_recording = False
    button.config(text="Start Recording")
    status_label.config(text="Saving...")

def save_recording(status_label):
    # Ensure recordings directory exists
    recordings_dir = "recordings"
    os.makedirs(recordings_dir, exist_ok=True)

    wav_file = os.path.join(recordings_dir, f"{filename}.wav")
    with sf.SoundFile(wav_file, mode='x', samplerate=samplerate, channels=channels, subtype='PCM_16') as file:
        for chunk in recorded_data:
            file.write(chunk)

    audio = AudioSegment.from_wav(wav_file)
    louder_audio = audio + 10  # boost by 10 dB
    mp3_file = os.path.join(recordings_dir, f"{filename}.mp3")
    louder_audio.export(mp3_file, format="mp3")
    status_label.config(text="Saved. Transcribing...")

    transcribe_and_summarize(mp3_file, status_label)
