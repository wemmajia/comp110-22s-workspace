"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)

    # Close the file to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform row tablee to column table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for key in column_table:
        if n >= len(column_table[key]):
            return column_table
            
        values: list[str] = []
        i: int = 0
        while i < n:
            values.append(column_table[key][i])
            i += 1
        result[key] = values

    return result


def select(ct: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = ct[column]
    return result


def concat(ct: dict[str, list[str]], ct2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for key in ct:
        result[key] = ct[key]
    for key in ct2:
        if key in result:
            result[key] += ct2[key]
        else:
            result[key] = ct2[key]
    
    return result


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result