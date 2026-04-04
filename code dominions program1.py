#Data collection 

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
points = int(input("Enter your points: "))

current_year = 2025

#Data Cleaning
#Arithmetic operations

age = current_year - birth_year
id_number = len(name)
future_points = points ** 2              
if id_number % 2 == 0:
    status = "EVEN"
else:
    status = "ODD"

#System Output

print("\n--- MEMBER PROFILE ---")
print(f"Name:\t{name}")
print(f"Age:\t{age}")
print(f"ID:\t{id_number}")                 
print(f"Points:\t{points}")
print(f"Future:\t{future_points}")
print(f"ID is {status}")

#Delivery & Cloud Deployment for data types 

print("\n--- DATA TYPES ---")
print(type(name))
print(type(age))
print(type(points))
