B = [5, -2, 7, 10, 3, -8, 4]

max_i = B.index(max(B))
min_i = B.index(min(B))

B[max_i], B[min_i] = B[min_i], B[max_i]

print("Після заміни:", B)

start = min(max_i, min_i) + 1
end = max(max_i, min_i)

print("Елементи між мінімальним і максимальним:", B[start:end])
