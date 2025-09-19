#OusydSoluman
#09/19/2025
# P1HW2-Travl Expenses
# This program calclates and displays travel expenses

budget=int(input("Enter Budget:"))
destiantion=input("Enter your travel destination:")
gas=int(input(" How much do you think you will spend on gas?"))
Accomodation=int(input("Approximately, how much will you need for accomdation/hotel?"))
Food=int(input("Last, how much do you need for food?"))

total_expenses= gas + Accomodation + Food
remaining_balance= budget - total_expenses 


#------------Travel Ecpenses----------
print("Location", destiantion)
print("Initial Budget", budget)
print("fuel", gas)
print("Accomodation", Accomodation)
print("Food", Food)
print("remaining balance", remaining_balance)