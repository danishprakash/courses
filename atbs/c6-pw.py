#! python3
# pw.py a script for storing passwords

PASSWORDS = {'zucker': '34rly', 
			 'email' : 'l4t3',
			 'luggage': '0n3'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Enter the correct format for usage')
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('The password for' + account + 'has been copied to your clipboard')
else:
	print('There is no such account in the db')
