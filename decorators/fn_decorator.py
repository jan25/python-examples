import functools
import re


def exclude_url(url, pattern):
    return re.search(pattern, url) is not None


def print_args(fn):
    @functools.wraps(fn)
    def wrapper_fn(*args, **kwargs):
        print(fn.__name__, 'called with', args, kwargs)
        return fn(*args, **kwargs)
    return wrapper_fn


def exclude_urls(pattern):
    def decorator_fn(fn):
        @functools.wraps(fn)
        def wrapper_fn(url, *args, **kwargs):
            if not exclude_url(url, pattern):
                return fn(url, *args, **kwargs)
        return wrapper_fn
    return decorator_fn


@print_args
@exclude_urls(".com|.org")
def parse_url(url):
    print(url)


parse_url("google.com")
parse_url("abc.xyz")
