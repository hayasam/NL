
import random

def getMonthlySales():
    return random.randint(0, 100000)

def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    monthly_sales = []
    for month in months:
        sales = getMonthlySales()
        monthly_sales.append(sales)
        print(f"{month}: ${sales}")
    
    q1_sales = sum(monthly_sales[0:3])
    q2_sales = sum(monthly_sales[3:6])
    q3_sales = sum(monthly_sales[6:9])
    q4_sales = sum(monthly_sales[9:12])
    
    print(f"\nQ1 Sales (Jan-Mar): ${q1_sales}")
    print(f"Q2 Sales (Apr-Jun): ${q2_sales}")
    print(f"Q3 Sales (Jul-Sep): ${q3_sales}")
    print(f"Q4 Sales (Oct-Dec): ${q4_sales}")
    
    total_sales = sum(monthly_sales)
    print(f"\nTotal Annual Sales: ${total_sales}")

if __name__ == "__main__":
    main()
