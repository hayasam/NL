
vehicles = ["car", "truck", "motorcycle", "bicycle", "bus"]

try:
    index = int(input("Enter the index of the vehicle (0-4): "))
    print(f"Vehicle at index {index}: {vehicles[index]}")
except (ValueError, IndexError):
    print("Invalid input or index out of range.")

print("\nAll vehicles:")
for vehicle in vehicles:
    print(vehicle)
