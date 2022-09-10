_in = [int(x) for x in input().split()]
N = _in[0]
K = _in[1]

cursor = 0
people = list(range(1, N + 1))
result = []

for _ in range(N):
    cursor += K - 1
    cursor %= len(people)
    result.append(str(people.pop(cursor)))

print("<{}>".format(", ".join(result)))
