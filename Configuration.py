# -*- coding: utf8 -*- 

__author__ = "A. Daouzli"
__copyright__ = "Copyright 2013, A. Daouzli"
__licence__ = "GPL3"
__version__ = "0.0.1"
__maintainer__ = "A. Daouzli"


"""
    Implementation of a config container

    25/06/2012 - A. Daouzli

"""


class Configuration(dict):
    def __init__(self, config_file=None, attrs=None):
        super(Configuration, self).__init__()
        if attrs is not None:
            self.set_attributes(attrs)
        self._elems = None
        self._idx = 0
        if config_file:
            self.get_config_from_file(config_file)

    def __str__(self):
        txt = ''
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                txt += key + ': ' + str(value) + '\n'
        return txt

    def __getattr__(self, attr):
        def mutator(*args, **kwargs):
            '''Define custom getters and setters

            '''
            if attr.startswith('get_'):
                attrib = attr.replace('get_', '')
                return self.__getattribute__(attrib)
            elif attr.startswith('set_'):
                attrib = attr.replace('set_', '')
                self.__setattr__(attrib, args[0])
            else:
                msg = "{} has no attribute {}".format(self.__class__.__name__, attr)
                raise AttributeError(msg)
        return mutator

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        self._idx = 0
        self._elems = [key for key in self.__dict__ if not key.startswith('_')]
        return self

    # for Python3
    def __next__(self):
        if self._idx >= len(self._elems):
            self._idx = 0
            raise StopIteration
        elem = self._elems[self._idx]
        self._idx += 1
        return elem

    # for Python2
    def next(self):
        if self._idx >= len(self._elems):
            self._idx = 0
            raise StopIteration
        elem = self._elems[self._idx]
        self._idx += 1
        return elem

    def __contains__(self, elem):
        return elem in self.__dict__

    def items(self):
        return [(key, value) for key, value in self.__dict__.items()
                if not key.startswith('_')]

    def set_attributes(self, kwarg):
        '''Set attributes to the config. Note that the attributes names will be
        stored in lower case format.

        @param attrs: dictionary containing the attributes
        @type attrs: dictionary

        '''
        for key, value in kwarg.items():
            self.__dict__[key.lower()] = value

    def get_configuration(self):
        return dict([(key, value) for key, value in self.__dict__.items()
                if not key.startswith('_')])

    def get_config_from_file(self, filename):
        '''Set the attributes from a file containing couples of key/value.
        each couple have string elements (the value can be between double quotes)
        comments are ignored (starts with #) and the key is converted to lower case.

        @param filename: name of the configuration file to parse

        '''
        for line in open(filename).readlines():
            try:
                line = line[:line.index("#")].strip()
            except:
                line = line.strip()
            if len(line) == 0:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].strip()
            if len(value) == 0:
                continue
            self.__dict__[key.lower()] = value
