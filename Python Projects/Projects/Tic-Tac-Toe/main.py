# tic-tac-toe
# by errol vogt 2023

def check(p, array):

    # checks rows
    for r in array:
        if all(x == p for x in r):
            return True

    # checks columns
    for i in range(3):
        column = [row[i] for row in array]
        if all(x == p for x in column):
            return True

    # checks diagonals
    if all(array[i][i] == p for i in range(3)):
        return True

    if all(array[i][2-i] == p for i in range(3)):
        return True

    return False


def print_board():
    # print board
    print(f'    1   2   3')
    print(f'  -------------')
    for n, row in enumerate(board):
        array_string = " | ".join(row)
        print(f'{n+1} | {array_string} |')
        print(f'  -------------')


# player board
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

print('Tic-Tac-Toe\n')

round_num = 0

playing = True
while playing:

    print_board()

    # get player number and cycle through

    if round_num % 2:
        player = "O"
    else:
        player = "X"

    try:
        choice = input(f'\nPlayer: {player}, enter a choice (xy): ')
        x = (int(choice[0]) - 1)
        y = (int(choice[1]) - 1)

        if board[x][y] == '_':
            board[x][y] = player
            round_num += 1

            if check(player, board):
                print_board()
                print(f'Wowe, Player {player}, wins!')
                playing = False

        elif board[x][y] == 'X' or 'O':
            raise ValueError(f"Cannot place there.")

    except ValueError:
        print('Invalid option/Cannot place.')





