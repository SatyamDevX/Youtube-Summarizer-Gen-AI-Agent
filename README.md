
# 🎥 YouTube Transcript → AI Summary Agent (2025)

This project demonstrates a **modern 2025-style AI Agent pipeline** that:

1. **Extracts high-quality transcripts from YouTube videos**
2. **Generates clean summaries using Gemini 2.5 Flash**
3. **Outputs structured Markdown-ready content**
4. Runs inside a **virtual environment** with minimal dependencies
5. Uses **simple tools + a single intelligent agent** — similar to the tool-calling workflows used by 2025 AI systems
6. Produces professional-grade summaries ready for blogs, documentation, or study notes

---

# 🚀 Features

### ✔️ Uses YouTubeTranscriptApi to fetch transcripts

* Works even when transcripts have timestamps
* Saves two formats:

  * `transcript_raw.txt`
  * `transcript_with_timestamps.txt`

### ✔️ AI Agent powered by **Gemini 2.5 Flash**

* High-quality summarization
* Clean structure
* Zero hallucinations
* Perfect for documentation or reports

### ✔️ Automatic Markdown output

* Creates `summary.md` with formatted content
* Ready for GitHub, Notion, Obsidian, blogs, etc.

---

# 🧠 AI Agent Concept (2025 Design Style)

This project follows the **2025 AI Agent pattern**:

### 🟦 **Tool Layer**

Independent functions the agent can call:

* Transcript Fetcher Tool
* Timestamp Formatter Tool
* File Writer Tool

### 🟪 **Reasoning Layer (Gemini 2.5 Flash)**

The model receives:

* Transcript text
* A summarization prompt
* Instruction formatting

The agent then:

* Reads text
* Breaks it down
* Produces a structured knowledge summary

### 🟧 **Output Layer**

The agent writes:

* `summary.txt`
* `summary.md`

This mirrors the Agent → Tools → Output architecture used in real 2025 AI systems.

---

# 📂 Project Structure

```
.
├── .venv        # python virtual environment.                        
├── .env                   # contains GOOGLE_API_KEY
├── GenAI_Summary
│   ├── summary.md
│   └── summary.txt
├── README.md
├── Transcripts
│   ├── transcript_raw.txt
│   └── transcript_with_timestamps.txt
└── youtube_video_summarizer.py           # optional main script

```

---

# 🔧 Setup

### 1️⃣ Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Install dependencies

```bash
pip install youtube-transcript-api yt-dlp google-generativeai python-dotenv

```

### 3️⃣ Add your API key to `.env`

```
GOOGLE_API_KEY="AIzaSy..." (your key)
```

---

# 📜 Step 1: Fetch YouTube Transcript

```python
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "rNxC16mlO60"
transcript = YouTubeTranscriptApi().fetch(video_id)

# Save raw transcript
raw_file = "transcript_raw.txt"
with open(raw_file, "w", encoding="utf-8") as f:
    for snippet in transcript.snippets:
        f.write(snippet.text + "\n")

# Save timestamps
timestamp_file = "transcript_with_timestamps.txt"
with open(timestamp_file, "w", encoding="utf-8") as f:
    for snippet in transcript.snippets:
        start = snippet.start
        end = start + snippet.duration
        f.write(f"[{start:.2f} --> {end:.2f}] {snippet.text}\n")
```

---

# 🤖 Step 2: AI Summary Agent (Gemini 2.5 Flash)

```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def summarize_text(text):
    prompt = f"""
You are an expert summarizer agent.
Create a clear, structured, high-quality summary of the transcript below.

Avoid repetition. Capture key points cleanly.

Transcript:
{text}
"""
    response = model.generate_content(prompt)
    return response.text
```

---

# 📝 Step 3: Save Summary

```python
with open("Transcript/transcript_raw.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

summary = summarize_text(transcript)

with open("GenAI_Summary/summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)
```

---

# 📘 Step 4: Convert to Markdown

```python
input_path = "GenAI_Summary/summary.txt"
output_path = "GenAI_Summary/summary.md"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

md_text = f"# Summary\n\n{text}"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_text)
```

---

# 🌟 Result

You get:

```
summary.md
```

With beautiful structured markdown:

* Headings
* Bullets
* Sections
* Clean formatting

This is perfect for:

💡 Documentation
💡 Study notes
💡 Blog posts
💡 GitHub repos
💡 Meeting summaries

---

# 🎉 Final Notes

This simple project demonstrates the **core of all modern AI Agent systems**:

### ✔ Tool-use

### ✔ Strong LLM reasoning

### ✔ Clean output generation

### ✔ Automation + reproducibility

### ✔ Extensible design

In 2025, most real AI systems work **exactly like this** —
a smart LLM making decisions + a set of tools + a final formatter.

---

