#!python3
#Bullet pointer adder for wiki editing - uses a string containing new line chars and return a string with bullet points(*) before each new line to the clipboard.

import pyperclip
text = pyperclip.paste()

text = text.split('\n')

for i in range(len(text)):
	text[i] = '* ' + text[i]

text = '\n'.join(text)
pyperclip.copy(text)
