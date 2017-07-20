#! python3

import pyperclip, re

clipboard = pyperclip.paste()

phoneNumbers = []
emails = []
matches = []

phoneNumRegex = re.compile(r'''
(\+?\d{3}|\(\d{3}\))?               #area code
(\s|-|\.)?                          #seperator - '.' or ' ' '-'
(\d{3})                             #mid 3 digits
(\s|-|\.)                           #seperator - '.' or ' ' '-'
(\d{4})                             #final four digits
''', re.VERBOSE)

emailRegex = re.compile(r'''(
([a-zA-Z0-9.%+-]+)                  #usernames
@                                   #@ symbol
([a-zA-Z0-9.-]+)                    #domain name
\.[a-zA-Z]+                         #.something
)''', re.VERBOSE)

for group in phoneNumRegex.findall(clipboard):
    phoneNumber = ('-').join([group[0], group [2], group[4]])
    matches.append(phoneNumber)

for group in emailRegex.findall(clipboard):
    matches.append(group[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No email addresses or phone numbers found')
