import time
start_time = time.time()

with open('day4-data.txt') as f:
    data = f.readlines()
result = 0
for line in data:
  count = 0
  first = True
  temp = line.split(":")
  numbers = temp[1].split("|")
  winning = ' '.join(numbers[0].split(" ")).split()
  scratch = ' '.join(numbers[1].split(" ")).split()
  for number in winning:
    if number in scratch:
      count *= 2
      if(first):
        count = 1
        first = False
  first = True
  result += count
  count = 0
print(result) 
end_time = time.time()
exec_time = (start_time - end_time) * -1000
print("Execution time: " + str(exec_time) + " ms")

start_time = time.time()

scratchcards = [1 for j in range(220)]
result2 = 0
for i,line in enumerate(data):
  for _ in range(scratchcards[i]):
    first = True
    count = 0
    temp = line.split(":")
    numbers = temp[1].split("|")
    winning = ' '.join(numbers[0].split(" ")).split()
    scratch = ' '.join(numbers[1].split(" ")).split()
    for number in winning:
      if number in scratch:
        count += 1
    for j in range(1,count+1):
      if i+j >= 220:
        continue
      scratchcards[i+j] += 1
    count = 0
for item in scratchcards:
  result2 += item
print("Result 2: " + str(result2)) 
end_time = time.time()
exec_time = (start_time - end_time) * -1000
print("Execution time: " + str(exec_time) + " ms")
