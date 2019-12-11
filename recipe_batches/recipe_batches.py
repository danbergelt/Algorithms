#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # instantiate infinite number of minimum batches for comparison
  minBatches = math.inf

  # loop through all ingredients in the recipe
  for ingredient in recipe:
    # if we are missing this ingredient, return 0 and break
    if ingredient not in ingredients:
      minBatches = 0
      break
    # finding the smallest number of minimum batches, and setting that to minBatches
    if ingredients[ingredient] // recipe[ingredient] < minBatches:
      minBatches = ingredients[ingredient] // recipe[ingredient]
  
  return minBatches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))