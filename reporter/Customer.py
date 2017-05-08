"""reporter.Customer: Represents Customer."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


class Customer():
    """Customer entity."""
    def __init__(self, customer_id, name, email, birthday, gender, address,
                 marital_status, dependents, date, line_id):
        # pylint: disable=unused-argument
        for key, value in locals().items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
