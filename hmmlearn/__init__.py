"""
HMMlearn: Hiden Markov Models in Python with scikit-learn like API
====================================================================

HMMlearn is a set of algorithm for learning and inference of Hiden Markov
Models.

Historically, this code was present in scikit-learn, but unmaintained. It
has been orphaned and separated as a different package.

"""
__version__ = '0.1a'


def setup_module(module):
    """Fixture for the tests to assure globally controllable seeding of RNGs
    """

    import os
    import numpy as np
    import random

    # It could have been provided in the environment
    _random_seed = os.environ.get('HMMLEARN_SEED', None)
    if _random_seed is None:
        _random_seed = np.random.uniform() * (2 ** 31 - 1)
    _random_seed = int(_random_seed)
    print("I: Seeding RNGs with %r" % _random_seed)
    np.random.seed(_random_seed)
    random.seed(_random_seed)