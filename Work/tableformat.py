# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''

    def headings(self, headers):
        for h in headers:
            print(f'{h.title():>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''

    def headings(self, headers):
        headers = [h.title() for h in headers]  # Capitalize headers
        print(','.join(headers))

    def row(self, rowdata):
        rowdata=[str(data) for data in rowdata]
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''

    def headings(self, headers):
        print('<table>')
        print('  <tr>')
        for h in headers:
            print(f'    <th>{h.title()}</th>')
        print('  </tr>')

    def row(self, rowdata):
        print('  <tr>')
        for d in rowdata:
            print(f'    <td>{d}</td>')
        print('  </tr>')
#     print('</table>')
        print('</table>')


def create_formatter(name):
    '''
    Factory function to create a formatter based on the name.
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown formatter type: {name}')
    
def print_table(data, headers, table_formatter):
    '''
    Print the table using the specified formatter.
    '''
    table_formatter.row(data)