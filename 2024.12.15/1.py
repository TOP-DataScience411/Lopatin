import math
class Tetrahedron :
    def __init__(self,edge: float):
        self.edge = edge

    def surface(self) -> float:
        return self.edge**2 * math.sqrt(3)
    def volume(self) -> float:
        return (self.edge**3)*math.sqrt(2)/12

# >>> one = Tetrahedron(10)
# >>> one.surface()
# 173.20508075688772
# >>> one.volume()
# 117.85113019775793
# >>> one.edge
# 10