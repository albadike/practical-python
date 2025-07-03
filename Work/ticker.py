# ticker.py

from follow import follow_csv, print_negative_changes

def parse_stock_data(lines):
    for line in lines:
        line = select_columns(line, [0, 1, 4])
        return line
        
def select_columns(row, indices):
    # if len(row) > max(indices):
    #     yield [row[index] for index in indices]
    
    # Alternatively, using generator expression. NOTE: return
    return (row[index] for index in indices if index < len(row))

if __name__ == '__main__':
    f = open('Data/stocklog.csv')
    lines = follow_csv(f)
    stock_generator = parse_stock_data(lines)
    for row_list in stock_generator:
        print(row_list)