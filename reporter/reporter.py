"""reporter.reporter: provides entry point main()."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
import pandas as pd
import googlemaps as gm
from datetime import datetime

# -*- coding: utf-8 -*-
__version__ = "0.2.0"


def main():
    """Main entry point."""
    if not sys.version_info[0] >= 3:
        raise Exception("Python 2.7 or a more recent version is required.")
    print("Executing bootstrap version %s." % __version__)

    # Import the csv files and export them as a list of objects
    customers = csv_import(os.path.join(os.path.dirname(__file__), 'data/customers.csv')).drop_duplicates()
    items = csv_import(os.path.join(os.path.dirname(__file__), './data/items.csv'))
    sales = csv_import(os.path.join(os.path.dirname(__file__), './data/sales.csv'))

    # Join sales, customers, items dataframes
    sale_cust = pd.merge(sales, customers, on='customerId')
    sale_cust_item = pd.merge(sale_cust, items, on='itemId')

    # Calculate age from birthday
    sale_cust_item['age'] = [calculate_age(x) for x in sale_cust_item['customerBirthday']]
    # Group sale_cust_item by age
    age_groups = [0, 19, 29, 39, 150]
    sale_cust_item['age_group'] = [calculate_age_group(x, age_groups) for x in sale_cust_item['age']]

    # Group sale_cust_item by region
    regions = ['Eastern', 'Central', 'Mountain', 'Pacific']
    sale_cust_item['region'] = [calculate_region(x, regions) for x in sale_cust_item['customerAddress']]

    print(('Customers imported:', customers.count()), ' ')
    print(('Items imported:', items.count()), ' ')
    print(('Sales imported:', sales.count()), ' ')

    print('Customers group by Age')
    print_table_groupby_total(sale_cust_item, ['age_group', 'itemName'])

    print('Customers group by Region')
    print_table_groupby_total(sale_cust_item, ['region', 'itemName'])


def csv_import(file):
    result_set = pd.read_csv(file, parse_dates=True, infer_datetime_format=True)
    result_set = result_set.drop('lineId', axis=1)
    return result_set


def print_table_groupby_total(df: pd.DataFrame, group_by: list):
    # df = pd.DataFrame([{fn: getattr(f, fn) for fn in fields} for f in arr])
    dcf = df.groupby(group_by).size().groupby(level=len(group_by)-1, group_keys=False).nlargest(1)
    print(dcf)


def calculate_age_group(base_column: int, age_groups: list):
    age_from = age_groups[0]
    age_groups_upto = age_groups[1:]
    for idx, age_upto in enumerate(age_groups_upto):
        if len(age_groups) - 1 <= idx:
            break
        if filter_by_age(base_column, age_from, age_upto-1):
            result = '{0}-{1}'.format(age_from, age_upto-1)
            return result
        age_from = age_upto


def filter_by_age(age, age_from: int, age_upto: int) -> bool:
    """Customer entity."""
    return age_from <= age <= age_upto


def calculate_age(date) -> int:
    """Calculate age from birthday."""
    today = datetime.today()
    birthday = datetime.strptime(date, '%m/%d/%Y')
    return today.year - birthday.year - ((today.month, today.day) <
                                         (birthday.month, birthday.day))


def calculate_region(address: str, regions: list) -> str:
    """Customer entity."""
    gmaps = gm.Client(key='AIzaSyCY4P3c7BjpGgrxP8YyYJ6F2_TTWC4kl7U')
    geocode_result = gmaps.geocode(address)
    if len(geocode_result):
        time_zone = gmaps.timezone(geocode_result[0]['geometry']['location'])
        region = time_zone['timeZoneName'].partition(' ')[0]
        if region in regions:
            return region
        else:
            return ''
