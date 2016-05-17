import matplotlib.pyplot as plt


#y = [1, 2, 3, 4, 5]
#x = [10,20,30,40,50]

x = list(range(10,500,10))
y = list(range(10,500,10))
plt.plot(x, y, color='r',label='line')
plt.legend(loc='upper left')
plt.show()
