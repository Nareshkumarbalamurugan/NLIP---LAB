import random

# Predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I am fine.", "I'm doing well!", "All good!"],
    "your name": ["I am a simple chatbot.", "You can call me ChatBot."],
    "help": ["I can answer basic questions.", "Try asking about my name or say hello."],
    "bye": ["Goodbye!", "See you later!", "Have a nice day!"]
}

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break

    found = False

    for key in responses:
        if key in user_input:
            print("Chatbot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Chatbot: Sorry, I didn't understand that.")