from typing import Optional


class Player:
    def __int__(self, name: str, marker: str):
        self.name = name
        self.marker = marker


class Board:
    def __init__(self):
        self.size = None
        self.diagCounts = None
        self.colCounts = None
        self.rowCounts = None
        self.board = None

    def __int__(self, size: int):
        self.reset(size)

    def reset(self, size: int):
        self.board = [['' for x in range(size)].copy() for y in range(size)]
        self.rowCounts = {}
        self.colCounts = {}
        self.diagCounts = {}
        self.size = size

    def place(self, player: Player, x: int, y: int) -> Optional[bool]:
        marker = player.marker

        if self.board[x][y] != '':
            raise ValueError
        else:
            self.board[x][y] = marker

            self.rowCounts[y] = self.rowCounts.get(y, {})
            self.rowCounts[y][marker] = self.rowCounts[y].get(marker, 0) + 1

            if self.rowCounts[y][marker] == self.size:
                return True

            self.colCounts[x] = self.colCounts.get(x, {})
            self.colCounts[x][marker] = self.colCounts[x].get(marker, 0) + 1

            if self.colCounts[x][marker] == self.size:
                return True

            if x == y:
                self.diagCounts["forward"] = self.diagCounts.get("forward", {})
                self.diagCounts["forward"][marker] = self.diagCounts["forward"].get(marker, 0) + 1

                if self.diagCounts["forward"][marker] == self.size:
                    return True

            if x + y == self.size - 1:
                self.diagCounts["backward"] = self.diagCounts.get("backward", {})
                self.diagCounts["backward"][marker] = self.diagCounts["backward"].get(marker, 0) + 1

                if self.diagCounts["backward"][marker] == self.size:
                    return True

            return True


class Game:
    def __int__(self, player1: Player, player2: Player, board: Board):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def plaGame(self):
        currTurn = 1
        gameDone = False

        while not gameDone:
            currPlayer = self.player1 if currTurn % 2 == 1 else self.player2
            x = int(input("write x position of marker"))
            y = int(input("write y position of marker"))
            if self.board.place(currPlayer, x, y):
                gameDone = True
                print(f"{currPlayer.name} wins!")
            else:
                currTurn += 1
