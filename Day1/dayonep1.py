def DayOne(filename:str):

    counter = 1

    with open(filename,"r") as file:

        data = file.readlines()

        for i in range(len(data)-1):
            if data[i+1] > data[i]:
                counter += 1
            else:
                continue

    
    return counter

if __name__ == "__main__":
    import timeit
    # print(DayOne('Day1/input.txt'))
    time_average = []
    for i in range(5):
        n = int(10**i)
        time_average.append([n,timeit.timeit("DayOne('Day1/input.txt')",setup="from __main__ import DayOne",number=n)/n])
    import matplotlib.pyplot as plt

    plt.loglog([i[0] for i in time_average],[i[1] for i in time_average])

    plt.show()