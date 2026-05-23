from random import randint

match_1 = (randint(0, 3), randint(0, 3))
match_2 = (randint(0, 3), randint(0, 3))
match_3 = (randint(0, 3), randint(0, 3))

team_a_points = 0
team_b_points = 0

def add_points(match):

    global team_a_points
    global team_b_points

    if match[0] > match[1]:      # if team a wins
        team_a_points = team_a_points + 3
    elif match[1] > match[0]:      # if team b wins
        team_b_points = team_b_points + 3
    else:           # they tied
        team_a_points = team_a_points + 1
        team_b_points = team_b_points + 1

    return

add_points(match_1)
add_points(match_2)
add_points(match_3)

print("argentina:", team_a_points)
print("USA:", team_b_points)