#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# "THE SCOTCH-WARE LICENSE" (Revision 42):
# <DonMarco42@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a scotch whisky in return
# Marco 'don' Kaulea
# ----------------------------------------------------------------------------
"""Random RFC

Usage:
    random_rfc.py
    random_rfc.py <index>
"""

import requests
import random
import docopt as dopt


class PageNotFoundException(Exception):
    pass


def get_random_rfc():
    while (True):
        counter = 0
        try:
            if(counter > 50):
                break
            counter += 1
            return get_rfc(random.randint(1, 9999))
        except requests.ConnectionError:
            exit(1)
        except PageNotFoundException:
            continue


def get_rfc(number):
    link = "http://www.rfc-editor.org/rfc/rfc{number}.txt".format(number=number)
    r = requests.get(link)
    r.encoding = 'utf-8'
    if 200 == r.status_code:
        return r.text
    else:
        raise PageNotFoundException


if __name__ == "__main__":
    arguments = dopt.docopt(__doc__)
    if "<index>" in arguments and arguments["<index>"]:
        try:
            print(get_rfc(arguments["<index>"]))
        except PageNotFoundException:
            print("There is no rfc{}. Try another indey".format(
                arguments['<index>']))
    else:
        print(get_random_rfc())
