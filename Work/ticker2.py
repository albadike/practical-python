# ticker.py

from follow import follow_csv, print_negative_changes
import csv

def select_columns(rows, indices):
    for row in rows:
        if len(row) > max(indices):
            yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


if __name__ == '__main__':
    f = open('Data/stocklog.csv')
    lines = follow_csv(f)
    stock_generator = parse_stock_data(lines)
    for row_dict in stock_generator:
        print(row_dict)
        if row_dict['change'] < 0:
            print(f"{row_dict['name']:>10s} {row_dict['price']:>10.2f} {row_dict['change']:>10.2f}")