#!/usr/bin/env python3
# coding: utf-8

class MakeURL(object):
    """
    Class for make git url
    """

    def __init__(self, *args, **kwargs):
        try:
            self._url = kwargs["url"]
        except KeyError:
            self._url = False

    @property
    def url(self):
        return self._url
