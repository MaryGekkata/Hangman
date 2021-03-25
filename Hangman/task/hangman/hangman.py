# Write your code here
import random

print('''H A N G M A N''')

consent = input('Type "play" to play the game, "exit" to quit: ')

while consent != "play" and consent != "exit":
    consent = input('Type "play" to play the game, "exit" to quit: ')

if consent == "play":
    word_list = ['python', 'java', 'kotlin', 'javascript']
    key_word = random.choice(word_list)
    print('\n')
    print(f"{'-'*len(key_word)}")

    user_letters_set = set()
    count = 0

    def check_count():
        if count == 8:
            print('You lost!')
        else:
            print('\n')

    def letters_check(user_letters_set, count):
        while count < 8:
            global temp_word
            low = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            user_letter = input('Input a letter: ')
            temp_word = []
            if user_letter in key_word and user_letter not in user_letters_set:
                user_letters_set.add(user_letter)
                for i in key_word:
                    temp_word += (i if i in user_letters_set else '-')
                print('\n')
                print(''.join(temp_word))
                if '-' not in temp_word:
                    print('You survived!')
                    break

            elif len(user_letter) != 1:
                print("You should input a single letter")

                check_count()
                for i in key_word:
                    temp_word += (i if i in user_letters_set else '-')
                print(''.join(temp_word))

            elif user_letter not in low:
                print("Please enter a lowercase English letter")

                check_count()
                for i in key_word:
                    temp_word += (i if i in user_letters_set else '-')
                print(''.join(temp_word))

            elif user_letter in user_letters_set:
                print("You've already guessed this letter")

                check_count()
                for i in key_word:
                    temp_word += (i if i in user_letters_set else '-')
                print(''.join(temp_word))

            else:
                print('''That letter doesn't appear in the word''')
                count += 1
                user_letters_set.add(user_letter)
                if count != 8:
                    print('\n')
                    for i in key_word:
                        temp_word += (i if i in user_letters_set else '-')
                    print(''.join(temp_word))

        else:
            print('You lost!')

    letters_check(user_letters_set, count)
