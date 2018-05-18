for i in range(1,1000):
  if i % 2 != 0:
    print(i)
for j in range(5,1000000):
  if j % 5 == 0:
    print(j)
a = [1, 2, 5, 10, 255, 3]
amount = sum(a)
print(amount)

average = amount / float(len(a))
print(average)