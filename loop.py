# for
for i in range(10):
  print(f"{i} : 안녕")

# while
i = 0
while i < 10:
  print(f"{i} : 안녕")
  i += 1

# 무한루프
i = 0
while True:
  print(f"{i}: 무한루프 연습")
  i += 1
  if i > 10:
    break

# break
for i in range(3):
  print(f"{i}: break test")
  if i > 3:
    break

# continue
for i in range(3):
  print("continue test")
  if i < 2:
    continue
  print("did you pass continue?")