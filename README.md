# ☄️ rocky - hud assistant

> "amaze! you work, i watch. save stars (and grades), question-friend!"

**rocky** is a modular, context-aware vision engine. it’s a silent partner that lives in your f8 key. 

whether you're stuck on a complex assembly instruction for a cybersecurity lab, or you're mid-match in *marvel rivals* wondering why your team is throwing and need a quick strategy pivot, rocky looks at your screen and gives you the context you’re missing.

### 🏗️ setup

**option 1: clone repo**
git installed, run this in your terminal:
```bash
git clone https://github.com/voidchecksam/rocky.git
cd rocky
```

**option 2: manual**
1. download `main.py` directly from this repo.
2. create a new folder on your desktop (call it `rocky` or whatever).
3. drop `main.py` inside that folder.

**final steps (common for both):**
1. **prerequisites:** make sure you have python 3.10+ installed.
2. **install dependencies:** open your terminal in the project folder and run:
   ```bash
   pip install pynput pillow plyer groq
   ```
   NOTE: ill make a requirements.txt once i get it to a stable 1.0 release.
3. **api key:** get a free vision-compatible key from [groq](https://console.groq.com/). 
4. **configure:** open `main.py` in vscode and replace `"YOUR_API_KEY_HERE"` with your actual key. (don't leak this, please).
5. **run it:** ```bash
   python main.py
   ```
6. **use:** hit **f8** anytime. rocky will grab your screen, analyze it, and hit you with a windows notification.

amaze,! save the stars! ☄️

### 🛠️ open source
i’m keeping the code raw so you can break it, fix it, and make it yours. OR HELP ME OUT !!!!!!!!!!!
* **api forks:** currently on **groq** (llama 4 scout) because it's fast and free (and im broke). swap it for gemini, openai, or local ollama if you want.
* **persona forks:** change the system prompt in the code. turn him into jarvis, HAL 9000, or whatever else your twisted brain got you thinking. 
* **os forks:** currently optimized for windows. feel free to port it to linux (wayland/x11) or mac.

### 🚀 features
* **stealth mode:** f8 takes a screenshot, sends it to the cloud, and gives you a windows notification. no bulky ui.
* **token saver:** auto-resizes your 4k/1080p shots before sending. saves bandwidth and keeps you within free tier limits.
* **companion energy:** right now it's an analyst; soon it’ll be a companion that asks why you're playing *death stranding* as a walking simulator or helps you pick a counter-hero in *marvel rivals*.

### 🛰️ roadmap (future plans)
* **live assistance:** moving from screenshots to a low-fps live stream for real-time coaching.
* **gui optimization:** a transparent, minimalist overlay so you don't even need the notification center.
* **proper audio:** integrating eridian-style tts (proper audio, tones, etc).
* **bug squashing:** constant refactoring to make the hotkey listener more stable during high-cpu gaming.

### 🐛 bug reports
found a bug? rocky is confused? 
please open an **issue** on this repo. tell me what happened, what OS you're on, and if you were mid-game or mid-lab. i'll try to fix it between classes.

### 🎓 why?
i like rocky, and i like working alone. a little companion helps. 

### 📜 license
**mit license**
copyright (c) 2026 **abdul muizz**
