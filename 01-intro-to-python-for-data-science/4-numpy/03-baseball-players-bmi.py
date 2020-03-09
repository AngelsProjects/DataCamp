'''
Baseball player's BMI
100xp
The MLB also offers to let you analyze their weight data. Again, both are available as regular
Python lists: height and weight. height is in inches and weight is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert height to
a numpy array with the correct units is already available in the workspace. Follow the instructions
step by step and finish the game!

Instructions
-Create a boolean numpy array: the element of the array should be True if the corresponding baseball
 player's BMI is below 21. You can use the < operator for this. Name the array light.
-Print the array light.
-Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light 
 inside square brackets to do a selection on the bmi array.
'''
# height and weight are available as regular lists

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
