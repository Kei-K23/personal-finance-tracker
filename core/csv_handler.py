import pandas as pd
from pathlib import Path
import os
import csv


class CSVHandler:
    CSV_FILE = "transactions.csv"
    CSV_FILE_PATH = ""
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    def __init__(self):
        # Setup CSV file path
        cwd = Path.cwd()
        self.CSV_FILE_PATH = os.path.join(cwd, self.CSV_FILE)

    @classmethod
    def initialize_csv(cls):
        """Load CSV file, when not found create new CSV"""
        try:
            pd.read_csv(cls.CSV_FILE_PATH)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(path_or_buf=cls.CSV_FILE_PATH, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """Add new entry row to CSV"""
        new_row = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }

        with open(cls.CSV_FILE_PATH, mode='a', newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_row)
        print("Entry added successfully")
