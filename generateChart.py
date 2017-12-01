
import matplotlib.pyplot as plt

line1 = plt.plot([100,200,500,1000,1500,2000], [2011,2820,6578,14369,21551,31948],label='One Process')
line2 = plt.plot([100,200,500,1000,1500,2000], [204,211,350,585,443,686],label='Two processes - Process 1')
line3 = plt.plot([100,200,500,1000,1500,2000], [1098,1281,4753,10526,7694,17863],label='Two processes - Process 2')


plt.setp(line1, color='r', linewidth=2.0)
plt.setp(line2, color='b', linewidth=2.0)
plt.setp(line3, color='g', linewidth=2.0)


plt.legend(loc='upper left')
plt.ylabel('Times')
plt.xlabel('Number of nodes')
plt.show()