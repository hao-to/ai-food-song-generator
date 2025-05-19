import os
from dotenv import load_dotenv
import sounddevice as sd
from scipy.io.wavfile import write
import assemblyai as aai

load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")


def record(filename="output.wav", duration=5):
    fs = 44100
    print("🎙️ Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print(f"✅ Saved as {filename}")


def speech2text(filename="output.wav"):
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)
    transcript = aai.Transcriber(config=config).transcribe(filename)

    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")

    return transcript.text
