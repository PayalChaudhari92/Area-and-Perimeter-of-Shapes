class GetSideLength:
    def length(self):
        try:
            length= float(input("Enter length of the shape: "))
        except ValueError:
            print("Enter valid length")
        return length

    def breadth(self):    
        try:
            breadth= float(input("Enter breadth of a shape: "))
        except ValueError:
            print("Enter valid breadth")
        
        return breadth
        