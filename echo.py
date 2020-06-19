#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "sohailadev"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""

    # parser = argparse.ArgumentParser(
    #     description='Perform transformation on input text.')
    # parser.add_argument('-u', '--upper',
    #                     help="convert text to uppercase", action="store_true")
    # parser.add_argument('-l', '--lower',
    #                     help="convert text to lowercase", action="store_true")
    # parser.add_argument('-t', '--title',
    #                     help="convert text to titlecase", action="store_true")
    # parser.add_argument("text", help="text to be manipulated")
    # return parser
    """Creates and returns an argparse cmd line option parser."""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true")
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    # print(args)
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not args:
        parser.print_usage()
        sys.exit()
    message = ns.text
    print(ns)
    if ns.upper:
        message = message.upper()

    if ns.lower:
        message = message.lower()

    if ns.title:
        message = message.title()

    print(message)


if __name__ == '__main__':
    main(sys.argv[1:])
