"""
Author: Miles Catlett
Date: 12/13/2022
This program allows the client to receive and send information from/to the server. This could allow for a variety of
games to be played, written in current format.
"""

import socket

HOST = "127.0.0.1"
PORT = 2001


def main():
    """
    This function allows the client to interact with the server.
    :return: None
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
        print(data.decode())
        name = input()
        s.sendall(name.encode())
        response = 'response'
        while response != 'x' or response != 'X':
            data = s.recv(1024)
            print(data.decode())
            response = input()
            s.sendall(response.encode())
            if response == 'x' or response == 'X':
                data = s.recv(1024)
                print(data.decode())
                break


main()