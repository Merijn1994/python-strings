# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)

report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'

# Part 2
player = 'Hans van Breukelen'

first_name = player[player.find("Hans"):4]

last_name_len = len(player[player.find("van Breukelen"):len(player)])

name_short = player[0] + '. ' + player[player.find("van Breukelen"):len(player)]

chant_with_end_space = len(first_name) * f'{first_name}! '

chant = chant_with_end_space[:len(chant_with_end_space)-1]

good_chant = chant[len(chant) - 1] != ' '