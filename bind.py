#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys

__author__ = 'guanr'

host = "127.0.0.1"
sockets = []


def bind(bport, eport):
    for i in range(int(bport), int(eport)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockets.append(s)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((host, i))
            s.listen(1)
        except WindowsError as e:
            print("bind %d failed" %i)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("run bind.py as python bind.py 8900 8910")
    else:
        bind(sys.argv[1], sys.argv[2])
    print("Press any key to exit...")
    input()

