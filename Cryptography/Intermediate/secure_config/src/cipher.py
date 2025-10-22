#!/usr/bin/env python3
import os
import sys
"""
cipher.py
This script can be used to pass bytes through a home-grown cipher algorithm.
The cipher is symmetric, so you can pass plaintext in to get ciphertext,
and ciphertext in to get plaintext.
"""


def cipher(b):
    key = [0x11, 0x67, 0x41, 0xe2, 0x86, 0x33, 0xc3, 0xe0,
           0x54, 0x7a, 0x18, 0x21, 0x77, 0x2f, 0xa9, 0xb4]
    window = len(key)
    output = []
    offset = 0x3d
    i = 0
    while i < len(b):
        pt = b[i:i + window]
        for j, _ in enumerate(pt):
            output.append(pt[j] ^ key[j])
        key = [(k + offset) % 256 for k in key]
        i += window
    return bytes(output)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: cipher.py input_file output_file')
        exit()

    in_f = sys.argv[1]
    out_f = sys.argv[2]

    for fname in [in_f, out_f]:
        if not fname.endswith('.xml') and not fname.endswith('.enc'):
            print('Acceptable extensions are .xml and .enc')
            exit()

    if not os.path.isfile(in_f):
        print(f'File not found {in_f}')
        exit()

    if in_f == out_f:
        print('The input and output files cannot be the same.')
        exit()

    with open(in_f, 'rb') as f:
        data = f.read()

    output = cipher(data)

    with open(out_f, 'wb') as f:
        f.write(output)
