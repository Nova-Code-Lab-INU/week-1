Name = input("Enter your name:")
Birth_year = int(input("Enter your birth year:"))
Team = input("Enter team Name:")
Score = float(input("Enter initial tech score:")) #taking user input for name ,birth year, team name and intial tech score and converting them to appropriate data types (string for name and team, integer for birth year, and float for score)
Name = Name.strip().title() #stripping any leading or trailing whitespace and converting the name to title case
Team = Team.strip().upper() #stripping any leading or trailing whitespace and converting the team name to uppercase
Age = 2026 - Birth_year #calculatuing age based on birth year
UserID = len(Name) #calculating user ID based on the lenght of the name
Potential_Score = Score ** 1.1 #calculating potential score based on the initial score raised to the power of 1.1

if UserID % 2 == 0 : #checking if the user ID is even or odd and assigning the appropriate value to name_length
   name_length = "even"
else:
    name_length = "odd"
print(f"\n\t\t\t\t\t\t NOVA User ID\t\t\t\t\t\t\n\n Name: {Name}\t\n Birth year : {Birth_year}\t\n Age: {Age} \n UserID: {name_length}\t\n Team: {Team}\t\n Initial tech score: {Score} \n Potential_Score: {Potential_Score}") #printing the user information in a formatted manner
print(f"\t\t\t\t\t\tData Types :\n Age : {type(Age)}\t\n UserID : {type(UserID)}\t\n Potential Score : {type(Potential_Score)}") #printing the data types of age, user ID, and potential score in a formatted manner