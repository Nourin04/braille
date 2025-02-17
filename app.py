import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pyttsx3
import speech_recognition as sr

# Function to convert text to Braille (A-Z characters)
def text_to_braille(text):
    braille_alphabet = {
        "A": "⠁", "B": "⠃", "C": "⠉", "D": "⠙", "E": "⠑", "F": "⠋", "G": "⠛", "H": "⠓", 
        "I": "⠊", "J": "⠚", "K": "⠅", "L": "⠇", "M": "⠍", "N": "⠝", "O": "⠕", "P": "⠏", 
        "Q": "⠟", "R": "⠗", "S": "⠎", "T": "⠞", "U": "⠥", "V": "⠧", "W": "⠺", "X": "⠭", 
        "Y": "⠽", "Z": "⠵"
    }
    return " ".join([braille_alphabet.get(char.upper(), "") for char in text if char.isalpha()])

# Function to convert speech to text using SpeechRecognition
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand the audio.")
            return ""
        except sr.RequestError:
            st.write("Sorry, there was an issue with the speech recognition service.")
            return ""

# Streamlit layout
st.title("Text to Braille and Speech to Braille Converter")

# Option 1: Text to Braille
st.header("Convert Text to Braille")
text_input = st.text_input("Enter Text", "")
if text_input:
    braille_text = text_to_braille(text_input)
    st.write(f"Braille Representation: {braille_text}")

# Option 2: Speech to Braille
st.header("Convert Speech to Braille")
if st.button("Convert Speech to Text & Braille"):
    text_from_speech = speech_to_text()
    if text_from_speech:
        braille_from_speech = text_to_braille(text_from_speech)
        st.write(f"Braille Representation from Speech: {braille_from_speech}")
