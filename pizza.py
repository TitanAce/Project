import csv
import sys
from tabulate import tabulate

def render_prices(file_path):
    try:
        with open(file_path) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")
    except csv.Error as e:
        sys.exit(f"CSV Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("No command-line arguments provided")
    elif len(sys.argv) == 2:
        if not sys.argv[1].lower().endswith('.csv'):
            sys.exit("Not a CSV file")
        render_prices(sys.argv[1])
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
