
vehicles = ["Car", "Motorcycle", "Truck", "Bicycle", "Bus", "Van"]

try:
    index_input = input("Enter an index of a vehicle: ")
    index = int(index_input)
    vehicle = vehicles[index]
    print(vehicle)
except ValueError:
    print("Error: Please enter a valid integer.")
except IndexError:
    print(f"Error: Index must be between 0 and {len(vehicles) - 1}.")
