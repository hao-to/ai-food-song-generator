# 🎤 AI Food Song Generator

Welcome to my take on how to use AI and 2 of my favorite things: food and music.

This project lets you enter any dish you love (or hate) and generates a **sarcastic, over-the-top song** about it — powered by OpenAI.

---

## 🍔 What does it do?

- Asks you for a dish (e.g. *"Spaghetti"*, *"Bratwurst"*, or *"Frozen Pizza"*)
- You can now **type it** or **say it out loud** 🎙️ (via [AssemblyAI](https://www.assemblyai.com/))
- Then lets you choose a song style:
  - Rap
  - Love Song
  - Breakup Song
  - Angry Metal Song
  - Sad Country Ballad
  - Or just pick one randomly 🎲
- It creates a *ridiculous little food song* about your dish using GPT

---

## 🧠 Why?

Because not every AI project needs to change the world.  
Sometimes, you just want to hear a country ballad about currywurst.  
Or, if you're like me: procrastinate working on *real* projects by doing this kind of nonsense instead.

---

## ▶️ How to run

1. **Install the dependencies**

```bash
pip install -r requirements.txt
```
⚠️ To play back the generated audio, you may need [FFmpeg](https://ffmpeg.org/) installed on your system.
On macOS, you can install it with Homebrew:

```bash
brew install ffmpeg
```

2. Set up your environment

Create a .env file with your API keys:
```
OPENAI_API_KEY=your-openai-api-key
ASSEMBLYAI_API_KEY=your-assemblyai-key
ELEVENLABS_API_KEY=your-elevenlabs-api-key

```

3. **Run the app**  

```
python main.py
```

## 🤖 Tech stack

- Python 3.12
- OpenAI GPT API
- AssemblyAI Speech-to-Text API
- dotenv for keeping API keys secret
- sounddevice & scipy for recording audio
- ElevenLabs Text-to-Speech API 

## 🛡️ License

MIT – feel free to remix this app into a metal ode to your leftovers.

---

✨ Coming soon
- More weird song styles
- Maybe: autoplaying songs?
- Maybe: saving lyrics to a file?
- Optional: have your song read aloud using AI voices (enabled by ElevenLabs)
- Maybe: never finishing serious projects again (because you'll create a one hit wonder or even a breakthrough album?) 🤷

## 💌 Author (me)

Inspired by a little madness, sleep deprivation, 3 kids and 2 cats.

