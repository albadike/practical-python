# testing

def parse_csv(filename, select, types, has_header=True):
    '''
    Parse a CSV file into a list of records (dictionaries or tuples).

    Parameters:
    filename: str
        The path to the CSV file.
    select: list of str
        The column names to select (if has_header is True).
    types: list of types
        The types to which to convert each column.
    has_header: bool
        Whether the CSV file has a header row.

    Returns:
    list of dict or list of tuple
        A list of records, either as dictionaries (if has_header is True) or tuples (if has_header is False).
    '''
    import csv

    with open(filename, 'r') as f:
        rows = csv.reader(f)

        if has_header:
            headers = next(rows)
            indices = [headers.index(colname) for colname in select]
            records = []
            for row in rows:
                if not row:  # skip empty rows
                    continue
                selected_row = [row[index] for index in indices]
                typed_row = [func(val) for func, val in zip(types, selected_row)]
                record = dict(zip(select, typed_row))
                records.append(record)
        else:
            records = []
            for row in rows:
                if not row:  # skip empty rows
                    continue
                typed_row = [func(val) for func, val in zip(types, row)]
                record = tuple(typed_row)
                records.append(record)

    return records

def print_greetings(names):
    for name in names:
        print(f"Hello, {name}!")