from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(prompt, allow_default=False):
    """Get date from user input"""
    date_str = input(prompt)
    # Return current date
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)

    try:
        # Check input date have this "%d-%m-%Y" format
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        # Format "%d-%m-%Y" and return date format as string
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        # Recursive call when user type wrong date format
        get_date(prompt, allow_default)


def get_amount():
    """Get amount from user input"""
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError(
                "Amount must be a non-negative or non-zero value.")
        return amount

    except ValueError as err:
        print(err)
        get_amount()


def get_category():
    """Get category from user input"""
    category = input(
        "Enter category ('I/i' for Income or 'E/e' for Expense): ").upper()

    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I/i' for Income or 'E/e' for Expense.")
    get_category()


def get_description():
    """Get description from user input"""
    return input("Enter a description (Optional): ")
