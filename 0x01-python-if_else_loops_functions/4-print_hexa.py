#!/usr/bin/python3
for i in range(99):
    print("{i:d} = {hexa_i}\n".format(i=int(i), hexa_i=hex(i)), end="")
