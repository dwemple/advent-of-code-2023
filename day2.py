import time
start_time = time.time()

class Possibility:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue

goal = Possibility(12,13,14)

class Game:
   def __init__(self, gameNumber, results):
      self.gameNumber = gameNumber
      self.rounds = []
      self.count = True
      self.max = Round()
      self.max.red = 0
      self.max.green = 0
      self.max.blue = 0
      for item in results:
        temp = item.split(",")
        round = Round()
        for color in temp:
          if color.find("blue") != -1:
              round.blue = int(color[0:3])
          if color.find("red") != -1:
             round.red = int(color[0:3])
          if color.find("green") != -1:
             round.green = int(color[0:3])
        if round.compare(goal):
           self.count = False
        if round.red > self.max.red:
           self.max.red = round.red
        if round.blue > self.max.blue:
           self.max.blue = round.blue
        if round.green > self.max.green:
           self.max.green = round.green
        #print(round.blue, round.green, round.red)
        round = Round()

        
             
class Round:
  def __init__(self):
     self.red = 0
     self.green = 0
     self.blue = 0
  def compare(self, other):
     if self.red > other.red or self.blue > other.blue or self.green > other.green:
        return True
     else: 
        return False
            

with open('day2-data.txt') as f:
    data = f.readlines()
result = 0
result2 = 0
games = []
for line in data:
  temp = line.split(":")
  game = [int(i) for i in temp[0].split() if i.isdigit()]
  rounds = temp[1].split(";")
  current = Game(game[0], rounds)
  if current.count:
     result += current.gameNumber
  result2 += current.max.red * current.max.green * current.max.blue
  


print("Result: " + str(result) + ", result 2: " + str(result2))

end_time = time.time()

exec_time = (start_time - end_time) * -1000
print("Execution time: " + str(exec_time) + " ms")
