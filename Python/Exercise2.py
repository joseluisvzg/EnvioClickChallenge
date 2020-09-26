#!/usr/bin/env python

consec_vowel = {
	'a': 'e',
	'e': 'i',
	'i': 'o',
	'o': 'u',
	'u': 'a'
}

def vowels_changer(text):
	new_text = []
	for char in text.lower():
		if char in consec_vowel:
			char = consec_vowel[char]
		new_text.append(char)
	new_text = ''.join(new_text)
	return new_text

if __name__ == "__main__":
	text = input("Type a text: ")
	new_text = vowels_changer(text)
	print(f"New text: {new_text}")