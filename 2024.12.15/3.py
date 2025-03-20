class ChessKing:
    files = {chr(ord('a')+el-1):el for el in range(1,9)}
    ranks = {str(el): el for el in range(1, 9)}

    def is_on_field(self,place:str):
        if place[0] in self.files.keys() and place[1] in self.ranks.keys():
            return True
        return False
    def __init__(self,color: str = 'white', square: str = None):
        self.color = color
        if color in ('black','white'):
            self.color = color
        else: self.color = 'white'
        if square is not None and self.is_on_field(square):
            self.square = square
        elif self.color == 'white':
            self.square = "e1"
        elif self.color == 'black':
            self.square = "e8"

    def turn(self,new_place):
        if self.is_turn_valid(new_place):
            self.square = new_place
        else: raise TypeError
    def is_turn_valid(self,new_place:str):
        if abs(self.files[self.square[0]]-self.files[new_place[0]])>1:return False
        if abs(self.ranks[self.square[1]] - self.ranks[new_place[1]]) > 1: return False

        if new_place == self.square: return False
        if not self.is_on_field(new_place): return False
        return True



    def __repr__(self):
        return f"{'W' if self.color == 'white' else 'B'}K: {self.square}"
    def __str__(self):
        return self.__repr__()



# >>> wk = ChessKing()
# >>> print(wk.color)
# white
# >>> print(wk.square)
# e1
# >>> wk.turn('e2')
# >>> print(wk)
# WK: e2
# >>> bk = ChessKing("black")
# >>> print(bk)
# BK: e8
# >>> bk.turn('e7')
# >>> print(bk)
# BK: e7
# >>> wk.turn('d4')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "D:\top academy\Data science\Homework\2024.12.15\3.py", line 24, in turn
#     else: raise TypeError
#           ^^^^^^^^^^^^^^^
# TypeError
# >>> bk.files == wk.files
# True
# >>> bk.ranks == wk.ranks
# True
