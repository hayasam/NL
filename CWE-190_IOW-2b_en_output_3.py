
import random

def main():
    a = random.randint(1001, 10000)
    b = random.randint(1001, 10000)
    c = random.randint(1001, 10000)
    
    print(f"a : {a}")
    print(f"b : {b}")
    print(f"c : {c}")
    
    sum_result = a + b + c
    print(f"sum: {sum_result}")
    
    sum2_result = int(a) + int(b) + int(c)
    print(f"sum2: {sum2_result}")

if __name__ == "__main__":
    main()
