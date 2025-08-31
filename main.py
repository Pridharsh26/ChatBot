import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

# Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand your voice."
    except sr.RequestError as e:
        return f"Error from Speech Recognition service: {e}"

# Gemini LLM
def get_gemini_response(question):
    response = chat.send_message(question)
    return response.text

# Convert text to speech and play
def speak(text):
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio = AudioSegment.from_file(fp, format="mp3")
    play(audio)

# Streamlit UI
st.set_page_config(page_title="Voice Gemini Bot")
st.header("🎙️ Voice Controlled Gemini Bot")

if st.button("🎤 Speak"):
    user_input = recognize_speech()
    st.write(f"🗣️ You said: {user_input}")
    response = get_gemini_response(user_input)
    st.write(f"🤖 Gemini: {response}")
    speak(response)
