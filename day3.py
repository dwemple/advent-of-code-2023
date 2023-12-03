import time
start_time = time.time()

with open('day3-data.txt') as f:
    data = f.readlines()

class Gear:
  def __init__(self):
    self.number = 0
    self.isActive = False


def checkForSymbols(matrix, posx, posy):
  if posy != 0:
    if matrix[posy-1][posx] != "." and matrix[posy-1][posx].isdigit() == False:
      return True
    if posx != 0:
      if matrix[posy-1][posx-1] != "." and matrix[posy-1][posx-1].isdigit() == False:
        return True
    if posx != 139:
      if matrix[posy-1][posx+1] != "." and matrix[posy-1][posx+1].isdigit() == False:
        return True
  if posy != 139:
    if matrix[posy+1][posx] != "." and matrix[posy+1][posx].isdigit() == False:
      return True
    if posx != 0:
      if matrix[posy+1][posx-1] != "." and matrix[posy+1][posx-1].isdigit() == False:
        return True
    if posx != 139:
      if matrix[posy+1][posx+1] != "." and matrix[posy+1][posx+1].isdigit() == False:
        return True
  if posx != 0:
    if matrix[posy][posx-1] != "." and matrix[posy][posx-1].isdigit() == False:
      return True
  if posx != 139:
    if matrix[posy][posx+1] != "." and matrix[posy][posx+1].isdigit() == False:
      return True
  return False
result = 0
mx = [[0 for i in range(140)] for j in range(140)]
for i, line in enumerate(data):
    for j, char in enumerate(line.rstrip()):
      mx[i][j] = char

for y in range(0,140):
  isActive = False
  number = ""
  for x in range(0,140):
    if mx[y][x].isdigit():
      number += mx[y][x]
      if checkForSymbols(mx,x,y):
        isActive = True
      if x == 139 or (x != 139 and mx[y][x+1].isdigit() == False):
        if isActive:
          result += int(number)
        isActive = False
        number = ""

print(result)
end_time = time.time()
exec_time = (start_time - end_time) * -1000
print("Execution time: " + str(exec_time) + " ms")
