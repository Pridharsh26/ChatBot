import google.generativeai as genai
import os

# Replace this with your Gemini API key
API_KEY = "AIzaSyCdaTArHRW9kQvmO0PZjxMY5N34sCY0MI8"

# Set up the Gemini API key
genai.configure(api_key=API_KEY)

# Load the Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Chat loop
chat = model.start_chat()

print("🤖 Gemini Chatbot (type 'bye' to exit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break
    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text)
    except Exception as e:
        print("⚠️ Error:", e)
