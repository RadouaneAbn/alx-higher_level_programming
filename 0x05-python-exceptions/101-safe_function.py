#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    functions_return = None
    try:
        functions_return = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)

    return functions_return
