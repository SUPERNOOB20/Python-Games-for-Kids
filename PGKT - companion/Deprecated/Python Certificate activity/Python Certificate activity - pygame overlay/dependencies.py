import sys
import os


# Wait, what do you mean this isn't CMake? :p
def add_libraries(expected_filepath = os.getcwd()):

    try:

        sys.path.append(expected_filepath)      # Snobs will frown upon this forbidden jutsu but PLEASE CUT ME SOME SLACK.
    except:
        print(f"\nError: \033[91mLibraries\033[00m folder not found at {expected_filepath} :c\n")

    return



def add_assets(expected_filepath = "Assets"):

    try:
        os.chdir(expected_filepath)
    except:
        expected_directory = os.getcwd() + "/Assets"
        print(f"\nError: \033[91mAssets\033[00m folder not found. \033[91m{expected_directory}\033[00m doesn't exist :c\n")

    return