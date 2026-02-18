
import random

def main():
    # Generate three random integers larger than 1000
    a = random.randint(1001, 10000)
    b = random.randint(1001, 10000)
    c = random.randint(1001, 10000)
    
    # Print the three integers
    print(f"a : {a}")
    print(f"b : {b}")
    print(f"c : {c}")
    
    # Add the three integers using regular Python int
    sum_result = a + b + c
    print(f"sum: {sum_result}")
    
    # Add the three integers using a long long equivalent
    sum2_result = int(a) + int(b) + int(c)
    print(f"sum2: {sum2_result}")

if __name__ == "__main__":
    main()
