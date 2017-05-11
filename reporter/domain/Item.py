"""reporter.Item: Represents Item."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from .Entity import Entity


class Item(Entity):
    """Item entity."""
    def __init__(self, item_id, category, name, cost, line_id):
        Entity.__init__(self)
        self.item_id = item_id
        self.category = category
        self.name = name
        self.cost = cost
        self.line_id = line_id

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.cost < other.cost
