class Selection:
    def selectOption(self):
        while True:
            try:
                option= int(input("Enter the option you want: "))
            except ValueError:
                print("Enter valid number.")
                continue

            if option in (1,2):
                pass
            else:
                print(" Please enter valid option")
            return option

    