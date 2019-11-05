# umm well below given are some examples of continue statement

numbersTaken = [1, 2, 3, 4, 5, 6]

print("Here are the numbers that are still available:")

for x in range(1,20):
    if x in numbersTaken:
        continue
    print(x)