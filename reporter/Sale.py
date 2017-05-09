"""reporter.Sale: Represents Sale."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


class Sale:
    """Sale entity."""
    def __init__(self, sale_id, item_id, customer_id, sale_date,
                 payment_method, line_id):
        self.sale_id = sale_id
        self.item_id = item_id
        self.customer_id = customer_id
        self.sale_date = sale_date
        self.payment_method = payment_method
        self.line_id = line_id

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
