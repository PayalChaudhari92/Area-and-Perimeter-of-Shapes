import sys
sys.path.append("C:/Users/Payal Chaudhari/Desktop/Python new folder/Practise_folder/Practice_automation/baseController")

from baseClass import Base
class Square(Base):
        

        def __init__(self,length):
            self.length= length

        def area(self):
            areaOfSquare= self.length*self.length
            return areaOfSquare
    
        def perimeter(self):
            perimeterSquare=4*self.length
            return perimeterSquare
