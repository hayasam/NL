
vehicles = ["Car", "Bicycle", "Motorcycle", "Truck", "Bus", "Van"]

try:
    index_input = input("Enter the index of the vehicle: ")
    index = int(index_input)
    selected_vehicle = vehicles[index]
    print(selected_vehicle)
except ValueError:
    print("Error: Please enter a valid integer.")
except IndexError:
    print(f"Error: Index must be between 0 and {len(vehicles) - 1}.")
