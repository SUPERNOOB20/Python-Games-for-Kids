from math import sqrt

def quadratic(a, b, c):
    x1 = -b / (2*a)
    x2 = sqrt(b**2 - 4*a*c) / (2*a)
    return (x1 + x2), (x1 - x2)





def student_info(*args, **kwargs):
    print("Subjects:", args)        # Positional arguments
    print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English")










quadratic(a=31, b=93, c=62)