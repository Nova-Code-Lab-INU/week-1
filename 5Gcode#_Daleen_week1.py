#data collection 
full_name=input("Enter Full Name: ")
birth_year=int(input("Enter Birth year"))
team_name=input("Enter Team Name")
tech_score=float(input("Enter Initial Tech Score (0-100):"))
#data cleaning & normalization 
#remove  any accidental leading/trailing spaces from the name
#ensure member name
clean_name=full_name.strip().title()
#format the team name to be strictly UPERCASE
clean_team=team_name.upper()
#the logic hub
#age calculation
current_year=2026
age=current_year-birth_year
#unique identifier 
user_id=len(clean_name)
#growth projection
potential_score= tech_score**1.1
#even/odd check 
seat_type="Even" if user_id %2==0 else "Odd"
#professional system output(the report) 
print("\n" +"="*40)
print(f"TECHNICAL IDENTITY CARD")
print("="*40)
print(f"Full Name:\t{clean_name}")
print(f"Team Name:\t{clean_team}")
print(f"Current Age:\t{age}")
print(f"User ID:\t{user_id}")
print(f"Seat:\t{seat_type})")
print("-"*40)
print(f"Tech Score:\t{tech_score}%")
print(f"Potential Score :\t{potential_score:.2f}%")
print("-"*40)
#display data categories 
print(f"\n[Data Types]:Name {type(clean_name)}: , ID: {type(user_id)},Score {type(potential_score)}")
print("="*40)