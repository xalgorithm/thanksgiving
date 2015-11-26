#!/usr/bin/env python
# Given a list of things to be thankful for in a yaml file output a randomly sorted list of those items as bullet
# points in the command line.
#
# Copyright © 2015 Adam Duston
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.


import os
import yaml
import random
import optparse

THANKS_FILE = os.path.abspath("./thanks.yml")


def parse_command_line(args=None):
    """
    Parse options from the command line.

    :param args: Args passed to the script from the command line
    :return: The options object
    """
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage=usage)

    parser.add_option("-t", "--thanks", action="store", help=("Location of the thanks YAML file. "
                                                              "Default: {0}".format(THANKS_FILE)))
    parser.add_option("-b", "--bullets", action="store_true", help='Output with bullet points')

    opts, _ = parser.parse_args(args)

    if not opts.thanks:
        opts.thanks = THANKS_FILE

    return opts


def main(args=None):
    """
    Main function loads the thanks file and

    :param args: Arguments passed to the script from the command line
    :return: None
    """
    opts = parse_command_line()

    thanks_list = yaml.load(open(os.path.abspath(opts.thanks)))

    # Shuffle the list
    random.shuffle(thanks_list['thanks'])

    for i in thanks_list['thanks']:
        if opts.bullets:
            print "- {0}".format(i)
        else:
            print i


if __name__ == "__main__":
    main()
