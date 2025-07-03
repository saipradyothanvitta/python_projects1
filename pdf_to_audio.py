import pdfplumber
from gtts import gTTS

def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def text_to_mp3(text, mp3_path, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save(mp3_path)
    print(f"MP3 saved to {mp3_path}")

# Example usage
pdf_file = "filehandling.pdf"
mp3_output = "output.mp3"

text = pdf_to_text(pdf_file)
if text.strip():
    text_to_mp3(text, mp3_output)
else:
    print("No text found in the PDF.")
