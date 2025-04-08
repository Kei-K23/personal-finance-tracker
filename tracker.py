from core import csv_handler, data_entry
from rich import print


def main():
    csv = csv_handler.CSVHandler()
    while True:
        print("\n[bold cyan]=== Personal Finance Tracker ===[/bold cyan]")
        print("1. Add a new transaction")
        print("2. View transactions and summary")
        print("3. Check monthly budget")
        print("4. View category summary")
        print("5. Plot transactions (line chart)")
        print("6. Plot monthly trend")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            date = data_entry.get_date(
                "Enter transaction date (dd-mm-yyyy) or leave blank for today: ", allow_default=True)
            amount = data_entry.get_amount()
            category = data_entry.get_category()
            description = data_entry.get_description()
            csv.add_entry(
                date=date, amount=amount, category=category, description=description)
        elif choice == "2":
            start_date = data_entry.get_date("Enter start date (dd-mm-yyyy): ")
            end_date = data_entry.get_date("Enter end date (dd-mm-yyyy): ")
            csv.get_transactions(start_date, end_date)
        elif choice == "7":
            print("[bold green]Goodbye![/bold green]")
            break
        else:
            print("[red]Invalid choice.[/red]")


if __name__ == "__main__":
    main()
