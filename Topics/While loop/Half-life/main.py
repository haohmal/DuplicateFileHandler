initial = int(input())
final = int(input())

periods = 0
while initial >= final:
    periods += 1
    initial //= 2

print(periods * 12)