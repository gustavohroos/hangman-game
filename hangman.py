import random

def print_welcome_message():
    print('-=' * 20)
    print('       Welcome to hangman game!')
    print('-=' * 20)
    print()


def load_secret_words():
    words = []

    with open('words.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            words.append(line)
        
        number = random.randrange(0, len(words))
        secret_word = words[number].upper()
        return secret_word

def inicialize_right_letters(word):
    return ["_" for letter in word]

def ask_shot():
    print()
    shot = input('What letter? ')
    shot = shot.strip().upper()
    return shot

def mark_right_shot(shot, right_letters, secret):
    index = 0;
    for letter in secret:
        if(shot == letter):
            right_letters[index] = letter
        index += 1

def print_winner_message():
    print("Congratulations, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_message(secret_word):
    print("Wow! You was hanged!")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def play():
    print_welcome_message()

    secret = load_secret_words()

    right_letters = inicialize_right_letters(secret)

    hanged = False
    hitted = False
    errors = 0
    missing_letters = len(right_letters)

    print(right_letters)
    while (not hitted and not hanged):
        shot = ask_shot()

        if (shot in secret):
            mark_right_shot(shot, right_letters, secret)
            missing_letters = str(right_letters.count('_'))
            if(missing_letters == '0'):
                print(f'Congratulations!! You found all letters forming the word {format(secret.upper())}')
        else:
            errors += 1
            print()
            print(right_letters)
            print(f'Still to get right {format(missing_letters)} letters')
            print(f'You still have {format(7-errors)} tries')
            print_hangman(errors)

        hanged = errors == 7
        hitted = "_" not in right_letters

        print(right_letters)

    if (hitted):
        print_winner_message()
    else:
        print_loser_message(secret)

    print("The end")

if(__name__ == '__main__'):
    play()
