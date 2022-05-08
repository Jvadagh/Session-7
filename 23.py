"""
23. We can represent a Tic-Tac-Toe board as a 3  3 grid in which each position can hold one of the
following three strings: "X", "O", or " ". Write a function named check_winner that accepts a
3  3 list as a parameter. If "X" appears in a winning Tic-Tac-Toe pattern, the function should return
the string "X". If "O" appears in a winning Tic-Tac-Toe pattern, the function should return the string
"O". If no winning pattern exists, the function should return the string " ".
"""

game = [['x', 'O', 'O'],
        ['x', 'O', 'O'],
        ['x', 'O', 'O']]

#for row in game:
    #print(row)


def check_winner(game):
    # satr
    if game[0][0] == game[0][1] and game[0][0] == game[0][2] and game[0][1] == game[0][2] and game[0][0] == 'x':
        result = 'x'
        return result
    if game[1][0] == game[1][1] and game[1][0] == game[1][2] and game[1][1] == game[1][2] and game[1][0] == 'x':
        result = 'x'
        return result
    if game[2][0] == game[2][1] and game[2][0] == game[2][2] and game[2][1] == game[0][2] and game[2][0] == 'x':
        result = 'x'
        return result
    # soton
    if game[0][0] == game[1][0] and game[1][0] == game[2][0] and game[0][0] == game[2][0] and game[0][0] == 'x':
        result = 'x'
        return result

    if game[0][1] == game[1][1] and game[1][1] == game[2][1] and game[0][1] == game[2][1] and game[0][1] == 'x':
        result = 'x'
        return result

    if game[0][2] == game[1][2] and game[1][2] == game[2][2] and game[0][2] == game[2][2] and game[0][2] == 'x':
        result = 'x'
        return result
    # ghotr
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] == game[2][2] and game[0][0] == 'x':
        result = 'x'
        return result
    if game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] == game[2][0] and game[0][2] == 'x':
        result = 'x'
        return result
    else:
        result = ' '
        return result


print(check_winner(game))
