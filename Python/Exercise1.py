#!/usr/bin/env python

vowels = {
	'a','e','i','o','u'
}

def vowels_counter(text):
	counter = 0
	for char in text.lower():
		if char in vowels:
			counter += 1
	return counter

if __name__ == "__main__":
	text = input("Type a text: ")
	count = vowels_counter(text)
	print(f"There are {count} vowels on the text: {text}")