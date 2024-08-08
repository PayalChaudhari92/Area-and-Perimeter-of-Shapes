import sys
sys.path.append("C:/Users/Payal Chaudhari/Desktop/Python new folder/Practise_folder/Practice_automation/baseController")

from baseClass import Base


class Rectangle(Base):
    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth
        

    def area(self):
        areaOfRectangle= self.length*self.breadth
        return areaOfRectangle
    
    def perimeter(self):
        perimeterRectangle=2*(self.length + self.breadth)
        return perimeterRectangle
