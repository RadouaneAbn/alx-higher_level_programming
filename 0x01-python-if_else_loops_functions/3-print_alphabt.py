#!/usr/bin/python3

for idx_ascii in range(97, 123):
    if chr(idx_ascii) == 'q' or chr(idx_ascii) == 'e':
        continue
    print("{c}".format(c=chr(idx_ascii)), end='')
