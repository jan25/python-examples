import re
from abc import ABC, abstractmethod
from typing import Callable


class Scheme:
    @classmethod
    def get_scheme(cls):
        raise NotImplementedError('not implemented')


class HTTPScheme(Scheme):
    SCHEME = 'http://'

    @classmethod
    def get_scheme(cls):
        return cls.SCHEME


# Add more schemes


class TLD:
    @classmethod
    def get_tld(cls):
        raise NotImplementedError('not implemented')


class ComTLD(TLD):
    TLD_ = '.com'

    @classmethod
    def get_tld(cls):
        return cls.TLD_

# Add more TLDs


class UrlConstructor(HTTPScheme, ComTLD):
    @classmethod
    def construct(cls, server_name):
        return cls.get_scheme() + server_name + cls.get_tld()


print(UrlConstructor.construct("google"))
