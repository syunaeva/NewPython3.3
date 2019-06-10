"""
new ways to use exceptions
"""
import traceback


def example1():
    """
    include traceback
    :return:
    """
    try:
        raise Exception
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)


def example2():
    """
    implicit exception chain
    """
    try:
        raise Exception
    except Exception:
        raise NotImplementedError # __context__ set - no loss date during debugging

def example3():
    """
    explicit exception chain
    :return:
    """
    try:
        raise Exception
    except Exception as exc:
        # Sets __cause__
        # In Python 3.3, ''from None''supresses
        raise NotImplementedError from exc

example3()
