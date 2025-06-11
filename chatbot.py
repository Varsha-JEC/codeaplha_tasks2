import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot():
    print("🤖 ChatBot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    speak("Hello! I'm your friendly chatbot. Type bye to exit.")

    while True:
        user_input = input("👤 You: ").lower()

        if user_input in ["hi", "hello"]:
            response = "Hi there!"
        elif user_input == "how are you":
            response = "I'm fine, thanks! How about you?"
        elif user_input in ["bye", "goodbye", "exit"]:
            response = "Goodbye! Have a great day!"
            print(f"🤖 ChatBot: {response}")
            speak(response)
            break
        elif user_input == "what is your name":
            response = "I'm ChatBot 1.0, nice to meet you!"
        else:
            response = "Sorry, I don't understand that."

        print(f"🤖 ChatBot: {response}")
        speak(response)

# Run the chatbot
chatbot()