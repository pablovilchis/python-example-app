"""reporter.Sale: Represents Sale."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from .Entity import Entity


class Sale(Entity):
    """Sale entity."""
    def __init__(self, sale_id, item_id, customer_id, sale_date,
                 payment_method, line_id):
        Entity.__init__(self)
        self.sale_id = sale_id
        self.item_id = item_id
        self.customer_id = customer_id
        self.sale_date = sale_date
        self.payment_method = payment_method
        self.line_id = line_id
