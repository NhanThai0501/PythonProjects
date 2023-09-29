#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What is the total bill? "))

people = int(input("How many people are in your party? "))

tip_rates = float(input("What is the tip rate (10% 12% 15% 18%) ? "))

bill_per_person = (bill / people) + (bill / people) * float(tip_rates/100.0)
bill_per_person = round(tip_per_person, 2)

message = f"Each person will pay {bill_per_person}$"

print(message)
