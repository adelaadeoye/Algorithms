#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []

    if len(recipe) == len(ingredients):
        for a, b in recipe.items():
            for c, d in ingredients.items():
                if a == c:
                    batches.append(d//b)
            return min(batches)
    return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 110, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 100, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
