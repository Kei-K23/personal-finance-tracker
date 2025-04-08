import pandas as pd
from pathlib import Path
import os
import csv
import rich
from datetime import datetime
from .data_entry import DATE_FORMAT


class CSVHandler:
    CSV_FILE = "transactions.csv"
    CSV_FILE_PATH = ""
    COLUMNS = ["date", "amount", "category", "description"]

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

    def get_transactions(self, start_date, end_date):
        """Get transactions record based on date range"""
        df = pd.read_csv(self.CSV_FILE_PATH)
        df["date"] = pd.to_datetime(df["date"], format=DATE_FORMAT)
        start_date = datetime.strptime(start_date, DATE_FORMAT)
        end_date = datetime.strptime(end_date, DATE_FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            rich.print(
                "[yellow]No transactions found in the given date range.[/yellow]")
        else:
            rich.print(
                f"\n[bold]Transactions from {start_date.strftime(DATE_FORMAT)} to {end_date.strftime(DATE_FORMAT)}[/bold]")
            rich.print(filtered_df.to_string(
                index=False, formatters={"date": lambda x: x.strftime(DATE_FORMAT)}))

            total_income = filtered_df[filtered_df["category"]
                                       == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"]
                                        == "Expense"]["amount"].sum()
            rich.print("\n[bold]Summary:[/bold]")
            rich.print(f"Total Income: {total_income:.2f}")
            rich.print(f"Total Expense: {total_expense:.2f}")
            rich.print(f"Net Savings: {(total_income - total_expense):.2f}")

        return filtered_df
