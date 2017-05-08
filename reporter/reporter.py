"""reporter.reporter: provides entry point main()."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import sys
from datetime import date
from geograpy import places
from .CSVImporter import CSVImporter

# from .Customer import Customer


# -*- coding: utf-8 -*-


__version__ = "0.2.0"


def main():
    """Main entry point."""
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    print("Executing bootstrap version %s." % __version__)
    # print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))

    customers_importer = CSVImporter('data/customers.csv', 'Customer')
    customers = customers_importer.to_list()

    items_importer = CSVImporter('data/items.csv', 'Item')
    items = items_importer.to_set()

    sales_importer = CSVImporter('data/sales.csv', 'Sale')
    sales = sales_importer.to_set()

    age_groups = [0, 19, 29, 39, 150]

    customers_groups = []

    for idx, age in enumerate(age_groups):
        # pylint: disable=W0612
        customers_groups.append([c for c in customers
                                 if filter_by_age(c, age_groups[idx],
                                                  age_groups[idx + 1])])
        

def calculate_age(born):
    """Calculate age from birthday."""
    today = date.today()
    return today.year - born.year - ((today.month,
                                      today.day) < (born.month, born.day))


def filter_by_age(customer, age_from, age_to):
    """Customer entity."""
    return age_from <= calculate_age(customer.birthday) < age_to
