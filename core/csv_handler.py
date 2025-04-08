import pandas as pd
from pathlib import Path
import os
import csv
import rich


class CSVHandler:
    CSV_FILE = "transactions.csv"
    CSV_FILE_PATH = ""
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    def __init__(self):
        # Setup CSV file path
        cwd = Path.cwd()
        self.CSV_FILE_PATH = os.path.join(cwd, self.CSV_FILE)
        self.initialize_csv()

    def initialize_csv(self):
        """Load CSV file, when not found create new CSV"""
        try:
            pd.read_csv(self.CSV_FILE_PATH)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.COLUMNS)
            df.to_csv(path_or_buf=self.CSV_FILE_PATH, index=False)

    def add_entry(self, date, amount, category, description):
        """Add new entry row to CSV"""
        new_row = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }

        with open(self.CSV_FILE_PATH, mode='a', newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.COLUMNS)
            writer.writerow(new_row)
        rich.print("[green]Entry added successfully![/green]")
