all_groups: list[tuple[int]] =  []

first_group: list[tuple[int]] = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
all_groups.append(first_group)

for i in range(1, 12):      # 12 groups.

    for match in range(0, len(first_group)):
        a = first_group[match][0]
        b = first_group[match][1]
        # print("a:", a)
        # print("b:", b)
        next_group_team_a = a + (i * 4)
        next_group_team_b = b + (i * 4)

        next_group = ((next_group_team_a, next_group_team_b))

        all_groups.append(next_group)

print(all_groups)