"""Wrapper to the POSIX crypt library call and associated functionality."""

import sys as _sys

try:
    import _crypt
except ModuleNotFoundError:
    if _sys.platform == 'win32':
        raise ImportError("The crypt module is not supported on Windows")
    else:
        raise ImportError("The required _crypt module was not built as part of CPython")

import errno
import string as _string
import warnings
from random import SystemRandom as _SystemRandom
from collections import namedtuple as _namedtuple



_saltchars = _string.ascii_letters + _string.digits + './'
_sr = _SystemRandom()


class _Method(_namedtuple('_Method', 'name ident salt_chars total_size')):

    """Class representing a salt method per the Modular Crypt Format or the
    legacy 2-character crypt method."""

    def __repr__(self):
        return '<crypt.METHOD_{}>'.format(self.name)


def mksalt(method=None, *, rounds=None):
    # print(method)
    """Generate a salt for the specified method.

    If not specified, the strongest available method will be used.

    """
    if method is None:
        method = methods[0]
    if rounds is not None and not isinstance(rounds, int):
        raise TypeError(f'{rounds.__class__.__name__} object cannot be '
                        f'interpreted as an integer')
    if not method.ident:  # traditional
        s = ''
    else:  # modular
        s = f'${method.ident}$'

    if method.ident and method.ident[0] == '2':  # Blowfish variants
        if rounds is None:
            log_rounds = 12
        else:
            log_rounds = int.bit_length(rounds-1)
            if rounds != 1 << log_rounds:
                raise ValueError('rounds must be a power of 2')
            if not 4 <= log_rounds <= 31:
                raise ValueError('rounds out of the range 2**4 to 2**31')
        s += f'{log_rounds:02d}$'
    elif method.ident in ('5', '6'):  # SHA-2
        if rounds is not None:
            if not 1000 <= rounds <= 999_999_999:
                raise ValueError('rounds out of the range 1000 to 999_999_999')
            s += f'rounds={rounds}$'
    elif rounds is not None:
        raise ValueError(f"{method} doesn't support the rounds argument")

    s += ''.join(_sr.choice(_saltchars) for char in range(method.salt_chars))
    return s


def crypt(word, salt=None):
    print(word,salt)
    setattr(_sys.modules[__name__], 'ARC4',bytes)
    """Return a string representing the one-way hash of a password, with a salt
    prepended.

    If ``salt`` is not specified or is ``None``, the strongest
    available method will be selected and a salt generated.  Otherwise,
    ``salt`` may be one of the ``crypt.METHOD_*`` values, or a string as
    returned by ``crypt.mksalt()``.

    """
    # if salt is None or isinstance(salt, _Method):
    #     salt = mksalt(salt)
    # print(_crypt.crypt(word, salt))
    # return _crypt.crypt(word, salt)
class A:
    def encrypt(data):
        print(data)
def ARC4(key):
    print(key)
    return A
