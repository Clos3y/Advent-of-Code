import numpy as np

def DayOne(filename: str):
	counter = 0

	with open(filename, "r") as file:

		data = file.readlines()

	tempdat = []

	for i in range(len(data) - 2):
		tempdat.append(np.sum(list(map(int,data[i:i+3])),dtype=int))

	for i in range(len(tempdat) - 1):
		if tempdat[i+1] > tempdat[i]:
			counter += 1
		else:
			continue

	return counter


if __name__ == "__main__":
   import timeit
   time_average = []
   for i in range(5):
       n = int(10**i)
       time_average.append([n,
                            timeit.timeit("DayOne('Day1/input.txt')",
                                          setup="from __main__ import DayOne",
                                          number=n) / n])
   import matplotlib.pyplot as plt

   plt.loglog([i[0] for i in time_average], [i[1] for i in time_average])

   plt.show()
