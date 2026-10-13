
import os
from google import genai
from google.genai import types
from calculator import calculate

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing.")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        tools=[calculate]
    )
)

print("Gemini AI Agent")
print("Calculator tool enabled.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    if not user_input:
        continue

    try:
        response = chat.send_message(user_input)
        print(f"\nAgent: {response.text}\n")

    except Exception as e:
        print(f"\nError: {type(e).__name__}: {e}\n")
