"""
INSTRUCTIONS
1. CALCULATE REMAINING BAKE TIME IN MINUTES: 
Implement the bake_time_remaining() function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes 
the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.

2. CALCULETE PREPARATION TIME IN MINUTES
Implement the preparation_time_in_minutes(number_of_layers) function that takes the number of layers you want to add to the lasagna as an argument and 
returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.

3. CALCULATE TOTAL ELAPSED COOKING TIME (PREP + BAKE) IN MINUTES
Implement the preparation_time_in_minutes(number_of_layers) function that takes the number of layers you want to add to the lasagna as an argument and 
returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.

4. CALCULATE TOTAL ELAPSED COOKING TIME (PREP + BAKE) IN MINUTES
Implement the elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) function that has two parameters: number_of_layers (the number of layers added 
to the lasagna) and elapsed_bake_time (the number of minutes the lasagna has been baking in the oven). This function should return the total number of 
minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

5. UPDATE THE RECIPE WITH NOTES
Go back through the recipe, adding "notes" in the form of function docstrings.

"""

#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(input_data):
    """"""
    return EXPECTED_BAKE_TIME - input_data

#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
PREPARATION_TIME = 2
def preparation_time_in_minutes(number_of_layers):
    """"""
    return number_of_layers * PREPARATION_TIME
    


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
