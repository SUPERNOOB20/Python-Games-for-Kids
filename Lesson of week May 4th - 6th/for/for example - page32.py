# Example 1: the one from the book

for counter in range(1, 11):
    print('Emma\'s Room - Keep Out!!!')


# Example 2: casting
# Casting allows us to convert information into text, so we can print it.
print("\n\n")


for counter in range(1, 11):
    message = "WARNING #" + str(counter) + ": Emma's Room, Keep Out!!!"
    print(message)



# Example 3: string interpolation
# String interpolation allows us to print information that isn't text.
print("\n\n")


for counter in range(1, 11):
    print(f"WARNING #{counter}: Emma's Room, Keep Out!!!")