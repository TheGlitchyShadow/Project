pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
briyani = ("Chicken Briyani", "Indian", 40, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

all_recipes = (pasta, briyani)
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe time:", all_recipes[1][2], "mins")
print("Pasta details (Sliced):", pasta[1:3])

print("\nPatsa recipe details:")
for detail in pasta:
    print(" -", detail)
