import random
import re

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "how are you": ["I'm good, thank you!", "Doing well, how about you?", "I'm fine, thanks!"],
            "what is your name": ["I am a chatbot created by OpenAI.", "You can call me ChatGPT.", "My name is Chatbot."],
            "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
            "default": ["I'm not sure I understand.", "Can you rephrase that?", "I'm here to help!"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        # Remove punctuation
        user_input = re.sub(r'[^\w\s]', '', user_input)
        
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def chat(self):
        print("Chatbot: Hello! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if "bye" in user_input.lower():
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.chat()
