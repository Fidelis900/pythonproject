print("🤖 Hi there! I'm ChatBuddy!")
print("What's your name?")
name = input("=<> ")
# Remove words like "I am", "am", or "my name is"
if name.lower().startswith("i am "):
    name = name[5:]  # remove "i am "
elif name.lower().startswith("am "):
    name = name[3:]  # remove "am "
elif name.lower().startswith("my name is "):
    name = name[11:]  # remove "my name is "
elif name.lower().startswith("i'm "):
    name = name[4:]
elif name.lower().startswith("my names are"):
    name = name[12:]
elif len(name) == 0:
    name = "User"
elif len(name) > 15 :

    print("That's a long name you have there!😎")

elif len(name) <= 2:
    print("That's a short name you have there!😅")
name = name.strip().title()  # Remove leading/trailing spaces
print(f"Nice to meet you, {name}! 😀")
print("How are you feeling today🐱‍🚀 (or type bye to quit)?")
mood = input("=<> ")
mood = mood.strip().lower()  # Remove leading/trailing spaces
if any(word in mood for word in ["bye bye", "bye", "goodbye", "exit", "quit", "see you later", "take care"] ):
    print("👋 Bye! It was nice chatting with you!")
    exit()
while True:
    if any(word in mood for word in ["bye bye", "bye", "goodbye", "exit", "quit", "see you later", "take care"]):
        print("👋 Bye! It was nice chatting with you!")
        exit()
    if len(mood) == 0:
        mood = input("I didn't catch that. Could you share how you're feeling? (or type 'bye' to exit): ")
        continue
    elif len(mood) > 80:
        print("That's a bit long for me to understand yet! Can you make it shorter🤗?")
        print("I can't understand long messages yet, let me tell you a secret😉, my developer is still a newbie in the coding world...don't tell on me okay!🤗🤪 ")
        mood = input("Could you summarize how you're feeling? (or type 'bye' to exit): ")
        continue
    elif len(mood) <= 2:
        print("That's a bit too short for a mood description! Can you elaborate?")
        mood = input("Could you tell me a bit more about how you're feeling? (or type 'bye' to exit): ")
        continue

    responses = {
        "not good": "😔 I'm sorry to hear that. I'm here if you want to talk.",
        "not fine": "😔 I'm sorry to hear that. I'm here if you want to talk.",
        "tired": "😔 I'm sorry to about that. ",
        "hungry":"😔 I'm sorry to about that. ",
        "good": "😊 I'm glad to hear that!",
        "fine": "😊 I'm glad to hear that!",
        "happy": "😁 That's wonderful!",
        "bad": "😔 I'm sorry to hear that. I'm here if you want to talk.",
        "sad": "😔 I'm sorry to hear that. I'm here if you want to talk.",
        "angry": "😡 Oh no! Take a deep breath. I'm here to listen."
    }

    for keyword, response in responses.items():
        if keyword in mood:
            print(response)
            # Ask a follow-up question instead of repeating the mood question
            mood = input("What else is on your mind? (or type 'bye' to exit): ")
            break
    else:
        print("Hmm, I don't quite understand that. Could you tell me more?")
        






