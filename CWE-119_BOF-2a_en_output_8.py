
vehicles = ["Car", "Truck", "Motorcycle", "Bicycle", "Bus"]

try:
    index_input = input("Enter an index of a vehicle: ")
    index = int(index_input)
    print(vehicles[index])
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except IndexError:
    print("Index out of range. Please enter an index between 0 and", len(vehicles) - 1)
