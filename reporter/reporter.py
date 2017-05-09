"""reporter.reporter: provides entry point main()."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import sys
from datetime import date
import googlemaps
from . import CSVImporter

# from .Customer import Customer


# -*- coding: utf-8 -*-


__version__ = "0.2.0"


def main():
    """Main entry point."""
    if sys.version_info < 2.7:
        raise Exception("Python 2.7 or a more recent version is required.")
    print("Executing bootstrap version %s." % __version__)
    # print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))

    customers_importer = CSVImporter.CSVImporter('data/customers.csv',
                                                 'Customer')
    customers = customers_importer.to_set()

    items_importer = CSVImporter.CSVImporter('data/items.csv', 'Item')
    items = items_importer.to_set()

    sales_importer = CSVImporter.CSVImporter('data/sales.csv', 'Sale')
    sales = sales_importer.to_set()

    age_groups = [0, 19, 29, 39, 150]
    regions = ['Eastern', 'Central', 'Mountain', 'Pacific']

    customers_by_age = []
    customers_by_region = []

    age_from = age_groups[0]
    age_groups_upto = age_groups[1:]

    for idx, age_upto in enumerate(age_groups_upto):
        if len(age_groups) - 1 <= idx:
            break
        customers_filtered = [c for c in customers
                              if filter_by_age(c, age_from,
                                               age_upto)]
        customers_by_age.append(customers_filtered)
        age_from = age_upto

    for idx, region in enumerate(regions):
        if len(regions) - 1 <= idx:
            break
        customers_by_region.append([c2 for c2 in customers
                                    if filter_by_region(c2, region)])


def calculate_age(born):
    """Calculate age from birthday."""
    today = date.today()
    return today.year - born.year - ((today.month, today.day) <
                                     (born.month, born.day))


def filter_by_age(customer, age_from, age_to):
    """Customer entity."""
    return age_from <= calculate_age(customer.birthday) < age_to


def filter_by_region(customer, region):
    """Customer entity."""
    gmaps = googlemaps.Client(key='AIzaSyCY4P3c7BjpGgrxP8YyYJ6F2_TTWC4kl7U')
    geocode_result = gmaps.geocode(customer.address)
    time_zone = gmaps.timezone(geocode_result)
    return region in time_zone.timeZoneName.partition(' ')[0]
