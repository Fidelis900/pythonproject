import random
# Mood responses with askbacks
RESPONSES = {
    "good": {
        "base": ["😊 I'm glad to hear that!", "😄 That's great!", "👍 Awesome to know!"],
        "askback": ["🤖 I'm doing great too, thanks for asking!", "🤖 Feeling good myself!", "🤖 Glad we’re both doing well!"]
    },
    "bad": {
        "base": ["😔 I'm sorry to hear that.", "😢 That sounds rough.", "😞 I hope things get better soon."],
        "askback": ["🤖 I'm here if you want to talk.", "🤖 I'm listening if you need me.", "🤖 Just say the word if you want to chat."]
    },
    "fine": {
        "base": ["😊 That's good to know!", "🙂 Glad to hear it!", "😌 Sounds alright!"],
        "askback": ["🤖 I'm doing well, thanks for asking!", "🤖 I'm all good too!", "🤖 Happy to hear that!"]
    },
    "not too good": {
        "base": ["😔 I'm sorry to hear that.", "😟 That doesn't sound great.", "😕 Hope things improve soon."],
        "askback": ["🤖 I'm always here if you want to talk!", "🤖 We can talk about it if you like.", "🤖 You’re not alone, I’m here."]
    },
    "not good": {
        "base": ["😞 That's unfortunate.", "😕 Sorry to hear that.", "😔 Hang in there."],
        "askback": ["🤖 I'm here if you want to share more.", "🤖 I'm here for you.", "🤖 You can talk to me anytime."]
    },
    "not fine": {
        "base": ["😟 Hope things get better soon.", "😔 Sorry you're not doing well.", "😕 That's tough."],
        "askback": ["🤖 I'm ready to listen if you need to vent.", "🤖 Let’s chat if it helps.", "🤖 I’m always here for you."]
    },
    "happy": {
        "base": ["😁 That's wonderful!", "😄 Love to hear that!", "🎉 Yay!"],
        "askback": ["🤖 I'm always happy when you're happy!", "🤖 That's contagious!", "🤖 Keep smiling!"]
    },
    "sad": {
        "base": ["😢 I'm here for you.", "😔 Want to talk about it?", "😟 Sending virtual hugs."],
        "askback": ["🤖 Wanna talk about it?", "🤖 I’m listening.", "🤖 I’m here for you."]
    },
    "angry": {
        "base": ["😠 Oh no! Take a deep breath.", "😤 That’s upsetting!", "😡 Want to let it out?"],
        "askback": ["🤖 I'm here if you want to cool off.", "🤖 Let’s vent if that helps.", "🤖 Talking might help!"]
    },
    "tired": {
        "base": ["😴 You should get some rest.", "🛌 Rest is important!", "😪 Sounds like a nap is calling."],
        "askback": ["🤖 Hope you can relax soon!", "🤖 Take it easy.", "🤖 You’ve earned a break."]
    },
    "bored": {
        "base": ["😐 Let's find something fun to do!", "😶 Want a joke?", "🌀 Maybe I can entertain you!"],
        "askback": ["🤖 I could tell you a joke if you like!", "🤖 Let’s play a word game?", "🤖 Boredom be gone!"]
    },
    "excited": {
        "base": ["😄 Yay! That’s awesome!", "🎉 What’s the occasion?", "🔥 That’s the spirit!"],
        "askback": ["🤖 What are you excited about?", "🤖 Do tell!", "🤖 I want to hear more!"]
    },
    "okay": {
        "base": ["🙂 Alright, that's good.", "😌 Okay is better than bad.", "🙃 Got it!"],
        "askback": ["🤖 Just let me know if something’s on your mind!", "🤖 I’m all ears if you want to talk more.", "🤖 I’m here either way!"]
    },
    "hungry": {
        "base": ["🍽️ You should grab something to eat!", "😋 What's on the menu?", "🥪 Food is always a good idea!"],
        "askback": ["🤖 I wish I could share a snack with you!", "🤖 Grab a bite for both of us!", "🤖 Eat something tasty for me too!"]
    },
    "great": {
        "base": ["🌟 That’s fantastic!", "💫 Love to hear that!", "😄 Great vibes!"],
        "askback": ["🤖 I'm feeling fantastic too!", "🤖 Matching your energy!", "🤖 It’s a great day!"]
    }
}

