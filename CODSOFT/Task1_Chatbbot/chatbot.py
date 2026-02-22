import re
import random

def greet():
    return random.choice([
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! Need any help?"
    ])

def get_name_response(user_input):
    name_match = re.search(r"my name is (\w+)", user_input)
    if name_match:
        name = name_match.group(1)
        return f"Nice to meet you, {name.capitalize()}!"
    return None

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "exit":
        return "Goodbye! Have a productive day."

    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        return greet()

    elif "your name" in user_input:
        return "I am a rule-based AI chatbot created for the CODSOFT internship."

    elif "how are you" in user_input:
        return "I'm functioning optimally. Thanks for asking!"

    elif "help" in user_input:
        return "You can greet me, ask my name, tell me your name, or type 'exit' to quit."

    elif re.search(r"\b(weather)\b", user_input):
        return "I cannot fetch real-time weather data yet."

    name_response = get_name_response(user_input)
    if name_response:
        return name_response

    return "I'm not sure how to respond to that."

def main():
    print("🤖 AI ChatBot Initialized. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "exit":
            break

if __name__ == "__main__":
    main()