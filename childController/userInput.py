from rectangle import Rectangle
from sides import GetSideLength
objGetSides=GetSideLength()
from square import Square
from circle import Circle

objGetSides=GetSideLength()
class UserInputCheck:
    def userInput(self, choice,formula):
        while choice == 1:
            length=objGetSides.length()
            breadth=objGetSides.breadth()
            objRectangle= Rectangle(length,breadth)

            if choice == 1 and formula == 1:
                print(objRectangle.area())
                break
            elif choice == 1 and formula == 2:
                print(objRectangle.perimeter())
                break
          

        while choice == 2:
            length=objGetSides.length()
            objSquare= Square(length)

            if choice == 2 and formula == 1:
                print(objSquare.area())
                break
            elif choice == 2 and formula == 2:
                print(objSquare.perimeter())
                break

        while choice == 3:
            length=objGetSides.length()
            objCircle= Circle(length)

            if choice == 3 and formula == 1:
                print(objCircle.area())
                break
            elif choice == 3 and formula == 2:
                print(objCircle.perimeter())
                break       
