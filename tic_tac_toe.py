import tic_ml

#player = 'o' comp = 'x'
board = [' ' for x in range(10)]

def counter(le, bo):
    x = len(bo)
    count = 0
    for i in range(x):
        if le == bo[i]:
            count += 1

    return count


def printBoard(board):
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("-----------")
    print(f" {board[7]} | {board[8]} | {board[9]}")


def won(bo, le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def insertLetter(pos, le):
    board[pos] = le


def SpaceIsFree(pos):
    return board[pos] == ' '


def isBoardFull(bo):
    if counter(' ', bo) > 1:
        return False
    return True


def playerMove():
    while True:
        move = input("Please select a position to place an \'o\' (1-9) :")

        try:
            move = int(move)
            if move >= 1 or move <= 9:
                if SpaceIsFree(move):
                    insertLetter(move, 'o')
                    break
                else:
                    print("Please inster a number in a free sapce")
            else:
                print("Please insert number within the range")
        except:
            print("Please inster a number")


def comp():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['x', 'o']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if won(boardCopy, let):
                move = i
                return move

    #middle move
    if SpaceIsFree(5):
        move = 5
        return move

    #corner move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if  len(cornersOpen) == 1:
        move = cornersOpen[0]

    if len(cornersOpen) > 1:
        move = randomPick(cornersOpen)

    #edge move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) == 1:
        move = edgesOpen[0]

    if len(edgesOpen) > 1:
        move = randomPick(edgesOpen)

    return move


def randomPick(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def main():
    input("Welcome to tic tac toe, press any key to continue :")
    while not isBoardFull(board):
        if not won(board, 'o'):
            move = comp()
            if move == 0:
                if not isBoardFull(board):
                    print("oops something went wrong")
                    break
            else:
                insertLetter(move, 'x')
                print(f"computer played at {move}")
                printBoard(board)

        else:
            print("Good Job, You Won")
            break

        if not won(board, 'x'):
        #     move = comp()
        #     if move == 0:
        #         if not isBoardFull(board):
        #             print("oops something went wrong")
        #             break
        #     else:
        #         insertLetter(move, 'o')
        #         print(f"computer played at {move}")
        #         printBoard(board)

        #comment the line below and uncomment the line above for ai vs ai
            playerMove()

        else:
            print("-_- sorry computer won this time")
            break



main()
while True:
    answer = input("Do you want to play again (yes/no) :")
    if answer.lower() == "y" or answer.lower() == "yes":
        board = [' ' for i in range(10)]
        print('-----------------------------------')
        main()

    else: break
