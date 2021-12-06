import numpy as np

def fish_takeover(days : int, file : str) -> int:
	with open(file,"r") as fish_data:
		fish = fish_data.read()
		fish = np.fromiter(map(lambda x: np.byte(x),fish[0::2]),dtype=np.byte)

		for i in range(days):

			for k,j in np.ndenumerate(fish):
				if j - 1 >= 0:
					fish[k] -= 1
				else:
					fish[k] = 6
					fish = np.append(fish,8)

		return fish.size

print(fish_takeover(256,"input.txt"))
