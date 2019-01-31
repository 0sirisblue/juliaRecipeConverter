import time

foodType = 'default'
foodTypeUnit = 'default'
numIngredients = 0



print('\nRECIPE INGREDIENT CALCULATOR v0.1\n')
print('-' * 30 + '\n')
print("This program will assist you in calculating the amount of ingredients needed \
to make a recipe, in any size or proportion, given an initial recipe.\n")
time.sleep(1)

print("First, let's get to know your initial recipe.\n")
foodType = input("What type of food are you making? (cookies, pies, tacos, etc.)\n- ")
time.sleep(1)

foodTypeUnit = input("What is the unit of measure for your final serving? (servings,\
 ounces, pies, etc.\n- ")
time.sleep(1)

numIngredients = int(input("How many ingredients does your recipe have? ")
