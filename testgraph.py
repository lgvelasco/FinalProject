import Screenplay as sp

import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt

annie_hall = sp.Screenplay('Annie_Hall.txt')
annie_hall.print()
print(annie_hall.get_characters())
print(annie_hall.divide_by_scenes())
print(annie_hall.get_sentiment())
print(len(annie_hall.divide_by_scenes()))


x = []
for i in range(len(annie_hall.divide_by_scenes())):
    x.append(i+1)

y = annie_hall.get_sentiment()
fig, ax = plt.subplots()
plt.plot(x, y)
plt.title(annie_hall.get_title(), fontsize=32)
plt.ylim((-0.75, 0.75))
plt.ylabel("Sentiment Polarity")
plt.xlabel("Running Time")
# plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
ttl = ax.title
ttl.set_position([.5, 1.05])

plt.show()