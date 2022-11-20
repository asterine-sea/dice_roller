import random

def get_input_string():
    """A function to get the input from the console
    and return it.

    Returns:
        string: A string containing the input from the console
    """
    string = input("> ")
    return string

def parse_input(string):
    """A function that parses the input at the character 'd'.

    Args:
        string (string): The string to be parsed.

    Returns:
        split_string (list of strings): The parsed list of strings
        as a result from the split function.
    """
    if string != '':
        split_string = string.split('d')
        return split_string
    else:
        return

def roll_loop(num_dice, num_sides):
    """A function that loops over the number of dice,
    generating a random number between 1 and the given
    number of sides. This also stores the values of each
    roll in the global "output_rolls" list.

    Args:
        num_dice (int): The number of dice to be rolled.
        num_sides (int): The number of sides the die has.

    Returns:
        int: The total of all rolls.
    """
    total = 0
    output_rolls = []
    random.seed()
    for i in range(num_dice):
        roll = random.randrange(1, num_sides+1)
        output_rolls.append(roll)
        total += roll
    return total, output_rolls

def main():
    while True:
        dice_to_roll = []
        rolls_to_output = []
        total_roll = 0
        dice_to_roll = parse_input(get_input_string())
        total_roll, rolls_to_output = roll_loop(int(dice_to_roll[0]), int(dice_to_roll[1]))
        output_string = f"{total_roll}: ( "

        for i in rolls_to_output:
            output_string += str(i)
            output_string += " "

        output_string += ")"

        print(output_string)

main()
