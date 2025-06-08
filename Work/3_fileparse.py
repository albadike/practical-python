# fileparse.py
#
# Exercise 3.3

import csv
import pprint
import sys

# def parse_csv(filename, select):
#     '''
#     Parse a CSV file into a list of records
#     '''

#     with open(filename) as f:
#         rows = csv.reader(f)

#         # Read the file headers
#         headers = next(rows)
#         record_list = []
#         for row in rows:
#             if not row:    # Skip rows with no data
#                 continue
#             # Create a dictionary for each row
#             record_dict = dict(zip(headers, row))

#             # Filter selections as a dictionary
#             record_dict = {key: record_dict[key] for key in select if key in record_dict}
#             if record_dict:
#                 record_list.append(record_dict)

#     return record_list


# Method 2
def parse_csv(file, select, types=None, has_header=False, silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    random_headers = []
    reader = csv.reader(file)

    # Read the file headers
    headers = next(reader)
    indices = []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select and has_header:
        try:
            indices = [headers.index(colname) for colname in select]
            headers = select
        except ValueError as e:
            if not silence_errors:
                print(f"**Error: Invalid column names! If your data contains column headers, confirm they are correctly set in 'select' and 'has_headers' arg - {e}**")

    else:
        random_headers = [f'col{r}' for r in range(1, len(headers)+1)]
        print(
            f'**No header found, using default headers: {random_headers}**')

    records = []
    line_num = 1
    for row in reader:
        line_num += 1

        if not row:    # Skip rows with no data
            continue

        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]
        else:
            # Even when users have no selection, they provide data types they are interested in
            types = None
            headers = random_headers
    
            try:
                # row = [row[s] for s in select]
                # headers = [headers[s] for s in select]
                
                # Alternative one-liner
                row, headers = ([src[i-1] for i in select] for src in (row, headers))
            except IndexError as e:
                if not silence_errors:
                    print(f"**Error: Did you forget to set has_headers=True/False? {e}**")
                break
            except TypeError as e:
                if not silence_errors:
                    print(f"**Error: Did you select the right columns -: 'name' vs 1? {e}**")
                sys.exit(1) 

        # Convert each row value to the user's desired types
        if types:
            try:
                row = [typ(val) for typ, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"**Error: Row {line_num}: Invalid data type conversion in {row}! {e}**")
                continue
                # sys.exit(1)  # Stop the program immediately

        # Make a dictionary
        record = dict(zip(headers, row))
        records.append(record)
    return records


def main():
    """Main function to demonstrate CSV parsing."""
    
    filename = 'Work/Data/portfolio.csv'
    select = ['name', 'price']             # Select columns by index; or by name if has_header=True
    types = [str, float]
    has_header = True                      # Set to False if the file has no header row
    silence_errors = True                  # Set to False to see error messages

    with open(filename, 'rt') as file: 
        try:
            records = parse_csv(file, select=select, types=types, has_header=has_header)
        except TypeError as e:
            if not silence_errors:
                print(f"**Error: File not found or mismatched 'select' columns {e}**")
            # Stop the program immediately
            raise   # 1 is conventional for error; 0 for clean exit

    pprint.pprint(records)
    
    
if __name__ == '__main__':
    main()
    
