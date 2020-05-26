# board = [[6, 0, 9, 0, 4, 0, 0, 0, 1],
#          [7, 1, 0, 5, 0, 9, 6, 0, 0],
#          [0, 5, 0, 0, 0, 0, 0, 0, 0],
#          [2, 0, 7, 0, 8, 0, 0, 2, 4],
#          [0, 0, 0, 0, 6, 0, 0, 2, 4],
#          [0, 6, 0, 9, 0, 0, 0, 0, 8],
#          [0, 0, 8, 0, 0, 0, 3, 0, 0],
#          [0, 0, 0, 4, 0, 0, 0, 0, 7],
#          [0, 0, 0, 0, 5, 0, 0, 0, 0]]

# board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#          [6, 0, 0, 1, 9, 5, 0, 0, 0],
#          [0, 9, 8, 0, 0, 0, 0, 6, 0],
#          [8, 0, 0, 0, 6, 0, 0, 0, 3],
#          [4, 0, 0, 8, 0, 3, 0, 0, 1],
#          [7, 0, 0, 0, 2, 0, 0, 0, 6],
#          [0, 6, 0, 0, 0, 0, 2, 8, 0],
#          [0, 0, 0, 4, 1, 9, 0, 0, 5],
#          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board = [[6,0,0,0,0,0,0,4,0],
         [0,0,5,0,0,2,0,0,7],
         [7,2,9,0,0,0,0,0,3],
         [0,9,0,0,4,0,0,0,1],
         [0,0,0,0,6,0,0,0,0],
         [4,0,0,0,8,0,0,7,0],
         [3,0,0,0,0,0,1,6,5],
         [2,0,0,4,0,0,8,0,0],
         [0,5,0,0,0,0,0,0,4]]


def printBoard(board):
    for y in range(9):
        print(board[y])



def findZero(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return (y, x)
    # if there are no more 0s
    return None


def validMove(board, digit, pos):
    # check row
    for x in range(len(board[0])):
        if board[pos[0]][x] == digit and x != pos[1]:
            return False
    # check column
    for y in range(len(board)):
        if board[y][pos[1]] == digit and y != pos[0]:
            return False

    # check box (3x3)
    box_y = pos[0] // 3
    box_x = pos[1] // 3
    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if board[y][x] == digit and y != pos[0] and x != pos[1]:
                return False

    # "else"
    return True


def solve(board):
    pos = findZero(board)
    if not pos:
        return True
    else:
        y, x = pos

    for num in range(1, 10):
        if validMove(board, num, (y, x)):
            board[y][x] = num

            # R E C U R S I O N
            if solve(board) != False:
                return True
            # "else"
            board[y][x] = 0

    return False

def solve(board):
    pos = findZero(board)
    # G O A L -> there are no 0s
    if not pos:
        return True
    else:
        y, x = pos

    # C H O I C E -> (num)
    for num in range(1, 10):
        # C O N S T R A I N T -> is (validMove) ?
        if validMove(board, num, (y, x)):
            board[y][x] = num

            # R E C U R S I O N

            if solve(board) != False:
                return True
            # "else"
            board[y][x] = 0

    return False


printBoard(board)
solve(board)
print("")
printBoard(board)
