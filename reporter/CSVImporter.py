"""reporter.CSVImporter: Imports CSV files."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
# import operator
import csv
import importlib

# import ptvsd
# ptvsd.enable_attach("my_secret", address = ('0.0.0.0', 8000))


class CSVImporter():
    """Imports CSV files."""

    def __init__(self, file_name, class_name):
        """Import csv anc create list of objects from it."""
        self.file_name = file_name
        self.class_name = class_name
        self.items = set()

        # Using inspect to generate class from class_name
        module = importlib.import_module('.' + class_name, 'reporter')
        class_ = getattr(module, class_name)

        # Sniffing csv dialect and reading file
        with open(file_name, 'rb') as csv_file:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))
            csv_file.seek(0)
            file_reader = csv.reader(csv_file, dialect)
            file_reader.next()
            # Iterating over file rows and appending new objects to items list
            for row in file_reader:
                self.items.add(class_(*row))

    def to_set(self):
        """Return item lists."""
        if self.items:
            return self.items
        else:
            raise Exception("Items set is empty.")

    def to_list(self):
        """Return item lists."""
        if self.items:
            return list(self.items)
        else:
            raise Exception("Items list is empty.")
