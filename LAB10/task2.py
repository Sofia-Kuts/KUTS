
with open("letters.txt", "w", encoding="utf-8") as f:
    for i in range(1, 10):
        f.write("a" * i + "\n")

print("Файл letters.txt створено.")
