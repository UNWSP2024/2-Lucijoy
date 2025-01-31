# Author: Lucia Floan
# Date: Jan 31, 2025
# Title: Total Purchase

def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    item1 = float(input("Enter the price of the first item"))
    item2 = float(input("Enter the price of the second item"))
    item3 = float(input("Enter the price of the third item"))
    item4 = float(input("Enter the price of the fourth item"))
    item5 = float(input("Enter the price of the fifth item"))
    
    # then displays the subtotal of the sale, 
    subtotal = item1 + item2 + item3 + item4 + item5
    
    # the amount of sales tax, and the total.  
    sales_tax = subtotal * 0.07
    
    # Assume the sales tax is 7 percent.
    total = subtotal + sales_tax

    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Sales Tax (7%): ${sales_tax:.2f}')
    print(f'Total: ${total:.2f}')

calculate_total_purchase()
