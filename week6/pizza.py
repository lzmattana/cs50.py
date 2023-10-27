import sys
import csv
from tabulate import tabulate

# Validate the command-line argument
if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
    sys.exit("Usage: python pizza.py <input.csv")

# Read the CSV file and handle file existence errors
try:
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

# Verify the CSV structure
if not reader.fieldnames:
    sys.exit("CSV file is empty")
expected_columns = reader.fieldnames  # Dynamically determine expected columns

# Format the data into an ASCII art table
formatted_table = tabulate(data, headers='keys', tablefmt='grid')

# Print the formatted table
print(formatted_table)
