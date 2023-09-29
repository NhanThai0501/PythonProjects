# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = str(name1.lower())
name2 = str(name2.lower())

# TRUE
name1_temp = int(name1.count("t"))
name2_temp = int(name2.count("t"))

true_sum = name1_temp + name2_temp

name1_temp = int(name1.count("r"))
name2_temp = int(name2.count("r"))

true_sum += name1_temp + name2_temp

name1_temp = int(name1.count("u"))
name2_temp = int(name2.count("u"))

true_sum += name1_temp + name2_temp

name1_temp = int(name1.count("e"))
name2_temp = int(name2.count("e"))

true_sum += name1_temp + name2_temp

# LOVE
name1_temp = int(name1.count("l"))
name2_temp = int(name2.count("l"))

love_sum = name1_temp + name2_temp

name1_temp = int(name1.count("o"))
name2_temp = int(name2.count("o"))

love_sum += name1_temp + name2_temp

name1_temp = int(name1.count("v"))
name2_temp = int(name2.count("v"))

love_sum += name1_temp + name2_temp

name1_temp = int(name1.count("e"))
name2_temp = int(name2.count("e"))

love_sum += name1_temp + name2_temp

total = int(str(true_sum) + str(love_sum))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 10 or total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
