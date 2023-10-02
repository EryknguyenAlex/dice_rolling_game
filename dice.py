import random


class Dice():
    @classmethod
    def roll(cls):
        numbers = range(1,7)
        dice_one = random.choice(numbers)
        dice_two = random.choice(numbers)
        return dice_one, dice_two


if __name__ == '__main__':
    dice_one, dice_two = Dice.roll()
    print(dice_one, dice_two)






