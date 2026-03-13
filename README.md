# HI Everyone

## About the Repo

</div>

---

## 🗂️ Projects Overview

| # | 🚀 Project | 📦 Libraries Used | ⚡ What It Does |
|---|-----------|------------------|----------------|
| 1 | 📂 File Analyzer | `pandas` | Cleans & summarizes CSV, JSON, XLSX, XLS files |
| 2 | 🎙️ Sound Recorder | `sounddevice`, `scipy` | Records 15 seconds of audio & saves as `.wav` |
| 3 | 🔐 Password Generator | `random`, `string` | Generates strong random passwords instantly |

---

## 📂 1. File Analyzer

> Drag in any data file — get instant insights!

A handy script that **automatically opens, cleans, and summarizes** your data files. Supports `.csv`, `.json`, `.xlsx`, and `.xls` formats.

**✨ Features:**
- Auto-detects file type and reads it with Pandas
- Drops fully empty rows & columns (basic cleaning)
- Prints `info()`, `head()`, `tail()`, and `describe()` for quick insight

**📦 Install dependencies:**
```bash
pip install pandas 
```

**▶️ Run:**
```bash
python file_analyzer.py
```

---

## 🎙️ 2. Sound Recorder

> Hit run, speak for 15 seconds, done!

A minimal audio recorder that **captures your microphone input** for 15 seconds and saves it as a `.wav` file — no complicated setup needed.

**✨ Features:**
- Auto-saves output as `recording.wav`
- Uses `sounddevice` to capture and `scipy.io.wavfile` to save

**📦 Install dependencies:**
```bash
pip install sounddevice scipy
```

**▶️ Run:**
```bash
python sound_recorder.py
```

```
🎙️  Recording for 15 seconds... Speak now!
✅  Done! Saved as recording.wav
```

---

## 🔐 3. Password Generator

> Strong passwords in one second, every time.

A clean, no-nonsense script that generates **secure, random passwords** using Python's built-in `random` and `string` libraries.

**✨ Features:**
- Mix of uppercase, lowercase, digits & special characters
- Customizable password length
- Instant output — no libraries to install!

**▶️ Run:**
```bash
python password_generator.py
```

```
🔐 Generated Password: Xq7#mK!2vLpR@9wT
```

---


---

## ⚙️ Requirements

```bash
# Install all at once
pip install pandas openpyxl sounddevice scipy
```

| Tool | Version |
|------|---------|
| Python | 3.8 or above |
| pandas | Latest |
| sounddevice | Latest |
| scipy | Latest |

> ---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/python-mini-projects.git

# 2. Navigate into it
cd python-mini-projects

# 3. Install dependencies
pip install pandas openpyxl sounddevice scipy

# 4. Run any script!
python file_analyzer.py
python sound_recorder.py
python password_generator.py
```

---
</div>
