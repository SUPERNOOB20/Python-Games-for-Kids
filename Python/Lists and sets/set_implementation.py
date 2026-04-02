#####   This file acts as a "tutorial" for teaching the set data structure...!

# Python already has a set
# A set is a list of many elements where none of the elements are repeated.

# Can you implement a set in Python...?
# Make a function that, when given a list, returns a set with the same elements!

# ----------------------------------------------------------

#  v  Your answer here  v






# ----------------------------------------------------------



# So? Could you do it? ^_^
# Here, have my resolution of the exercise as an example:


# When given a list, this function returns a set with the same elements.
def eliminates_repeated_elements(list):

    set = []

    for element in list:
        if element not in set:
            set.append(element)

    return set



list = [True, 6, 7, "Art", 7, "Maths", 7, 6, True, 6, 6]

print(eliminates_repeated_elements(list))




# Python already has an implementation of sets!

# Note that lists go in square brackets [], with their elements separated by commas.
# Note that sets  go in curly brackets  {}, with their elements separated by commas.

dummy_list = [True, 6, 7, "Art", 7, "Maths", 7, 6, True, 6, 6]
dummy_set = {True, 6, 7, "Art", 7, "Maths", 7, 6, True, 6, 6}

print("Type of dummy_list:", type(dummy_list))
print("Type of dummy_set:", type(dummy_set))

print("dummy list:", dummy_list)
print("dummy_set:", dummy_set)




# You can also cast lists (or other datatypes, too!) to sets, like this:

# Example number one:
print("dummy_set (cast):", set(dummy_list))


# Example number two:
dummy_list_number_two = ["P.E", "Art", 6, False, "Art", 67, 67, False, True, 6, 7, "Art"]
set_of_dummy_list_number_two = set(dummy_list_number_two)

print(set_of_dummy_list_number_two)