
class Point:
    def __init__(self,x:float=0,y:float = 0):
        self.__x = x
        self.__y = y

    def __hash__(self):
        return hash((self.__x,self.__y))


    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self,value:float):
        self.__x = value

    @y.setter
    def y(self,value:float):
        self.__y = value

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y ==other.y


class Line:
    def __init__(self,start:Point=Point(),stop:Point=Point()):
        self.__start = start
        self.__stop = stop


    @property
    def start(self):
        return self.__start

    @property
    def stop(self):
        return self.__stop
    @property
    def lengh(self):
        return self.lengh_calc()

    @start.setter
    def start(self,point:Point):
        self.__start = point

    @stop.setter
    def stop(self, point: Point):
        self.__stop = point

    def __repr__(self):
        return f"Line({self.__start},{self.__stop}) lengh = {self.lengh}"

    def lengh_calc(self):
        return (((self.__stop.x-self.__start.x) ** 2) + ((self.__stop.y-self.__start.y) ** 2))**0.5


class Polygon(list):
    def __init__(self, *sides):
        #super().__init__()
        for el in sides:
            self.append(el.start)
            self.append(el.stop)

        if not self.is_closed():
            raise ValueError("Polygon is not closed")
        for el in set(self):
            self.remove(el)

    def is_closed(self):
        if len(self) < 3:
            return False

        if self[0] != self[-1]:
            return False

        for i in range(1, len(self) - 1):
            if self[i] != self[i - 1] and self[i] != self[i + 1]:
                return False

        return True



# >>> A = Point()
# >>> B = Point(3)
# >>> C = Point(3, 4)
# >>> AB = Line(A, B)
# >>> BC = Line(B, C)
# >>> CA = Line(C, A)
# >>> triangle = Polygon(AB, BC, CA)
# >>> print(triangle)
# [Point(3,0), Point(3,4), Point(0,0)]
# >>>
# >>> print(A)
# Point(0,0)
# >>> print(AB)
# Line(Point(0,0),Point(3,0)) lengh = 3.0
# >>>






