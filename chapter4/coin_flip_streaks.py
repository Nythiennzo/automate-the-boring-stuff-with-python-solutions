import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    head_or_tail_list = []
    for i in range(100):
        head_or_tail_list.append(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak_value = None
    streak_length = 0

    for head_or_tail_item in head_or_tail_list:
        if streak_value != head_or_tail_item:
            streak_value = head_or_tail_item
            streak_length = 1
        else:
            streak_length += 1

        if streak_length == 6:
            numberOfStreaks += 1
            streak_value = None
            streak_length = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 100))