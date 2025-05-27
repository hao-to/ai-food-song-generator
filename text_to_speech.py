import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()

# Get API key from environment
api_key = os.getenv("ELEVENLABS_API_KEY")

# Initialize ElevenLabs
client = ElevenLabs(api_key=api_key)

def speak(text):
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
)

    play(audio)


