_in = [int(x) for x in input().split()]
N = _in[0]
M = _in[1]
board = [[x for x in input()] for _ in range(N)]


def have_to_change(a, b):
    return [
        [
            1
            if ((x + y) % 2 == 0 and item == a) or ((x + y) % 2 == 1 and item == b)
            else 0
            for x, item in enumerate(row)
        ]
        for y, row in enumerate(board)
    ]


def take_subset(data, xs, ys, xe, ye):
    return [
        [item for xi, item in enumerate(row) if xs <= xi < xe]
        for yi, row in enumerate(data)
        if ys <= yi < ye
    ]


a = have_to_change("B", "W")
b = have_to_change("W", "B")

min = N * M

for x in range(M - 7):
    for y in range(N - 7):
        count_a = sum(sum(take_subset(a, x, y, x + 8, y + 8), []))
        count_b = sum(sum(take_subset(b, x, y, x + 8, y + 8), []))
        if count_a < min:
            min = count_a
        if count_b < min:
            min = count_b

print(min)
