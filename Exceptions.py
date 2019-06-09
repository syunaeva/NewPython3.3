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
