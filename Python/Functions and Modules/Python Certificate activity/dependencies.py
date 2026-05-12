import sys
import os


# Wait, what do you mean this isn't CMake? :p
def add_libraries(expected_filepath = os.getcwd()):

    try:
        sys.path.append(expected_filepath)
    except:
        print(f"Error: \033[91mLibraries\033[00m folder not found.  at {os.getcwd()} :c")

    return



def add_assets(expected_filepath = "Assets"):

    try:
        os.chdir(expected_filepath)
    except:
        print(f"Error: \033[91mAssets\033[00m folder not found at {os.getcwd()} :c")

    return