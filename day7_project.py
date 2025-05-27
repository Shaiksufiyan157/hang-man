import random
# from word_list
import hungman_word
import hungman_art
print(r''''
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/                       ''')
stages=hungman_art.stages
logo=hungman_art.logo
word_list =  hungman_word.word_list

choosen_word=random.choice(word_list)
print(choosen_word)

for i in range(len(choosen_word)):
    print("_",end="")

lives=6

gameOver=False

correct_letters=[]

while not gameOver:
    guess = input("\nenter your guess").lower()

    if guess not in choosen_word:
        lives-=1
    print(f"****************************<{lives} >/LIVES LEFT****************************")
    print(stages[lives])
    if lives==0:
        print(f"the word is {choosen_word.upper()}")
        print("you lose!!, now man has been hung")
        break
    display = ''
    for letter in choosen_word:
        if guess == letter:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display += "_"
    print(display)

    if '_' not in display:
        gameOver=True
        print("You win!!, you saved the man to be hung")







