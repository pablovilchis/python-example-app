"""reporter.reporter: provides entry point main()."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import datetime
import sys
import collections

import googlemaps

from reporter import CSVImporter
import reporter.domain

# -*- coding: utf-8 -*-


__version__ = "0.2.0"


def main():
    """Main entry point."""
    if sys.version_info < 2.7:
        raise Exception("Python 2.7 or a more recent version is required.")
    print("Executing bootstrap version %s." % __version__)
    # print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))

    # Import the csv files and export them as a list of objects
    customers = csv_import('data/customers.csv', 'Customer')
    items = csv_import('data/items.csv', 'Item')
    sales = csv_import('data/sales.csv', 'Sale')

    # Group imported customers by age
    age_groups = [0, 19, 29, 39, 150]
    customers_by_age = customers_group_age(age_groups, customers)

    # Group imported customers by region
    regions = ['Eastern', 'Central', 'Mountain', 'Pacific']
    customers_by_region = customers_group_region(customers, regions)

    # Group imported items by ??
    items_dict = collections.defaultdict(list)

    for item in items:
        items_dict[item[0]].extend(item[1:4])

    [sum(i) for i in zip(*items_dict)]

    # Group imported sales by saleId
    sales_dict = collections.defaultdict(list)

    for sale in sales:
        sales_dict[sale.sale_id].extend(sale[0:1, 3:5])




def csv_import(file, to_type):
    csv_importer = CSVImporter.CSVImporter(file, to_type)
    result_set = csv_importer.to_set()
    return result_set


def customers_group_region(customers, regions):
    customers_by_region = []
    for idx, region in enumerate(regions):
        if len(regions) - 1 <= idx:
            break
        customers_by_region.append([c2 for c2 in customers
                                    if filter_by_region(c2, region)])
    return customers_by_region


def customers_group_age(customers: list, age_groups: list) -> list:
    customers_by_age = []
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
    return customers_by_age


def calculate_age(born: datetime) -> int:
    """Calculate age from birthday."""
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) <
                                     (born.month, born.day))


def filter_by_age(customer: reporter.domain.Customer, age_from: int, age_to: int) -> bool:
    """Customer entity."""
    return age_from <= calculate_age(customer.birthday) < age_to


def filter_by_region(customer: reporter.domain.Customer, region: str) -> bool:
    """Customer entity."""

    gmaps = googlemaps.Client(key='AIzaSyCY4P3c7BjpGgrxP8YyYJ6F2_TTWC4kl7U')
    geocode_result = gmaps.geocode(customer.address)
    if len(geocode_result):
        time_zone = gmaps.timezone(geocode_result[0]['geometry']['location'])
        return region in time_zone['timeZoneName'].partition(' ')[0]
    else:
        return False
