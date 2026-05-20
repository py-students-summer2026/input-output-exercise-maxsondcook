"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    favorite_vegetable= input("What is your favorite vegetable? ")
    x = favorite_vegetable
    print("Interesting! I also love " + x + "!")

def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    favorite_number = input("What is your favorite number? ")
    x = favorite_number
    print("Interesting! I also love " + x + "!")

def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    name = input("What is your name? ")
    x = name
    zodiac_sign = input("What is your zodiac sign? ")
    y = zodiac_sign
    print("Interesting! My name is also " + x + ", and I'm also a " + y + "!")

def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    name = input("What is your name? ")
    x = name
    age = input("What is your age? ")
    y = age
    print("Interesting! My name is also " + x + ", and I'm also " + y + " years old!")