import whisper
from transformers import pipeline
import textwrap
import tkinter as tk
import os

def transcribe_and_summarize(mp3_path, status_label):
    status_label.config(text="Transcribing...")

    # Ensure folder for summaries and transcripts exists
    output_dir = "summary"
    os.makedirs(output_dir, exist_ok=True)

    # Load Whisper model
    model = whisper.load_model("base")
    result = model.transcribe(mp3_path)
    transcript = result["text"]

    # Save transcript to text file in summary folder
    base_filename = os.path.splitext(os.path.basename(mp3_path))[0]
    transcript_path = os.path.join(output_dir, f"{base_filename}_transcript.txt")
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    # Load summarization model
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Split into chunks if needed
    def split_text(text, max_len=1024):
        return textwrap.wrap(text, max_len, break_long_words=False)

    chunks = split_text(transcript)
    summary_parts = []
    for chunk in chunks:
        max_len = min(len(chunk.split()), 150)
        min_len = max(20, max_len // 3)
        summary = summarizer(chunk, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
        summary_parts.append(summary)

    summary = "\n\n".join(summary_parts)

    # Save summary to text file in summary folder
    summary_path = os.path.join(output_dir, f"{base_filename}_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)

    status_label.config(text="Done.")
    show_summary_popup(summary, transcript_path)

def show_summary_popup(summary, transcript_path):
    def open_transcript():
        if os.path.exists(transcript_path):
            with open(transcript_path, "r", encoding="utf-8") as f:
                transcript_text = f.read()
            transcript_window = tk.Toplevel()
            transcript_window.title("Transcript")
            transcript_window.geometry("500x400")
            text_widget = tk.Text(transcript_window, wrap="word", font=("Arial", 12))
            text_widget.insert("1.0", transcript_text)
            text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    summary_window = tk.Toplevel()
    summary_window.title("Summary Notes")
    summary_window.geometry("500x400")

    text_widget = tk.Text(summary_window, wrap="word", font=("Arial", 12))
    text_widget.insert("1.0", summary)
    text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    view_button = tk.Button(summary_window, text="View Transcript", command=open_transcript, font=("Arial", 10))
    view_button.pack(pady=10)
