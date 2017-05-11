"""reporter.Entity: Represents an model entity."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import json


class Entity(object):
    """Model entity."""
    def __init__(self):
        pass

    def to_json(self):
        """Model entity."""
        json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        """Model entity."""
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return other is not self
