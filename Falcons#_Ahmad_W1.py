print("***********************************************************************")
print("------------ Nova Member Analytics & Profiling System (V1.0)-----------")
print("***********************************************************************")

# ----------------Data gathering from user----------------------

Full_name = input("Enter your full name: ")             #ask user for name
bd = int(input("What is the birthyear: "))              #ask user for birthday
team = input("Team name: ")                             #ask user for team name
score = int(input("Initial Tech Score: "))              #ask user for score

#----------------Data cleaning and normalization----------------

Full_name = Full_name.capitalize().strip()              #visualizing 
age = 2026 - bd                                         #calculatating age
ID = len(Full_name)                                     #calculating ID
potintial_score = score**1.1                            #calculating potintial
#if ID%2==0:                                            #check even/odd
#    print("Your lab seat is: even")
#else :
#    print("Your lab seat is: odd")

#-------------------------------------Digital ID----------------

print("===============================================================================================")
print("\t\t\t\t\t\tID CARD                       ")
print("===============================================================================================\n")

print(f"\tName:\t\t\t{Full_name} \t type: {type(Full_name)}")                      #display full name
print(f"\tAge:\t\t\t{age} \t\t\t\t type: {type(age)}")                             #display age
print(f"\tID:\t\t\t{ID} \t\t\t\t type: {type(ID)}")                                #display ID
print(f"\tpotintial score:\t{potintial_score} \t\t type: {type(potintial_score)}") #display score
if ID%2==0:                                            
    print("\tYour lab seat is:       even")                                        #display even/odd
else :
    print("\tYour lab seat is:       odd")
print("\n===============================================================================================")

