#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# "THE SCOTCH-WARE LICENSE" (Revision 42):
# <DonMarco42@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a scotch whisky in return
# Marco 'don' Kaulea
# ----------------------------------------------------------------------------

from urllib.request import urlopen
from random import randint


def getRandomRfc():
    while (True):
        counter = 0
        try:
            if(counter > 10):
                break
            ++counter
            con = urlopen("http://www.rfc-editor.org/rfc/rfc%d.txt"
                          % randint(1, 9999))
            return (con.read().decode("utf-8"))
            break
        except Exception:
            continue


def main():
    print (getRandomRfc())

if __name__ == "__main__":
    main()
