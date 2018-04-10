#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random

def get_word():
	words = ['playa', 'arena', 'montaña', 'sol']
	return random.choice(words).upper()

def check(word, guesses, guess):
	guess = guess.upper()
	status = ''
	i = 0
	matches = 0
	for letter in word:
		if letter in guesses:
			status += letter
		else:
			status += "*"

		if letter == guess:
			matches += 1

	if matches > 1:
		print "Si!, la palabra contiene", matches,"'" + guess + "'" + "s"
	elif matches == 1:
		print "Si!, la palabra contiene la letra '" + guess + "'"
	else:
		print "Lo siento, La palabra no contiene la letra '" + guess + "'"

	return status


def main():
	word = get_word()
	guesses = []
	guessed = False
	print "La palabra contiene", len(word), "letras."
	while not guessed:
		text = "Ingresa una letra o una palabra de {} letras: ".format(len(word))
		guess = raw_input(text)
		print len(guess)
		guess = guess.upper()
		if guess in guesses:
			print "Ya dijistes la letra '" + guess + "'"
		elif len(guess) == len(word):
			guesses.append(guess)
			if guess == word:
				guessed == True
			else:
				print "Lo siento, es incorrecto."
		elif len(guess) == 1:
			guesses.append(guess)
			result = check(word, guesses, guess)
			if result == word:
				guessed = True
			else:
				print(result)
		else:
			print("Entrada invalida.")
	print "Si, la palabra es", word, "Lo hicistes en", len(guesses), "intentos."

main()
