
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from dotenv import load_dotenv
import os

# put the video it here.
video_id = "rNxC16mlO60"
transcript = YouTubeTranscriptApi().fetch(video_id)   # note: instantiating class
print(transcript)

# Assuming your transcript object is called 'transcript'
# transcript.snippets is the list of FetchedTranscriptSnippet

# 1️⃣ Save raw transcript (only text)
raw_file = "Transcript/transcript_raw.txt"
with open(raw_file, "w", encoding="utf-8") as f:
    for snippet in transcript.snippets:
        f.write(snippet.text + "\n")

print(f"Raw transcript saved to {raw_file}")

# 2️⃣ Save transcript with timestamps
timestamp_file = "Transcript/transcript_with_timestamps.txt"
with open(timestamp_file, "w", encoding="utf-8") as f:
    for snippet in transcript.snippets:
        start = snippet.start
        end = start + snippet.duration
        f.write(f"[{start:.2f} --> {end:.2f}] {snippet.text}\n")

print(f"Transcript with timestamps saved to {timestamp_file}")



# -----------------------------------------
# USE YOUR AI STUDIO KEY
# -----------------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# -----------------------------------------
# SETUP MODEL – stable for AI Studio keys
# -----------------------------------------
model = genai.GenerativeModel("models/gemini-2.5-flash")

# -----------------------------------------
# SUMMARY AGENT
# -----------------------------------------
def summarize_text(text):
    prompt = f"""
You are an expert summarizer specializing in long-form educational and scientific content.

Rewrite the following transcript into a **deep, structured, multi-section summary** with:

- Clear section headers
- Bullet points
- Key insights
- Scientific explanations
- Important quotes
- Actionable takeaways
- Real examples from the transcript
- NO missing context
- NO generic statements
- NO compression that removes meaning

Make the summary detailed and useful for study and note-taking.

Transcript:
{text}

Start your summary now:
"""
    response = model.generate_content(prompt)
    return response.text


# -----------------------------------------
# LOAD  TRANSCRIPT
# -----------------------------------------
with open("Transcripts/transcript_raw.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

# -----------------------------------------
# RUN SUMMARY
# -----------------------------------------
summary = summarize_text(transcript)

# SAVE
with open("GenAI_Summary/summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print("✨ Summary saved to summary.txt")
print(summary[:800])


# convert it to markdown file.
input_path = "GenAI_Summary/summary.txt"
output_path = "GenAI_Summary/summary.md"

# Read TXT
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# OPTIONAL: Add a header so your MD looks nice
md_text = f"# Summary\n\n{text}"

# Save as MD
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_text)

print("Markdown file created at:", output_path)


