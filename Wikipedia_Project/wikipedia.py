import wikipedia
from random import randint

randomNum = randint(1,10000)
rayan = wikipedia.search("Rayan", results = randomNum)
for i in rayan:
    print(i)
print(f"The number of times generated is {randomNum}")