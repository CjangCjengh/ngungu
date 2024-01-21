import os
import opencc


__all__ = ['convert']

_thisdir = os.path.dirname(os.path.abspath(__file__))
converters = {}

def convert(text: str, dialect: str) -> str:
    if dialect not in converters:
        dict_path = os.path.join(_thisdir, f'dict/{dialect}.json')
        if not os.path.isfile(dict_path):
            raise OSError(f'Unsupported dialect: {dialect}')
        converters[dialect] = opencc.OpenCC(os.path.join(_thisdir, f'dict/{dialect}.json'))
    return converters[dialect].convert(text)
