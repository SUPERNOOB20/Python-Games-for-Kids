class Show:

    def __init__(self, watched: bool, rating: int):
        self.watched: bool = watched        # False if show hasn't been watched, True if it has.
        self.rating: int   = rating         # In a range of 0 to 5 stars

        valid_rating = (rating >= 0) and (rating <= 5)     # Checks for a valid rating (0 to 5 stars).

        # TODO: Replace by lambda
        valid_watched = False
        if type(watched) == "bool":
            valid_watched = True

        if not (valid_rating and valid_watched):
            raise Exception ("Formato invalido")


game_of_thrones = Show(True, 1)
harry_potter_philosopher_stone = Show(True, 4)
harry_potter_and_the_deathly_hollows_part_1 = Show(True, 5)
harry_potter_and_the_deathly_hollows_part_2 = Show(False, 0)




### Idea: If the viewer liked two similar shows, recommend a third one that is similar to those two!

# Task: If the viewer watch "harry_potter_philosopher_stone" and "harry_potter_and_the_deathly_hollows_part_1"
#       and gave them a rating of 3 or more, recommend "harry_potter_and_the_deathly_hollows_part_2"

# v  Do the exercise here  v

