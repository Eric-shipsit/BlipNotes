# BlipNotes

## Features


## Installation
### Step 1: Clone the project
```
git clone https://github.com/yourusername/echonote.git
cd blipnotes
```

### Step 2: Install Python libraries
```
pip install sounddevice soundfile pydub transformers torch openai-whisper
```

### Step 3: Install FFmpeg
FFmpeg is required to convert audio files (e.g., from WAV to MP3).

📥 Windows
1. Go to the official FFmpeg website: https://ffmpeg.org/download.html

2. Under Windows, click on the link to gyan.dev or BtbN builds.

3. Download the release full build (e.g., ffmpeg-release-essentials.zip).

4. Extract the ZIP file to a folder, for example:
C:\ffmpeg

5. Add FFmpeg to your system PATH:

- Open Windows Search → type Environment Variables

- Click on Edit the system environment variables

- Click Environment Variables

- Under System Variables, find and edit Path

- Add a new entry:
C:\ffmpeg\bin

6. Open a new Command Prompt and check:
```
ffmpeg -version
```
If it prints FFmpeg version info, you're done!

### Optional: Install VB-Cable Virtual Audio Device
[VB-Audio Cable](https://vb-audio.com/Cable/)
This is needed for the application to listen to your computer's input and output sounds. Change your computer's input and output to this after installation.

### Step 4: Run program
```
python main.py
```

## Potential Future features
- Change to live time tanscription
- UI Improvements
- Recording/Summary hub within application

## Acknowledgements 
[Pydub Library](https://github.com/jiaaro/pydub)
[Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
[OpenAI Whisper](https://github.com/openai/whisper)

