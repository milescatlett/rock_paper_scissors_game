"""
Author: Miles Catlett
Date: 12/13/2022
This is the rock paper scissors game. It can be fit with the server and client programs to allow the game to be played.
It has two functions: The game and the game directions.
"""

import random


def game(client_input):
    """
    This function consists of the game rules.
    :param client_input: str: user input
    :return: str: response or message
    """
    if client_input != 'r' and client_input != 'p' and client_input != 's':
        return ["You must enter 'r', 'p', or 's'. Please try again.", 0, 0]
    client_sel = 0
    if client_input == 'p' or client_input == 'P':
        client_sel = 1
    elif client_input == 's' or client_input == 'S':
        client_sel = 2
    plays = ["Rock.", "Paper.", "Scissors."]
    server_sel = random.randint(0, 2)
    play = "You played " + plays[client_sel] + "\n" + "The computer played " + plays[server_sel] + "\n"
    again = "Enter 'r', 'p', or 's' to play again, or enter 'x' to end the game."
    if client_sel == server_sel:
        return [play + "That's a tie!\n" + again, 0, 0]
    elif client_sel == 0 and server_sel == 2:
        return [play + "You win!\n" + again, 1, 0]
    elif client_sel == 1 and server_sel == 1:
        return [play + "You win!\n" + again, 1, 0]
    elif client_sel == 2 and server_sel == 1:
        return [play + "You win!\n" + again, 1, 0]
    else:
        return [play + "The computer wins!\n" + again, 0, 1]


def game_directions(name):
    """
    This function returns the directions to the game.
    :param name: str: name
    :return: str: directions
    """
    directions = b"Welcome, " + name + b".\n" + \
                 b"You are playing 'Rock, Paper, Scissors!\n" + \
                 b"Make your play by typing 'r' for 'Rock'...\n" + \
                 b"'p' for 'Paper'...\n" + \
                 b"And 's' for 'Scissors'...\n" + \
                 b"The computer will respond instantly when you play.\n" + \
                 b"Enter 'x' when you want to exit.\n" + \
                 b"Make your first play.\n"
    return directions

