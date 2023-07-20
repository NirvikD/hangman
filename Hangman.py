import random


def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()




words = get_list_of_words('/usr/share/dict/words')
#print(words)

random_word = random.choice(words)

print("Welcome to word guessing game")
lives = len(random_word)
print(f"You have {lives} lives")
display =[]
for l in range(len(random_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter")
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
            print(display)
    if guessed_letter not in random_word:
        lives-=1
        print(f"YOU HAVE {lives} LIVES LEFT")



    if lives==0:
            game_over=True
            print("You loose")
            print(f"The correct word was {random_word}")
    if '_' not in display:
        print("You win")
        game_over=True





















