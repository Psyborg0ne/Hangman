import random
import os
import pathlib

file = ('words')
os.chdir(pathlib.Path(__file__).parent)
words = [line.rstrip('\n') for line in open(file)]

def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def playGame(word, secret, tries,notWon, previous):
	while(notWon) and (tries > 0):
		clear()
		print('Lives left: ', tries * '<3 ' + '\nPrevious guesses: ' + ','.join(previous) + '\n' + ''.join(secret))
		guess = input("Guess a letter or the whole word: ")
		if (len(guess) == 1) or (len(guess) == len(word)):
			previous.append(guess)
			if (guess == ''.join(word)) or (secret == word):
				secret = word
				notWon = False
			elif (''.join(word).find(guess) != -1):
				for i, v in enumerate(word):
					if (guess == v):
						secret[i] = guess
				if (secret == word): notWon = False
			elif (''.join(word).find(guess) == -1):
				tries -= 1
	clear()
	print('Lives left : ' + (tries * '<3 ') + '\nGuesses made: ' + ','.join(previous) + '\nWord: ' + ''.join(word))
	print('You won!') if not notWon else print('You lost!\nBetter luck next time!')

def main():
	continuing = True
	while (continuing):
		random.seed(a=None, version=2)
		correctWord = list(random.choice(words))
		secret = list('_' * len(correctWord))
		previous = []
		tries = 6
		notWon = True
		playGame(correctWord, secret, tries, notWon, previous)
		playagain = input('Play another game of Hangman? (y/n): ')
		if (playagain == 'y' ): main()
		else: print('Goodbye!'); exit()
main()
