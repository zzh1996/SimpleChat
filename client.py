#!/usr/bin/env python3
# encoding: utf-8

import socket, select, sys

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.connect(('127.0.0.1', 9999))
except:
    print('Cannot connect to server!')
    exit()

print('Connected to server!')

name = input("Your name:")

soc.send((name + ' joined in').encode())

while True:
    rs, ws, es = select.select([sys.stdin, soc], [], [])
    for s in rs:
        if s == soc:
            try:
                data = soc.recv(4096)
                if (data):
                    print(data.decode())
                else:
                    print('Disconnected!')
                    exit()
            except:
                print('Disconnected!')
                exit()
        else:
            try:
                soc.send((name + ': ' + sys.stdin.readline()[:-1]).encode())
            except:
                print('Disconnected!')
                exit()
