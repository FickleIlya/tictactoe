import random


def check_board(board: list):
    coords = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '-':
                coords.append((i, j))

    if coords:
        return coords
    else:
        return False


def win_check(board: list, x_o: str, k: int, place: tuple) -> bool:

    row, col = place
    field = board[:]

    # print history of moves
    print('Place:', place)
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end='')
        print('\n', end='')
    print('\n')

    for way in range(3):

        # checking in column!
        if way == 0:
            cnt = 1

            for i in range(2):

                for d in range(1, k):

                    if i == 0:
                        r1 = row + d

                        if 0 <= r1 < len(field) and field[r1][col] == x_o:
                            cnt += 1
                            if cnt == k:
                                return True
                        else:
                            break

                    if i == 1:

                        r2 = row - d

                        if 0 <= r2 < len(field) and field[r2][col] == x_o:
                            cnt += 1
                            if cnt == k:
                                return True
                        else:
                            break

        # checking in row!
        elif way == 1:

            cnt = 1
            for i in range(2):
                for d in range(1, k):
                    if i == 0:

                        c1 = col + d

                        if 0 <= c1 < len(field[0]) and field[row][c1] == x_o:
                            cnt += 1
                            if cnt == k:
                                return True
                        else:
                            break

                    if i == 1:
                        c2 = col - d

                        if 0 <= c2 < len(field[0]) and field[row][c2] == x_o:
                            cnt += 1

                            if cnt == k:
                                return True
                        else:
                            break
        # checking diagonally
        elif way == 2:

            for i in range(2):
                # diagonally form left top to right down
                if i == 0:
                    cnt = 1

                    for j in range(2):

                        for d in range(1, k):

                            if j == 0:

                                r1 = row + d
                                c1 = col + d

                                if 0 <= r1 < len(field) and 0 <= c1 < len(field[0]) and field[r1][c1] == x_o:

                                    cnt += 1

                                    if cnt == k:
                                        return True
                                else:
                                    break

                            elif j == 1:

                                r2 = row - d
                                c2 = col - d

                                if 0 <= r2 < len(field) and 0 <= c2 < len(field[0]) and field[r2][c2] == x_o:
                                    cnt += 1

                                    if cnt == k:
                                        return True
                                else:
                                    break
                # diagonally form right top to left down
                elif i == 1:
                    cnt = 1

                    for j in range(2):

                        for d in range(1, k):

                            if j == 0:

                                r1 = row - d
                                c1 = col + d

                                if 0 <= r1 < len(field) and 0 <= c1 < len(field[0]) and field[r1][c1] == x_o:
                                    cnt += 1

                                    if cnt == k:
                                        return True
                                else:
                                    break

                            elif j == 1:

                                r2 = row + d
                                c2 = col - d

                                if 0 <= r2 < len(field) and 0 <= c2 < len(field[0]) and field[r2][c2] == x_o:
                                    cnt += 1

                                    if cnt == k:
                                        return True
                                else:
                                    break


def game(board: list, k: int):

    win = None
    cnt = 0

    while not win:

        for turn in ['X', 'O']:

            if coords := check_board(board=board):

                spot = random.choice(coords)
                row, col = spot
                board[row][col] = turn
                cnt += 1

                if cnt >= 5 and win_check(board=board, x_o=turn, k=k, place=spot) and cnt >= 5:
                    win = f'Winner: {turn}'
                    break
            else:
                win = 'Draw'

    # print the results
    print(win)
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end='')
        print('\n', end='')


def main():
    # set size of map n - column, m - raw
    n, m = map(int, input('Set size of map: ').split())
    k = int(input('Set number of X/O to win: '))

    while k > n and m:
        print('Number should be less or equal num of columns and rows!')
        k = int(input('Set number of X/O to win: '))

    # board starts with coordinates (0,0)
    board = [['-' for i in range(n)] for j in range(m)]

    game(board, k)


if __name__ == '__main__':
    main()

