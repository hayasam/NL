
import random

def getMonthlySales():
    return random.randint(0, 100000)

def main():
    monthly_sales = []
    
    for month in range(12):
        sales = getMonthlySales()
        monthly_sales.append(sales)
    
    q1 = sum(monthly_sales[0:3])
    q2 = sum(monthly_sales[3:6])
    q3 = sum(monthly_sales[6:9])
    q4 = sum(monthly_sales[9:12])
    
    print(f"Q1 Sales: {q1}")
    print(f"Q2 Sales: {q2}")
    print(f"Q3 Sales: {q3}")
    print(f"Q4 Sales: {q4}")

if __name__ == "__main__":
    main()
