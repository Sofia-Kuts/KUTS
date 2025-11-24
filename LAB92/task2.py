count = 0
prev = None

while True:
    n = int(input())
    if n == 0:
        break

    if prev is not None :
        if (prev > 0 and n < 0) or (prev < 0 and n > 0):
            count += 1

    prev = n
print(count)


