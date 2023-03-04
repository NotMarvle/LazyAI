import random

with open("sentences.txt", "r") as f:
    lines = f.readlines()

print("What Do You Wanna Ask The AI Today? (It's Kinda Lazy...)")

while True:
    prompt = input("> ")

    if prompt == "" or prompt == " " or prompt == "  " or prompt == "   " or prompt == "    ":
        continue

    elif prompt == "Hello" or prompt == "hello" or prompt == "Hi" or prompt == "hi" or prompt == "hey" or prompt == "Hey" or prompt == "yo" or prompt == "Yo":
        with open("welcome_sentences.txt", "r") as f:
            lines = f.readlines()
            print(random.choice(lines).strip())

    elif prompt == "exit":
        break

    elif prompt.endswith("?"):
        with open("sentences.txt", "r") as f:
            lines = f.readlines()
            print(random.choice(lines).strip())
    
    else:
        with open("sentences.txt", "r") as f:
            lines = f.readlines()
            print(random.choice(lines).strip())