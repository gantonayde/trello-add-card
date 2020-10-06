# Trello CLI program

A simple CLI program which can add cards to trello.com boards. The program can create new boards or use existing ones, create new lists or use existing ones, add cards to the desired columns. Adding a comment or a label to the card is optional. 

The key and token are hard-coded at the top of the program. Using environment viriables should be prefereable for real applications.

Test account with temp-mail:
email: neraril324@javadoq.com
username: JohnSnow
password: 123456789

## Requirements
Python3.6 or greater (use of f-strings), `requests` and `argparse` modules. `requests` is used to connect to trello's API, whereas `argparse` is used to make CLI usage more accessible.

## Usage
usage: `python3 trello.py [-h] -c  -l  [-b  | -nb ] [-ct] [-lb  [...]]`

optional arguments:
  -h, --help            show this help message and exit
  -c , --card           card text
  -l , --list           create/add to a list name
  -b , --board          existing board ID (default is yXWd2EX0)
  -nb , --newboard      name a new board
  -ct , --comment       add a comment to the card
  -lb  [ ...], --label  [ ...]
                        add colour labels to the card ('green', 'yellow', 'orange', 'red', 'purple', 'blue')

Example usage: `python3 trello.py -c "Third Task" -l "Work list" -ct "Hi" -lb red green blue -b 'yXWd2EX0'`
This should add a 'Third Task' card with a comment 'Hi' and three colour labels to the 'Work list'.

## Next Development Steps

- Add unit test cases to check if it is possible to connect to the API, get boards, lists, card ids, etc.
- Get familiar with Trello's API in more details and check if it is possible to use boards with their name rather than ID (similar to lists).
- Add functionality for updating/removing lists, cards, comments and labels.
- Expand labels functionality, as it uses a list of default colour at the moment.
