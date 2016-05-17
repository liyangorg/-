import numpy as np
import matplotlib.pyplot as plt

n_groups = 4

distances = [11, 13, 16, 17]

fix, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.7

opacity = 0.4
rects = plt.bar(index, distances, bar_width,alpha=opacity, color='b',label=    'Men')

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.ylim(0,40)
plt.legend()

plt.tight_layout()
plt.show()
