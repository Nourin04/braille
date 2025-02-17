import streamlit as st
from gtts import gTTS
import speech_recognition as sr
import os

# Function to convert text to Braille (use a Braille conversion function here)
def text_to_braille(text):
    # You can implement your own Braille conversion logic or use a pre-built mapping
    braille_dict = {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛',
        'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝',
        'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥',
        'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', ' ': '⠂'
    }
    braille_text = ''.join([braille_dict.get(char, char) for char in text.lower()])
    return braille_text

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            st.write("Sorry, there was an error with the speech recognition service.")
            return ""

# Function to convert text to speech using gTTS
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")  # Plays the saved file (for Windows)
    # For Linux, use: os.system("mpg321 output.mp3")

# Streamlit Interface
st.title("Text to Braille and Speech to Braille Converter")

# Text to Braille Conversion
text_input = st.text_area("Enter text to convert to Braille")
if text_input:
    braille_output = text_to_braille(text_input)
    st.write(f"Braille Output: {braille_output}")

# Speech to Text Conversion
if st.button("Convert Speech to Text"):
    speech_text = speech_to_text()
    if speech_text:
        braille_from_speech = text_to_braille(speech_text)
        st.write(f"Braille Output from Speech: {braille_from_speech}")

# Text to Speech (Optional)
text_to_speech_button = st.button("Convert Text to Speech")
if text_to_speech_button:
    if text_input:
        text_to_speech(text_input)
    elif speech_text:
        text_to_speech(speech_text)


