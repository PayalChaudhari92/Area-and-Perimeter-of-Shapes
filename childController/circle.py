import sys
sys.path.append("C:/Users/Payal Chaudhari/Desktop/Python new folder/Practise_folder/Practice_automation/baseController")

from baseClass import Base
class Circle(Base):
    def __init__(self,length):
        self.length= length

    def area(self):
        areaOfCircle= 3.14*(self.length*self.length)
        return areaOfCircle
    
    def perimeter(self):
        perimeterCircle=2*3.14*self.length
        return perimeterCircle