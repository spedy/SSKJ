import numpy as np

lines = open("score.txt").readlines()

words = np.random.choice(lines, 3, replace=False)

for word in words:
    print(word)
    raw_input("Press Enter to continue...")