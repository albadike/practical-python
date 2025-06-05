dicti = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}

print('{name:>10s} {shares:10d} {price:10.2f}'.format_map(dicti))

print('{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1))

print('{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1))

# C-style (printf-style) String Formatting
print()
print('The value is %d' % 3)

print('%5d %-5d %10d' % (3, 4, 5))

print('%0.2f' % 3.1415926)


# Byte string
print()
print(b'%s has %d messages' % (b'Dave', 37))

print(b'%b has %d messages' % (b'Dave', 37))  # %b may be used instead of %s