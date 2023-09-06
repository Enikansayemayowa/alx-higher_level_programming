#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name" or hasattr(self, name):
            raise AttributeError("can't set attribute")
        super().__setattr__(name, value)
