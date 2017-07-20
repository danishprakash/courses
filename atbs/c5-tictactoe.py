theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5':
        ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

def drawBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def checkWinner(turn):
    if theBoard['1'] == theBoard['2'] == theBoard['3'] == turn:
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] == turn:
        return True
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] == turn:
        return True
    elif theBoard['3'] == theBoard['5'] == theBoard['7'] == turn:
        return True

#drawBoard(theBoard)

turn = 'X'

for i in range(9):
    drawBoard(theBoard)
    move = raw_input('Enter the position to check  ' + turn + ' ')
    if move == 'exit':
        break

    if theBoard.get(move, 0) == ' ':
        theBoard[move] = turn
    else:
        print('That position is already used!')

    if checkWinner(turn):
        print('Player ' + turn + ' Won!')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

drawBoard(theBoard)
