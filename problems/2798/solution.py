_in = [int(x) for x in input().split()]
N = _in[0]
M = _in[1]
cards = [int(x) for x in input().split()]

result = 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      print(cards[i], cards[j], cards[k])
      v = cards[i]+ cards[j]+ cards[k]
      if result < v <= M:
        result = v
print(result)