# Generators for file processing

"""_summary_
Generators are a powerful feature in Python that allow you to iterate over data without loading everything into memory at once.
This is particularly useful for processing large files or streams of data.
In this example, we demonstrate how to use generators to filter lines from a file based on a substring match.

Key Points:
1. Generators are defined using the 'yield' keyword, which allows you to produce a series of values over time.
2. The `filematch` function reads lines from a file and yields only those that contain a specified substring.
3. This approach is memory efficient, as it processes one line at a time instead of loading the entire file into memory.
4. The example also includes a commented-out section that demonstrates how to use the generator with a file.
5. Memory Considerations: List comprehensions generate the entire list in memory eagerly.
For very large datasets, this can lead to performance bottlenecks, and generator expressions might be a more suitable choice for memory efficiency.

Memory Considerations: List comprehensions generate the entire list in memory eagerly. 
For very large datasets, this can lead to performance bottlenecks, 
and generator expressions might be a more suitable choice for memory efficiency.

Why is this useful for generators?
1. Efficiency: You can process huge (or infinite) data streams without loading everything into memory.
2. Laziness: Data isn't produced until you actually need it.
3. Composability: You can chain, filter, and combine generators/functions cleanly.

# itertools Module
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
"""

# def filematch(filename, substr):
#     with open(filename, 'r') as f:
#         for line in f:
#             if substr in line:
#                 yield line

# Filter and yield lines containing a substring
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

# if __name__ == "__main__":
#     for line in filematch('Data/portfolio.csv', 'MSFT'):
#         print(line.strip())
#     print("---End of file.---")
