import random
import hangman_art
import hangman_words

def play_hangman():
    logo = hangman_art.logo
    stages = hangman_art.stages
    word_list = hangman_words.word_list
    correct_word = random.choice(word_list)
    guessed_letters = ["_" for letter in correct_word]
    current_guessed_letters = 0
    player_lives = 6
    is_inputed = False

    print(logo)

    while "_" in guessed_letters and player_lives > 0:

        try: 
            answer = input("Guess a letter: ")[0].lower()
        except IndexError:
            answer = input("You have't type in your letter: ")[0].lower()

        current_guessed_letters = guessed_letters.count("_")

        for i in range(len(correct_word)):
            if answer == correct_word[i] and guessed_letters[i] == "_" and not is_inputed:
                guessed_letters[i] = answer
                is_inputed = True
                print("Correct!")
        is_inputed = False

        if current_guessed_letters == guessed_letters.count("_"):
            player_lives -= 1
            
            if answer in correct_word:
                print("Wrong..You've already guessed it.")
            else:
                print(f"Wrong... {answer} is not in the word.")
            
        print(guessed_letters)
        print(stages[player_lives])

    if player_lives > 0:
        print(f"Congratulation!!! You correctly guess the word {correct_word}")
    else:
        print("You died by hang...")

    replay = input("Type 'y' to try again: ").lower()

    if replay == 'y':
        play_hangman()
    else:
        print("Thank you for playing.")

play_hangman()