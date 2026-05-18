import sys
import os
import pathlib


# Wait, what do you mean this isn't CMake? :p
def add_libraries(expected_filepath = pathlib.Path(__file__).parent.resolve()):

    try:
        sys.path.append(expected_filepath)      # Snobs will frown upon this forbidden jutsu but PLEASE CUT ME SOME SLACK.
    except:
        print(f"\nError: \033[91mLibraries\033[00m folder not found at {expected_filepath} :c\n")

    return



def add_assets(expected_filepath = "Assets"):

    absolute_filepath = os.path.join(pathlib.Path(__file__).parent.resolve(), expected_filepath)

    try:
        os.chdir(absolute_filepath)
    except:
        expected_directory = absolute_filepath
        print(f"\nError: \033[91mAssets\033[00m folder not found.\n\033[91m{expected_directory}\033[00m doesn't exist :c\n")
        print(f"Error: Couldn't find {absolute_filepath}")

    return