from matplotlib import pyplot as plt

movies = ["Usual Suspects", "Shawshank", "Star Wars", "Goonies"]
watched_times = [3, 8, 10, 5]

plt.bar(range(len(movies)), watched_times)

plt.title("Potter's Movies")

plt.xticks(range(len(movies)), movies)

plt.show()
