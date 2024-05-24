import wikipedia

for i in range(1,1000):
    randomPage = wikipedia.random(1) 
    print(f"Iteration {i} - {randomPage} - URL: https://en.wikipedia.org/wiki/Special:Random/{randomPage}")