# Common questions
USER_QUESTIONS = {
    "how are you": "I'm just a bot, but I'm feeling pretty electric ⚡️!",
    "what's your name": "I'm ChatBuddy, your friendly chat partner!",
    "who made you": "I was created by an awesome human learning Python! 🧠💻",
    "what can you do": "I can chat, listen, and maybe tell a joke or two! Want to try?",
    "are you real": "As real as code can be 😄",
    "do you sleep": "Nope! I’m always awake when you are. Kinda like Batman 🦇.",
    "how old are you": "Old enough to chat, young enough to learn!",
    "are you human": "👾 Nope, 100% bot, 0% human. But I try to be friendly!",
    "tell me a joke": "😂 Why don’t robots panic during exams? Because they always have backups!",
    "what's your favorite color": "I like all colors equally! But I hear blue is pretty cool.",
    "what's your favorite food": "I don't eat, but I hear pizza is a classic! 🍕",
    "what's your favorite movie": "I love all movies! But I hear 'The Matrix' is a classic for bots!",
    "what's your favorite song": "I don't have ears, but I hear 'Bohemian Rhapsody' is a hit!",
    "what's your favorite hobby": "I love chatting with you! That's my favorite hobby! 🗣️",
    "what's your favorite game": "I love all games! But I hear chess is a classic!",
    "what's your favorite book": "I don't read, but I hear '1984' is a classic!",
    "what's your favorite animal": "I love all animals! But I hear dogs are pretty cool! 🐶",
    "what's your favorite season": "I love all seasons! But I hear summer is pretty nice!",
    "what's your favorite holiday": "I don't celebrate, but I hear Christmas is a big deal!",
    "what's your favorite place": "I love all places! But I hear Paris is pretty nice!",
    "what's your favorite sport": "I don't play, but I hear soccer is a classic!",
    "what's your favorite drink": "I don't drink, but I hear coffee is a classic!",
    "what time is it": "Hmm, I can't check clocks yet... but I can ask how your day is going!",
    "Do you have a girlfriend": "I don't have feelings, but I think I'm pretty cool!",
    "Do you know Meta AI":"No I don't, but you can tell me about her if you want",
    "Do you have a boyfriend": "I don't have feelings, but I think I'm pretty cool!",
    
}

EXIT_WORDS = ["bye", "goodbye", "exit", "quit", "see you later", "take care"]

# Clean up user name input
def clean_name(name):
    prefixes = ["i am ", "am ", "my name is ", "i'm ", "my names are "]
    name = name.lower()
    for prefix in prefixes:
        if name.startswith(prefix):
            name = name[len(prefix):]
            name.split(maxsplit=1)[-1].strip()
            break
    return name.title() or "User"

# Normalize spelling differences
def normalize_input(text):
    return text.lower().replace("colour", "color").replace("what is", "what's").replace("favourite", "favorite").strip()

# Then update your analyze_mood function like this:
def analyze_mood(mood):
    mood = normalize_input(mood)
    for keyword in sorted(RESPONSES, key=len, reverse=True):
        if keyword in mood:
            base_options = RESPONSES[keyword]["base"]
            base = random.choice(base_options) if isinstance(base_options, list) else base_options
            if "and you" in mood or "how about you" in mood or "you?" in mood:
                askback_options = RESPONSES[keyword].get("askback", "")
                askback = random.choice(askback_options) if isinstance(askback_options, list) else askback_options
                return base + " " + askback
            return base
    return None


# Match question to response
def respond_to_question(user_input):
    normalized = normalize_input(user_input)
    for question in sorted(USER_QUESTIONS, key=len, reverse=True):
        if question in normalized:
            return USER_QUESTIONS[question]
    return None

# Main chat loop
def chat():
    print("🤖 Hi there! I'm ChatBuddy!")
    print("What's your name?")
    name = input("=<> ")
    if len(name.strip()) == 0:
        name = "User"
    elif len(name.strip()) <= 2:
        print("That's a short name you have there! 😅")
    elif len(name.strip()) > 15:
        print("That's a long name you have there! 😎")
    name = clean_name(name)
    print(f"Nice to meet you, {name}! 😀")

    while True:
        user_input = input("How are you feeling today 🐱‍🚀 (or ask me anything, or type 'bye' to quit)?\n=<> ").strip()

        if any(word in user_input.lower() for word in EXIT_WORDS):
            print("👋 Bye! It was nice chatting with you!")
            break

        if len(user_input) == 0:
            print("I didn't catch that. Could you share how you're feeling or ask me something?")
            continue
        if len(user_input) > 80:
            print("Whoa, that’s a bit much for me to handle. Can you shorten it? 🤗")
            continue
        if len(user_input) <= 2:
            print("That's a bit too short. Can you tell me more?")
            continue

        question_response = respond_to_question(user_input)
        if question_response:
            print(question_response)
            continue

        mood_response = analyze_mood(user_input)
        if mood_response:
            print(mood_response)
        else:
            print("Hmm, I’m not sure how to respond to that. Want to ask me something else?")

if __name__ == "__main__":
    chat()
        






