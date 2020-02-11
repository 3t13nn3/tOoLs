#TO ADD: Copy to clipboard thing avoiding pyperclip

import sys

def data_recovery():
	text = []
	words = []
	if sys.argv[1] == "1":
		while True:
			try:
				line = input()
			except EOFError:
				break
			words.append(line + "\n")
		words[len(words)-1] = words[len(words)-1][:len(words[len(words)-1])-1]
	else:
		words = sys.argv[2:]
		for i in  range(len(words)):
			words[i] += " "

	for i in words:
		text.append(str(i))

	return text


def tRaNsFoRm(og_text):
	text = list("".join(og_text))
	for i in range(len(text)):
		if i & 0x01:
			text[i] = text[i].upper()
		else:
			text[i] = text[i].lower()

	return "".join(text)


if __name__ == "__main__":
	
	og_text = data_recovery()
	text    = tRaNsFoRm(og_text)

	print(text)