# 🎧 Audiobook Generator

A simple and modern **AI-powered audiobook generator** built with **Python, Streamlit, and Microsoft Edge-TTS**. Convert text into natural-sounding speech and generate audiobook audio directly from your browser.

## ✨ Features

* 📝 Convert text into spoken audio
* 🎙️ Multiple natural-sounding voices
* 🌍 Support for different languages and accents
* ⚡ Fast text-to-speech generation using Edge-TTS
* 🎨 Clean and interactive Streamlit interface
* 🔊 Listen to generated audio directly in the browser
* 💾 Download generated audiobook audio
* 🖥️ Runs locally on your computer
* 🔐 No API key required for Edge-TTS

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Streamlit** — Web interface
* **Edge-TTS** — Microsoft Edge's online text-to-speech service
* **asyncio** — Asynchronous audio generation

## 📂 Project Structure

```text
audiobook-generator/
│
├── main.py              # Main Streamlit application
├── voice.py
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Files ignored by Git
│
└── .venv/              # Virtual environment (not committed)
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ZikCodes/Audiobook-Generator.git
cd vocalise
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet:

```bash
pip install streamlit edge-tts
```

Then create one with:

```bash
pip freeze > requirements.txt
```

### 4. Run the application

```bash
streamlit run main.py
```

The application should open automatically in your browser.

If it doesn't, Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

## 🎙️ How It Works

The application follows a simple workflow:

```text
User enters text
       ↓
Selects a voice
       ↓
Streamlit sends the text to Edge-TTS
       ↓
Edge-TTS generates speech
       ↓
Generated audio is returned
       ↓
User listens or downloads the audiobook
```

## 🗣️ Voice Selection

Edge-TTS provides a variety of voices, including different languages, accents, genders, and speaking styles.

Example voices:

```text
en-US-AriaNeural
en-US-GuyNeural
en-GB-SoniaNeural
en-GB-RyanNeural
```

You can add additional voices to the application depending on your requirements.

## 📦 Requirements

Example `requirements.txt`:

```text
streamlit
edge-tts
```

## 🖼️ Application Preview



```markdown
![Audiobook Generator](Demo\\demo_img1.png)
```



## 🔮 Future Improvements

Some features that could be added in future versions:

* [ ] Upload `.txt` files
* [ ] Upload PDF documents
* [ ] Upload Word documents
* [ ] Automatically split long books into chapters
* [ ] Generate separate audio files for each chapter
* [ ] Adjustable speech rate
* [ ] Adjustable pitch
* [ ] Adjustable volume
* [ ] Chapter navigation
* [ ] Audiobook metadata support
* [ ] Cover image generation
* [ ] Multiple audio formats
* [ ] Audio merging
* [ ] Progress indicator for large books
* [ ] Custom voice selection
* [ ] Cloud deployment

## ⚠️ Limitations

* Edge-TTS requires an internet connection to generate speech.
* Very large amounts of text may need to be processed in smaller chunks.
* Voice availability depends on the voices provided by Edge-TTS.
* Generated audio quality and availability depend on the underlying Microsoft Edge TTS service.



## 📄 License

This project is open source and available under the **MIT License**.

## 👨‍💻 Author

**Zik**

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

### ⭐ Built with Python, Streamlit & Edge-TTS
