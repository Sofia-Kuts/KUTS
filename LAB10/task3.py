import matplotlib.pyplot as plt

vowels = "aeiouAEIOU"

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

counter = {v: 0 for v in vowels}

for ch in text:
    if ch in counter:
        counter[ch] += 1

plt.bar(counter.keys(), counter.values())
plt.title("Частота голосних у тексті")
plt.xlabel("Голосні")
plt.ylabel("Кількість")

plt.savefig("hist.png")
plt.close()

print("hist.png збережено.")
