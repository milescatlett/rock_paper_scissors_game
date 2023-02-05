"""
Author: Miles Catlett
Date: 12/13/2022
This program allows the server to pull from any game file written in the rock, paper, scissors game format and play it
with the client side.
"""

import rock_paper_scissors_game as rps
from socket import *
localhost = gethostbyname("localhost")

HOST = localhost
PORT = 2001  # don't use ports less than 1024


def main():
    """
    This function allows the server to run the game and interact with client.
    :return: None
    """
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server started...")
        con, address = s.accept()
        with con:
            print(f"Connection by {address}")
            con.sendall(b"Enter your name: ")
            name = con.recv(1024)
            directions = rps.game_directions(name)
            con.sendall(directions)
            data = con.recv(1024)
            client_count = 0
            server_count = 0
            data = data.decode()
            while data != 'x' or data != 'X':
                game = rps.game(data)
                con.sendall(game[0].encode())
                client_count += game[1]
                server_count += game[2]
                data = con.recv(1024)
                data = data.decode()
                if data == 'x' or data == 'X':
                    msg = "You won " + str(client_count) + " games, and the computer won " + str(server_count) + ".\n"
                    if client_count > server_count:
                        msg += "Congratulations! You won!"
                    elif client_count < server_count:
                        msg += "Sorry. Better luck next time."
                    else:
                        msg += "You tied with the computer."
                    con.sendall(msg.encode())
                    break


main()
