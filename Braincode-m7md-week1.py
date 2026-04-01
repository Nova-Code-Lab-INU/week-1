#Data collection 

full_name=input("Enter your name :")
birth_year=input("Enter your year :")
team_name=input("Enter your team :")
score=input("Enter your score :")

#Data Cleaning

clean_name = full_name.strip().title()
clean_team = team_name.upper()
 
#Arithmetic operations

birth_year=int(birth_year)
score=float(score)

#The Logic Hub (Arithmetic & Analysis)

current_year=2026

age=current_year - birth_year

ID_user=len(full_name)

potential_score=score**1.1

if ID_user%2==0:
  ID_type="Even"
else:
  ID_type="Odd"

#Professional System Output (The Report)

print("************************************************")
print(type(clean_name))
print(type(age))
print(type(score))

#Delivery & Cloud Deployment

print("************************************************")
print("Name: ",{clean_name})
print("Team: ",{clean_team})
print("Age: ",{age})
print("User ID: ",{ID_user},{ID_type})

