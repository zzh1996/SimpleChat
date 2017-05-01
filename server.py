#!/usr/bin/env python3
# encoding: utf-8

import socket, select

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind(('0.0.0.0', 9999))
soc.listen()

print("Server started!")

rlist = [soc]

while 1:
    rs, ws, es = select.select(rlist, [], [])
    for s in rs:
        if s == soc:
            client, addr = soc.accept()
            rlist.append(client)
        else:
            try:
                data = s.recv(4096)
                if data:
                    for client in rlist[1:]:
                        try:
                            client.send(data)
                        except:
                            rlist.remove(client)
                else:
                    rlist.remove(s)
            except:
                rlist.remove(s)
