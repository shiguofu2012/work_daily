#!/usr/bin/python


class storage(dict):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            value = self[key]
            return value
        except KeyError, k:
            return k

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            return k

    def __call__(self, key):
        try:
            return self[key]
        except KeyError, k:
            return k

if __name__ == '__main__':
    s = storage()
    s.name = "gfshi"
    print hasattr(s, 'name')
