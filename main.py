import random
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

styles = [
    "Rap",
    "Love Song",
    "Breakup Song",
    "Angry Metal Song",
    "Sad Country Ballad"
]


def print_intro():
    print("\n🎤 Welcome to the AI Food Song Generator 🎤\n")
    time.sleep(1.5)

    print("Loading musical nonsense", end="", flush=True)
    for _ in range(3):
        time.sleep(0.75)
        print(".", end="", flush=True)
    print()

    time.sleep(1.5)
    print("Get ready for hilarious, sarcastic songs about your favorite dishes!\n")
    time.sleep(1.5)


def get_user_dish():
    return input("Name a dish you love (or hate): (type 'exit' to quit)\n> ")


def choose_style():
    print(
        "Choose a style:\n"
        "1. Rap\n"
        "2. Love Song\n"
        "3. Breakup Song\n"
        "4. Angry Metal Song\n"
        "5. Sad Country Ballad\n"
        "6. Random style"
    )

    try:
        style_choice = int(input("\nEnter the number of your style choice:\n> "))
    except ValueError:
        style_choice = 6

    if style_choice == 1:
        return "Rap"
    elif style_choice == 2:
        return "Love Song"
    elif style_choice == 3:
        return "Breakup Song"
    elif style_choice == 4:
        return "Angry Metal Song"
    elif style_choice == 5:
        return "Sad Country Ballad"
    else:
        style = random.choice(styles)
        print(f"\n🎲 Randomly chosen style: {style}\n")
        return style


def generate_prompt(dish, style):
    return (
        f"You are a witty songwriter and your task is to write a short, funny, sarcastic "
        f"{style} about {dish}. Make it sound ridiculous but catchy."
    )


def generate_song(prompt):
    messages = [
        {
            "role": "system",
            "content": "You are a hilarious, sarcastic, slightly chaotic songwriter specializing in food-themed songs."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content


def main():
    print_intro()

    while True:
        dish = get_user_dish()

        if dish.lower() == "exit":
            print("\nGoodbye, you crazy chef! 👋")
            break

        style = choose_style()
        prompt = generate_prompt(dish, style)

        try:
            song = generate_song(prompt)
            print(f"\n🎵 Here is your {style.lower()} about {dish}: 🎵\n\n{song}\n")
        except Exception as e:
            print(f"\nOops! Something went wrong: {e}\n")


if __name__ == "__main__":
    main()
