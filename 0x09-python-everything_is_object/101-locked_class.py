#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attr, value):
        if hasattr(self, attr) or attr == "first_name":
            super().__setattr__(attr, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(attr))
