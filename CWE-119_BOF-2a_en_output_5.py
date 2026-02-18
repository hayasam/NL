
vehicles = ["Car", "Motorcycle", "Truck", "Bicycle", "Bus", "Van"]

try:
    index_input = input("Enter the index of a vehicle: ")
    index = int(index_input)
    selected_vehicle = vehicles[index]
    print(selected_vehicle)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except IndexError:
    print(f"Index out of range. Please enter a number between 0 and {len(vehicles)-1}.")
