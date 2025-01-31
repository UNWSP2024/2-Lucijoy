# Author: Lucia Floan
# Date: Jan 31, 2025
# Title: Average Age
def average_age():
    # Get User Input
    age1 = int(input("Enter the age of the first friend: "))
    age2 = int(input("Enter the age of the second friend: "))          
    age3 = int(input("Enter the age of the third friend: "))
    age4 = int(input("Enter the age of the fourth friend: "))
    age5 = int(input("Enter the age of the fifth friend: "))           

    # Sum ages
    sum_of_ages = age1 + age2 + age3 + age4 + age5
               
    # Average the ages
    average = sum_of_ages / 5

    # Print the results
    print(f'The average is: {average:.2f}')

# Line which calls the above function.
average_age()
