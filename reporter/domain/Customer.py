"""reporter.Customer: Represents Customer."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from datetime import datetime
from .Entity import Entity


class Customer(Entity):
    """Customer entity."""
    def __init__(self, customer_id, name, email, birthday, gender, address,
                 marital_status, dependents, date, line_id):
        # for key, value in locals().items():
            # setattr(self, key, value)
        Entity.__init__(self)
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.birthday = datetime.strptime(birthday, "%m/%d/%Y")
        self.gender = gender
        self.address = address
        self.marital_status = marital_status
        self.dependents = dependents
        self.date = datetime.strptime(date, "%m/%d/%Y")
        self.line_id = line_id
