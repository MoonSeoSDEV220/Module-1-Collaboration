# Module 3 Lab - Case Study: lists, Functions, and classes
# Name: Moon Seo
# Purpose: creating Python app that could utilize the user input and 
# organize into a format that is easy-to-read.




class Vehicle: #Super class called Vehicle. contains an attribute for vehicle type.
    def __init__(self, vehicle_type: str) -> None:
        valid_types = ['car', 'truck', 'plane', 'boat', 'broomstick']
        if vehicle_type not in valid_types:
            print("Invalid vehicle type.")
            vehicle_type = "car"
        self.vehicle_type = vehicle_type

    def __str__(self):
        return self.vehicle_type

class Automobile(Vehicle): #Class for Automobile which inherits the attributes from vehicle.
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")

        while doors not in [2, 4]: #While loop for validation check.
            print("Invalid input. Please choose between 2 or 4.")
            doors = int(input("Enter the number of doors (2 or 4): "))

        while roof not in ["solid", "sun roof"]:
            print("Invalid input. Please choose between solid or sun roof.")
            roof = input("Choose between solid or sun roof: ").lower()

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return (
            f"Vehicle Type: {super().__str__()}\n"
            f"Year: {self.year}\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Number of doors: {self.doors}\n"
            f"Type of roof: {self.roof}"
        )

year = int(input("Enter the year: "))
make = input("Enter the make: ")
model = input("Enter the model: ")

while True:
    try:
        doors = int(input("Enter the number of doors (2 or 4): "))
        if doors in [2, 4]:
            break
        else:
            print("Invalid input. Please enter either 2 or 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    roof = input("Enter the type of roof (solid or sun roof): ").lower()
    if roof in ["solid", "sun roof"]:
        break
    else:
        print("Invalid input.")

car = Automobile(year, make, model, doors, roof)
print(car)