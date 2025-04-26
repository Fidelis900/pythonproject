from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import yaml
import random

# Create chatbot instance
chatbot = ChatBot(
    "ChatBuddy",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///chatbuddy_database.sqlite3"
)

# Load bot questions from YAML
with open('bot_questions.yml', 'r') as file:
    data = yaml.safe_load(file)
    bot_questions = data['questions']

# Create trainer
# Create trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train chatbot with your custom YAML
trainer.train("./train.yml")

# Pick a random first question
first_question = random.choice(bot_questions)
print(f"ChatBuddy: {first_question}")

# Chat Loop
print("Type 'exit' anytime to quit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.get_response(user_input)
    print(f"ChatBuddy: {response}")
