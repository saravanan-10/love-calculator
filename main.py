print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n") 
name2 = input("What is their name? \n")  

combine_names = (name1 + name2).lower()
t = combine_names.count("t")
r = combine_names.count("r")
u = combine_names.count("u")
e = combine_names.count("e")
first_half_count = t + r + u + e

l = combine_names.count("l")
o = combine_names.count("o")
v = combine_names.count("v")
e = combine_names.count("e")
second_half_count = l + o + v + e

combine_count = str(first_half_count) + str(second_half_count)
combine_count = int(combine_count)

if combine_count < 10 or combine_count > 90:
  print(f"Your score is {combine_count}, you go together like coke and mentos.")
elif combine_count > 40 or combine_count < 50:   
  print(f"Your score is {combine_count}, you are alright together.")
else:
  print(f"Your score is {combine_count}.")