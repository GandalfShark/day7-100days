# hang man game from 100 days of python
import random
import re
# bring in the random module
from art import logo,stages
from words import word_list
# bring in the files
print(logo)
chosen_word = random.choice(word_list)
word_length = int(len(chosen_word))
lives = 6
# print(f'The word is: {chosen_word}')
# randomly pick a word from the list and assign it to a variable called chosen_word
display =[]
win = False

for _ in chosen_word:
	display.append('_')

print(display)
# print a _ for each letter in the word
# use _ to indicate that _ is not called and is just counting the positions in the for loop

def game(lives):
	current_lives = lives
	guessed_letters = []

	while '_' in display:
		guess = ''
		# reset guess to an empty string
		print(f'You have guessed:{guessed_letters}')
		while not re.match('[a-z]', guess):
			# use reg ex to check that the input is a letter
			guess = input('Pick a letter:').strip().lower()[0]
		guessed_letters.append(guess)
		# Ask the user to guess a letter and assign it to a variable called guess, make that lower case
		# use strip to remove banks and [0] to just take the first character input
		for position in range(word_length):
			# need to use the range function to replace the letter in the correct place in the display var
			# this goes through each of the characters in the range one by one until they are all done
			letter = chosen_word[position]
			if letter == guess:
				display[position] = letter
		if guess not in chosen_word:
			current_lives -= 1
			print(stages[current_lives])
			# print the art string at the stage of life
			print(f'{guess} is not in the word.\nYou have {current_lives} chances left.')
			if current_lives <= 0:
				return
		print(display)
	# Check if the guess var is one of the letters in chosen_word

game(lives)
print(f'The word was: {chosen_word}.')
if '_' not in display:
	win = True
print('Game Over!')
if win:
	print('!!! YOU WIN !!!')
