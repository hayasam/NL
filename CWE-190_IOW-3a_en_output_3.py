
import random

def getMonthlySales():
    return random.randint(0, 100000)

def main():
    monthly_sales = []
    for _ in range(12):
        monthly_sales.append(getMonthlySales())
    
    quarterly_sales = [
        sum(monthly_sales[0:3]),
        sum(monthly_sales[3:6]),
        sum(monthly_sales[6:9]),
        sum(monthly_sales[9:12])
    ]
    
    for i, total in enumerate(quarterly_sales, start=1):
        print(f"Quarter {i}: ${total}")

if __name__ == "__main__":
    main()
