#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    num_of_batches = 0

    # Base case – Check if there are recipes
    if len(recipe) == 0:
        return 0

    for item in recipe:
        # Check if there are ingredients
        if item not in ingredients.keys():
            return 0
        # Check if there are enough ingredients for recipe
        elif ingredients[item] < recipe[item]:
            return 0

    # If there are enough ingredients, check how many batches can be made
    has_enough_ingredients = True
    # Make a copy of ingredients, so the original list isn't mutated
    ingredients_list = ingredients
    while has_enough_ingredients:
        for item in recipe:
            if recipe[item] <= ingredients_list[item]:
                ingredients_list[item] -= recipe[item]
            else:
                has_enough_ingredients = False
                break

         # If there are enough ingredients, increment the batches
        if has_enough_ingredients:
            num_of_batches += 1

    return num_of_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
