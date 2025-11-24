n = int(input("Введіть кількість секунд :"))

hours = (n // 3600) % 24

rem = n % 3600
minutes = rem // 60
seconds = rem % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")