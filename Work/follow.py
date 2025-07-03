# follow.py
import csv
import os
import time
import generators

## Without using a generator
# f = open('Data/stocklog.csv')
# f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

# while True:
#     line = f.readline()
#     if line == '':
#         time.sleep(0.1)   # Sleep briefly and retry
#         continue
#     fields = line.split(',')
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
    

# Read text file and yield lines
def follow(file):
    while True:
        line = file.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line  # Yield is a form of return; We can process line here or yield it for processing later

def follow_csv(file):
    while True:
        lines = csv.reader(file)
        if lines == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        # for line in lines:
        #     yield line  # line is a []
        return lines
        
def print_negative_changes(follows):
    for line in follows:
        fields = line.split(',')
        name = fields[0].strip('"')
        with open('Data/portfolio.csv') as file_obj:
            # f.seek(0, os.SEEK_END)
            if name in file_obj.read():
                price = float(fields[1])
                change = float(fields[4])
                if change < 0:
                    print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
                            
if __name__ == "__main__": 
    f = open('Data/stocklog.csv')
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
    f_generator = follow(f)
    # print_negative_changes(f_generator)
    
    fm_generator = generators.filematch(f_generator, 'IBM')
    for line in fm_generator:
        print(line.strip())
    
    # reader = csv.reader(f_generator)
    # for row in reader:
    #     print(row)  # ['MSFT', '30.20', '6/11/2007', '09:52.41', '0.15', '30.05', '30.20', '29.95', '7453568']
    

    
    
    f.close()