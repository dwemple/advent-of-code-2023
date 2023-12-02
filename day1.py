import time
start_time = time.time()

with open('day1-data.txt') as f:
    data = f.readlines()

class numero:
    def __init__(self, i,v):
        self.index = i
        self.value = v
    def __lt__(self, other):
        return self.index < other.index
    
final = 0

numerinos = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def findNumbers(line):
    result = []
    for idx, char in enumerate(line):
        if char.isdigit(): 
            result.append(numero(idx,int(char)))
    for idx, i in enumerate(numerinos):
        if line.find(i) != -1:
            result.append(numero(line.find(i), idx+1))
        if line.rfind(i) != -1:
            if line.rfind(i) != result[-1].index:
              result.append(numero(line.rfind(i), idx+1))
    result.sort()
    end = str(result[0].value) + str(result[-1].value)
    return int(end) 

for line in data:
    final += findNumbers(line)
        
print(final)

end_time = time.time()

exec_time = (start_time - end_time) * -1000
print("Execution time: " + str(exec_time) + " ms")

