_ = int(input())
numbers = input().split(" ")

count = 0

def find(n):
  for i in range(3, round(number / 2) + 1, 2):
    if number % i == 0:
      return False
  return True

for number in numbers:
  number = int(number)
  if number == 1:
    continue
  if number == 2:
    count +=1
    continue
  if number % 2 == 0:
    continue
  if find(number):
    count += 1

print(count)