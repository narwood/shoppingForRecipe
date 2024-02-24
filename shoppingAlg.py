#for zani
import pandas as pd

#Load in grocery and recipe sheets
recipeDB = pd.read_excel('C:/Users/Suzanna Moran/PearlHacks24/shoppingForRecipe/RecipeData.xlsx', header=1)
groceryDB = pd.read_excel('C:/Users/Suzanna Moran/PearlHacks24/shoppingForRecipe/StoreData.xlsx', header=1)

shopping_list = []

print(recipeDB)
print(recipeDB.columns)
print(groceryDB)
print(groceryDB.columns)

#Find the cheapest option
for recipe_item in recipeDB['Ingredient']:
    cheapest_item = None
    cheapest_price = float('inf')
    grocery_row = 0
    while grocery_row < 8:
        if (recipe_item.lower() in groceryDB['Product'][grocery_row].lower()):
            if (groceryDB['Price'][grocery_row] < cheapest_price):
                print("new cheapest item: " + str(groceryDB['Product'][grocery_row]) + " is " + str(groceryDB['Price'][grocery_row]) + ", cheaper than " + str(cheapest_item) + " at " + str(cheapest_price))
                cheapest_item = groceryDB['Product'][grocery_row]
                cheapest_price = groceryDB['Price'][grocery_row]
        grocery_row += 1
    shopping_list.append(cheapest_item)
print(shopping_list)