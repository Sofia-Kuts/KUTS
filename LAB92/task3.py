def decode(binary):
    result = ""
    zeros = 0

    for ch in binary:
        if ch == '0':
            zeros += 1
        else:
            letter = chr(ord('a') + zeros)
            result += letter
            zeros = 0

    return result

import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        print(decode(line))
