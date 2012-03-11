import json
import sys

board = json.loads(sys.stdin.read())

# vertical
for y in range(3):
    for x in range(7):
        if board[y][x] == board[y+1][x] == board[y+2][x] == board[y+3][x] and board[y][x] in 'OX':
            print 'Winner: {0}'.format(board[y][x])
            sys.exit(0)

# horizontal
for y in range(6):
    for x in range(4):
        if board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3] and board[y][x] in 'OX':
            print 'Winner: {0}'.format(board[y][x])
            sys.exit(0)

# diagonal
for y in range(3):
    for x in range(4):
        if board[y][x] == board[y+1][x+1] == board[y+2][x+2] == board[y+3][x+3] and board[y][x] in 'OX':
            print 'Winner: {0}'.format(board[y][x])
            sys.exit(0)

# other diagonal
for y in range(3, 6):
    for x in range(4):
        if board[y][x] == board[y-1][x+1] == board[y-2][x+2] == board[y-3][x+3] and board[y][x] in 'OX':
            print 'Winner: {0}'.format(board[y][x])
            sys.exit(0)

print 'No winner'
