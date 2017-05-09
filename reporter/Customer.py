"""reporter.Customer: Represents Customer."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from datetime import datetime
import locale


class Customer():
    """Customer entity."""
    def __init__(self, customer_id, name, email, birthday, gender, address,
                 marital_status, dependents, date, line_id):
        # for key, value in locals().items():
            # setattr(self, key, value)
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
