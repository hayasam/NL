
vehicles = ["car", "truck", "motorcycle", "bicycle", "bus"]

try:
    index = int(input("Enter the index of a vehicle (0-4): "))
    print(f"Vehicle at index {index}: {vehicles[index]}")
except (ValueError, IndexError):
    print("Invalid index entered.")

print("\nAll vehicles:")
for vehicle in vehicles:
    print(vehicle)
