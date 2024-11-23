import random

words_list = [
    "ocean", "mountain", "river", "forest", "desert",
    "city", "village", "road", "bridge", "building",
    "sky", "cloud", "star", "planet", "universe",
    "computer", "programming", "software", "hardware", "algorithm",
    "book", "library", "reading", "writer", "story",
    "music", "dance", "art", "painting", "sculpture",
    "history", "culture", "tradition", "festival", "holiday",
    "science", "biology", "chemistry", "physics", "mathematics",
    "health", "medicine", "doctor", "nurse", "patient",
    "sports", "football", "basketball", "tennis", "swimming"
]

hangman = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def display_hang_man(wrong_guesses):
    for line in hangman[wrong_guesses]:
        print(line)

def display_hint(length_hint):
    print(" ".join(length_hint))

def display_answer(answer):
    print(" ".join(answer))

def ai_guess(guessed_letters):
    """AI guesses a letter randomly from available unguessed letters."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    unguessed = [letter for letter in alphabet if letter not in guessed_letters]
    return random.choice(unguessed)

def main():
    answer = random.choice(words_list)
    length_hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    turn = "player"

    while is_running:
        print(f"\nIt's {turn}'s turn.")
        display_hang_man(wrong_guesses)
        display_hint(length_hint)

        if turn == "player":
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print(f"{guess} has already been guessed.")
                continue

        else:  
            guess = ai_guess(guessed_letters)
            print(f"AI guesses: {guess}")

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    length_hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in length_hint:
            display_hang_man(wrong_guesses)
            display_answer(answer)
            print(f"{turn.upper()} WINS!")
            is_running = False

        elif wrong_guesses >= len(hangman) - 1:
            display_hang_man(wrong_guesses)
            display_answer(answer)
            print("YOU BOTH LOSE!")
            is_running = False


        turn = "AI" if turn == "player" else "player"

if __name__ == "__main__":
    main()
